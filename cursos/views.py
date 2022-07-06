from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import UpdateView

from .models import Cursos
from .forms import CursoForm


def curso(request, slug):
    curso = get_object_or_404(Cursos, slug=slug)

    return render(request, "cursos/curso.html", {"curso": curso})


def curso_editar(request):
    return render(request, "cursos/curso-editar.html")


def add_curso(request):
    if request.method == "POST":
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = CursoForm()
    return render(request, "cursos/curso-crear.html", {"form": form})


def edit_curso(request, pk):
    curso = Cursos.objects.get(id=pk)
    form = CursoForm(instance=curso)

    if request.method == "POST":
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = CursoForm(instance=curso)

    return render(request, "cursos/curso-edit.html", {"form": form})

def delete_curso(request, pk):
    curso = Cursos.objects.get(id=pk)
    curso.delete()

    return redirect("index")
