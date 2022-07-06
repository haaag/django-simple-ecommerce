from django.urls import path

from .views import add_to_cart, cart, checkout

urlpatterns = [
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', cart, name='cart'),
    path('cart/checkout/', checkout, name='checkout'),
]
