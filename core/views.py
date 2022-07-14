from django.contrib.auth import login
from django.db.models import Q
from django.shortcuts import render, redirect

from cursos.models import Cursos, Category, Review
from .forms import SignUpForm

# Create your views here.


def index(request):
    cursos = Cursos.objects.all()[0:8]
    return render(request, "core/index.html", {"cursos": cursos})


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('/')

    else:
        form = SignUpForm()

    return render(request, "core/signup.html", {"form": form})


def login_(request):
    return render(request, "core/login.html")


def about(request):
    return render(request, "core/about.html")


def shop(request):
    categorias = Category.objects.all()
    cursos = Cursos.objects.all()

    categoria_activa = request.GET.get("category", "")

    if categoria_activa:
        cursos = cursos.filter(category__slug=categoria_activa)

    query = request.GET.get("query", "")

    if query:
        cursos = cursos.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )

    context = {
        "cursos": cursos,
        "categorias": categorias,
        "categoria_activa": categoria_activa,
    }

    return render(request, "core/shop.html", context)
