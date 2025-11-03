from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import *
from .models import *


def home(request):
    form = LoginForm(request.POST or None)
     
    if request.method == "POST" and form.is_valid():
        email = form.cleaned_data["email"]
        password = form.cleaned_data["password"]
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('shop:profile')
        else:
            form.add_error(None, 'Невірна пошта або пароль.')
    
    return render(request, 'shop/home.html', {'form': form})

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

def shop_logout(request):
    logout(request)
    return redirect('shop:home')

def sposob_oplaty(request):
    return render(request, 'shop/sposob_oplaty.html')

