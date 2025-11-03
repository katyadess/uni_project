from django import forms
from .models import *
from django.contrib.auth import get_user_model, password_validation

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
        
class EditProfileForm(forms.ModelForm):
    email = forms.EmailField(
    widget=forms.EmailInput(attrs={
        'id': 'email', 
        'name': 'email',
    }), 
    required=True
    )
    
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'name': 'first_name',
        }),
        max_length=100, 
        required=True
    )
    
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'name': 'last_name',
        }),
        max_length=100, 
        required=True
    )
    
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email']
    

class EditPhoneForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = ['telephone'] 
        widgets = {
            'telephone': forms.TextInput(attrs= {
                'name': 'phone',
                'type': 'tel',
            })
        }
        
        
class UserDeleteForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = []
        
class ChangePasswordForm(forms.Form):
    
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'name': 'old_password'
        }),
        required=True
    )
    
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'name': 'new_password1'
        }),
        required=True,
        validators=[password_validation.validate_password]
    )
    
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'name': 'new_password2'
        }),
        required=True
    )
    
    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data.get('new_password1')
        p2 = cleaned_data.get('new_password2')
        if p1 and p2 and p1 != p2:
            self.add_error('new_password2', 'Паролі не співпадають.')
        return cleaned_data