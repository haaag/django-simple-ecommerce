from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


import carrito.views as cart

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
    path("", include("carrito.urls")),
    path("add_to_cart/<int:product_id>", cart.add_to_cart, name="add_to_cart"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
