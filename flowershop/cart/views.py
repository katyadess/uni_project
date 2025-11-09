from django.shortcuts import render, redirect
from .cart import Cart
from orders.forms import OrderForm
from orders.models import *
from shop.models import *
from django.contrib.auth.decorators import login_required
from random import sample
from datetime import timedelta
from django.utils import timezone

threshold = timezone.now() - timedelta(hours=1)
# Create your views here.

@login_required(login_url='shop:home')
def cart(request):
    cart = Cart(request)
    order_form = OrderForm(request.POST or None)
    
    Order.objects.filter(
        user=request.user,
        is_paid=False,
    ).exclude(payment_method='cash').filter(
        created_at__lt=threshold
    ).delete()
    
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
            
            item = cart.cart.get(str(bouquet.id))
            if item and item['quantity'] > 1:
                cart.add(bouquet, -1, update_quantity=False)
            else:
                cart.remove(bouquet)
           
            
        elif 'proceed-to-checkout' in request.POST:
            
            order_form = OrderForm(request.POST)
            if order_form.is_valid():
                    
                order = order_form.save(commit=False)
                order.user = request.user
            
                order.delivery_method = request.POST.get('delivery_method', 'standard')
                order.time = request.POST.get('time') or None
                order.date = request.POST.get('date')
                order.user_name = request.POST.get('user_name')
                order.user_tel = request.POST.get('user_tel')
                order.recipient_name = request.POST.get('recipient_name')
                order.recipient_phone = request.POST.get('recipient_phone')
                order.add_card = 'add_card' in request.POST
                order.card_message = request.POST.get('card_message')
                order.street = request.POST.get('street')
                order.house = request.POST.get('house')
                order.apartment = request.POST.get('apartment')
                order.unknown_address = 'unknown_address' in request.POST
                
                
                order.save()
                
                for item in cart:
                    OrderItem.objects.create(
                        order=order,
                        bouquet=item['bouquet'],
                        price=item['price'],
                        quantity=item['quantity']
                    )
                cart.clear() 
            
            request.session['can_access_sposob_oplaty'] = True
            return redirect('shop:sposob_oplaty', order_id=order.id)
            
        elif 'add-to-cart' in request.POST:
            bouquet_id = request.POST.get('bouquet_id') 
            bouquet = Bouquet.objects.get(id=bouquet_id)
            cart.add(bouquet)
            return redirect('cart:cart')
    
        return redirect('cart:cart')
    
    return render(request, 'cart/cart.html', {
        'cart': cart,
        'suggested': suggested,
        'order_form': order_form,
    }) 