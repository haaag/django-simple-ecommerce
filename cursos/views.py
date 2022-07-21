from django.shortcuts import render, get_object_or_404, redirect

from .models import Cursos, Review
from .forms import CursoForm


def curso(request, slug):
    MAX_RATING = 6

    curso = get_object_or_404(Cursos, slug=slug)

    review_avg = round(
        sum([rating.rating for rating in curso.reviews.all()])
        // len(curso.reviews.all()),
        2,
    )

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

    return render(
        request, "cursos/curso.html", {"curso": curso, "review_avg": review_avg}
    )


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
            return redirect("producto", curso.slug)
    else:
        form = CursoForm(instance=curso)

    return render(request, "cursos/curso-edit.html", {"form": form, "curso": curso})


def delete_curso(request, pk):
    curso = Cursos.objects.get(id=pk)
    curso.delete()

    return redirect("index")
