from django.shortcuts import render, get_object_or_404, redirect

from .models import Cursos, Review
from .forms import CursoForm


def curso(request, slug):
    curso = get_object_or_404(Cursos, slug=slug)

    if request.method == "POST":
        rating = request.POST.get("rating", 3)
        content = request.POST.get("content", "")

        if content:
            reviews = Review.objects.filter(created_by=request.user, product=curso)

            if reviews.count() > 0:
                review = reviews.first()
                review.rating = rating
                review.content = content
                review.save()
            else:
                review = Review.objects.create(
                    product=curso,
                    rating=rating,
                    content=content,
                    created_by=request.user,
                )

            return redirect("producto", slug=slug)

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


# def add_review(request):
#     if request.method == "POST":
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("/")
