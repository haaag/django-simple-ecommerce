from django.urls import path
from django.contrib.auth import views

import core.views as core


urlpatterns = [
    path("", core.index, name="index"),
    path("shop/", core.shop, name="shop"),
    path("signup/", core.signup, name="signup"),
    path(
        "login/", views.LoginView.as_view(template_name="core/login.html"), name="login"
    ),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("about/", core.about, name="about"),
]
