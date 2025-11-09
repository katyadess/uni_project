from django.contrib import admin
from .models import *
# Register your models here.

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['bouquet']
    extra = 0
    
    
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id', 
        'user', 
        'user_name', 
        'delivery_method', 
        'payment_method', 
        'date', 
        'time', 
        'created_at',
        'total_cost',
        )
    list_filter = ('delivery_method', 'payment_method', 'created_at')
    search_fields = ('user_name', 'user_tel', 'recipient_name', 'recipient_phone')
    inlines = [OrderItemInline]
    readonly_fields = ('created_at',)
    
    def total_cost(self, obj):
        return f"{obj.get_total_cost():.2f} грн"
    total_cost.short_description = 'Total Cost'

admin.site.register(Order, OrderAdmin)