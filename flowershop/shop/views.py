from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from .forms import *
from .models import *
from django.core.paginator import Paginator
from django.db.models import Q
from django.db.models.functions import Lower

def home(request):
    form = LoginForm(request.POST or None)
     
    if request.method == "POST" and form.is_valid():
        email = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('shop:profile')
        else:
            form.add_error(None, 'Невірна пошта або пароль.')
    
    return render(request, 'shop/home.html', {'form': form})

def registration(request):
    form = RegistrationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        login(request, user)
        return redirect('shop:profile')
    
    return render(request, 'shop/registration.html', {'form': form})

@login_required(login_url='shop:home')
def profile(request):
    user = request.user
    user_data, created = UserData.objects.get_or_create(user=user)
    
    if request.method == 'POST':
        if 'update' in request.POST:
            edit_account_form = EditProfileForm(request.POST, instance=user)
            edit_phone_form = EditPhoneForm(request.POST, instance=user_data)
            
            if edit_account_form.is_valid() and edit_phone_form.is_valid():
                edit_account_form.save()
                phone = edit_phone_form.cleaned_data.get('telephone')
                user_data.telephone = phone
                user_data.save()
        elif 'delete-acc' in request.POST:
            delete_user_form = UserDeleteForm(request.POST, instance=user)
            if delete_user_form.is_valid():
                if not user.is_superuser and not user.is_staff:
                    user.delete()
                    
        return redirect(f'{request.path}')
    
    edit_account_form = EditProfileForm(instance=user)
    edit_phone_form = EditPhoneForm(instance=user_data)
    delete_user_form = UserDeleteForm(instance=request.user)
    
    return render(request, 'shop/profile.html', {
        'edit_account_form': edit_account_form,
        'edit_phone_form': edit_phone_form,
    })
    
@login_required(login_url='shop:home')
def change_password(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            user = request.user
            if not user.check_password(form.cleaned_data['old_password']):
                form.add_error('old_password', 'Неправильний старий пароль.')
            else:
                user.set_password(form.cleaned_data['new_password1'])
                user.save()
                update_session_auth_hash(request, user)  # prevents logout
                return redirect('shop:profile')
    else:
        form = ChangePasswordForm()
        
    return render(request, 'shop/change_password.html', {'form': form})


def main(request):
    query = request.GET.get('q', '')
    flower_type = request.GET.get('flower_type', '')
    price_order = request.GET.get('price_order', '')
    bouquets = Bouquet.objects.all()
    
    if query:
        bouquets = bouquets.annotate(
            lower_name=Lower('name'),
            lower_composition=Lower('composition')
        ).filter(
            Q(lower_name__contains=query.lower()) |
            Q(lower_composition__contains=query.lower())
        )
    if flower_type:
        bouquets = bouquets.filter(flowers__name=flower_type)
    
    if price_order == 'asc':
        bouquets = bouquets.order_by('price')
    elif price_order == 'desc':
        bouquets = bouquets.order_by('-price')
    
    paginator = Paginator(bouquets, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    flower_types = FlowerType.objects.all()
    
    context = {
        'flower_types': flower_types,
        'bouquets': page_obj
    }
    return render(request, 'shop/main.html', context)

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

def shop_logout(request):
    logout(request)
    return redirect('shop:home')

def sposob_oplaty(request):
    return render(request, 'shop/sposob_oplaty.html')

