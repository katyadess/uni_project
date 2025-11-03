from django import forms
from .models import *
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class LoginForm(forms.Form):
    username = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'name': 'username',
        }),
        required=True
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'name':'password'
        })
    )
    
class RegistrationForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'name':'password'
        })
    )
    
    class Meta:
        model = CustomUser
        fields = ['first_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'name': 'first_name'}),
            'email': forms.EmailInput(attrs={'name': 'email'}),
        }