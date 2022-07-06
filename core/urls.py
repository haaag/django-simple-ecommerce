from django.urls import path
from django.contrib.auth import views

import core.views as core
import cursos.views as product


urlpatterns = [
    path("", core.index, name="index"),
    path("shop/", core.shop, name="shop"),
    path("shop/<slug:slug>", product.curso, name="producto"),
    path("curso/", product.curso, name="curso"),
    path("add-curso/", product.add_curso, name="crear-curso"),
    path("edit-curso/<int:pk>", product.edit_curso, name="edit-curso"),
    path("delete-curso/<int:pk>", product.delete_curso, name="delete-curso"),
    path("signup/", core.signup, name="signup"),
    path("login/", views.LoginView.as_view(template_name="core/login.html"), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("about/", core.about, name="about"),
]
