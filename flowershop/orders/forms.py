from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'user_name', 'user_tel',
            'recipient_name', 'recipient_phone',
            'add_card', 'card_message',
            'delivery_method', 'street', 'house', 'apartment', 'unknown_address',
            'date', 'time',
        ]
        
        widgets = {
            'user_name': forms.TextInput(),
            'user_tel': forms.TextInput(),

            'recipient_name': forms.TextInput(attrs={'placeholder': "Ім'я"}),
            'recipient_phone': forms.TextInput(attrs={'placeholder': "Телефон"}),

            'add_card': forms.CheckboxInput(attrs={'id': 'card'}),
            'card_message': forms.Textarea(attrs={'placeholder': "Введіть текст листівки..."}),

            'delivery_method': forms.Select(),
            'street': forms.TextInput(attrs={'placeholder': "Вулиця"}),
            'house': forms.TextInput(attrs={'placeholder': "Будинок"}),
            'apartment': forms.TextInput(attrs={'placeholder': "Квартира/Офіс"}),
            'date': forms.DateInput(attrs={'placeholder': "Дата", 'type': 'date'}),
            'time': forms.TimeInput(attrs={'placeholder': "Період",  'type': 'time'}),
        }