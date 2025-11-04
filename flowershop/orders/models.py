from django.db import models
from django.conf import settings
from shop.models import *

class Order(models.Model):
    DELIVERY_METHODS = [
        ('standard', 'Стандартна (~2 години)'),
        ('exact', 'В точний час (+99 грн)'),
        ('express', 'Експрес (~30 хвилин +99 грн)'),
        ('pickup', 'Самовивіз (безкоштовно)'),
    ]
    
    PAYMENT_METHODS = [
        ('card', 'Оплата карткою (Visa/MasterCard)'),
        ('cash', 'Наложений платіж (готівкою або терміналом)'),
        ('applepay', 'Apple Pay'),
        ('googlepay', 'Google Pay'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    user_name = models.CharField(max_length=100)
    user_tel = models.CharField(max_length=20)

    recipient_name = models.CharField(max_length=100, blank=True, null=True)
    recipient_phone = models.CharField(max_length=20, blank=True, null=True)

    add_card = models.BooleanField(default=False)
    card_message = models.TextField(blank=True, null=True)

    delivery_method = models.CharField(max_length=20, choices=DELIVERY_METHODS, default='standard')
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS, default='card')  # 🧠 Додано тут!

    street = models.CharField(max_length=255, blank=True, null=True)
    house = models.CharField(max_length=50, blank=True, null=True)
    apartment = models.CharField(max_length=50, blank=True, null=True)
    unknown_address = models.BooleanField(default=False)

    date = models.CharField(max_length=50, blank=True, null=True)
    time = models.CharField(max_length=50, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Замовлення №{self.id}'

    def get_total_cost(self):
        total = sum(item.get_cost() for item in self.items.all())

        
        if self.delivery_method in ['exact', 'express']:
            total += 99
        
        if self.add_card:
            total += 29

        return total
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    bouquet = models.ForeignKey(Bouquet, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.bouquet.name} x {self.quantity}"

    def get_cost(self):
        return self.price * self.quantity
