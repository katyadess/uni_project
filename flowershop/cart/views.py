from django.shortcuts import render, redirect
from .cart import Cart
from shop.models import *
from django.contrib.auth.decorators import login_required
from random import sample
# Create your views here.

@login_required(login_url='shop:home')
def cart(request):
    cart = Cart(request)
    
    bouquets = list(Bouquet.objects.all())
    try:
        suggested = sample(bouquets, 2)
    except ValueError:
        suggested = bouquets
    
    
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
            
        elif 'proceed-to-checkout' in request.POST:
            if len(cart) >= 1:
                request.session['can_access_sposob_oplaty'] = True
                return redirect('shop:sposob_oplaty')
            else:
                return redirect('cart:cart')
            
        elif 'add-to-cart' in request.POST:
            bouquet_id = request.POST.get('bouquet_id') 
            bouquet = Bouquet.objects.get(id=bouquet_id)
            cart.add(bouquet)
            return redirect('cart:cart')
    
        return redirect('cart:cart')
    
    return render(request, 'cart/cart.html', {
        'cart': cart,
        'suggested': suggested,
    }) 