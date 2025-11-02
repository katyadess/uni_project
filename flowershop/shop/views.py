from django.shortcuts import render
from .models import Bouquet

def home(request):
    return render(request, 'shop/home.html')

def main(request):
    return render(request, 'shop/main.html')

def registration(request):
    return render(request, 'shop/registration.html')

def about_us(request):
    return render(request, 'shop/ProNas_info.html')

def delivery(request):
    return render(request, 'shop/dostavka_info.html')

def payment(request):
    return render(request, 'shop/oplata_info.html')

def flower_detail(request):
    return render(request, 'shop/pro_tovar.html')
