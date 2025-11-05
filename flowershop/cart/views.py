from django.shortcuts import render, redirect
from .cart import Cart
from shop.models import *
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='shop:home')
def cart(request):
    cart = Cart(request)
    
    if request.method == 'POST':
        if 'remove' in request.POST:
            bouquet_id = request.POST.get('bouquet_id') 
            bouquet = Bouquet.objects.get(id=bouquet_id)
            
            cart.remove(bouquet)  
            return redirect('cart:cart') 
        elif 'increase' in request.POST:
            bouquet_id = request.POST.get('bouquet_id') 
            bouquet = Bouquet.objects.get(id=bouquet_id)
            
            cart.add(bouquet)
        elif 'decrease' in request.POST:
            bouquet_id = request.POST.get('bouquet_id') 
            bouquet = Bouquet.objects.get(id=bouquet_id)
            
            cart.add(bouquet, -1, update_quantity=False)
    
        return redirect('cart:cart')
    
    return render(request, 'cart/cart.html', {
        'cart': cart,
    }) 