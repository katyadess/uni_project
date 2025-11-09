from django.shortcuts import render, redirect
from .models import *
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='shop:home')
def order(request, order_id):
    
    order = get_object_or_404(Order, id=order_id, user=request.user, is_active=True)
    order.status = 'paid'
    order.is_active = False
    order.save()
    return render(request, 'orders/zamovlenya_usp.html', {
        'order': order,
    })
 