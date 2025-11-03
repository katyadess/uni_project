from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='shop:home')
def order(request):
    return render(request, 'orders/zamovlenya_usp.html')
