from .cart import Cart

def cart(request):
    return {'сart': Cart(request)}