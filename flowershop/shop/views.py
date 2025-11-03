from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

from .models import *


def home(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('shop:profile')
        else:
            return render(request, 'shop:home', {'form': {'errors': True}})
    
    return render(request, 'shop/home.html')

def registration(request):
    return render(request, 'shop/registration.html')

def main(request):
    return render(request, 'shop/main.html')

# изменения не нужны
def about_us(request):
    return render(request, 'shop/ProNas_info.html')
def delivery(request):
    return render(request, 'shop/dostavka_info.html')
def payment(request):
    return render(request, 'shop/oplata_info.html')


def pro_tovar(request):
    return render(request, 'shop/pro_tovar.html')

def oplata(request):
    return render(request, 'shop/oplata.html')

@login_required(login_url='shop:home')
def profile(request):
    return render(request, 'shop/profile.html')

def sposob_oplaty(request):
    return render(request, 'shop/sposob_oplaty.html')


