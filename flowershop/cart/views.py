from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='shop:home')
def cart(request):
    return render(request, 'cart/cart.html')