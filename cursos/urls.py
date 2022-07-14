from django.urls import path

import cursos.views as product


urlpatterns = [
    path("shop/<slug:slug>", product.curso, name="producto"),
    path("curso/", product.curso, name="curso"),
    path("add-curso/", product.add_curso, name="crear-curso"),
    path("edit-curso/<int:pk>", product.edit_curso, name="edit-curso"),
    path("delete-curso/<int:pk>", product.delete_curso, name="delete-curso"),
]
