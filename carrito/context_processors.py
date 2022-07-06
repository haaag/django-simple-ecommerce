from .carrito import Cart


def cart(request):
    return {"carrito": Cart(request)}
