from django.shortcuts import render
from .models import Bouquet

def home(request):
    return render(request, 'shop/home.html')

def main(request):
    return render(request, 'shop/main2.html')

def registration(request):
    return render(request, 'shop/registration.html')

def flower_detail(request):
    return render(request, 'shop/pro_tovar.html')
