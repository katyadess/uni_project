from django.shortcuts import render, redirect
from .models import *
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='shop:home')
def order(request, order_id):
    
    if not request.session.get('can_access_order_page'):
        return redirect('shop:oplata', order_id=order_id)
    
    del request.session['can_access_order_page']
    
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'orders/zamovlenya_usp.html', {
        'order': order,
    })
 