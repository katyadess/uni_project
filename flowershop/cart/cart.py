from decimal import Decimal
from django.conf import settings
from shop.models import Bouquet


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
        
    def add(self, bouquet, quantity=1, update_quantity=False):
        bouquet_id = str(bouquet.id)
        current_price = str(bouquet.new_price) if bouquet.new_price else str(bouquet.price)
        if bouquet_id not in self.cart:
            self.cart[bouquet_id] = {'quantity': 0, 'price': str(current_price)}
        
        if update_quantity:
            self.cart[bouquet_id]['quantity'] = quantity
        else:
            self.cart[bouquet_id]['quantity'] += quantity       
        self.save()
        
    def save(self):
        
        for item in self.cart.values():
            item['price'] = str(item['price'])
        
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True
        
    def remove(self, bouquet):
        bouquet_id = str(bouquet.id)
        if bouquet_id in self.cart:
            del self.cart[bouquet_id]
            self.save()
            
    def __iter__(self):
        bouquet_ids = self.cart.keys()
        bouquets = Bouquet.objects.filter(id__in=bouquet_ids)
        for bouquet in bouquets:
            
            self.cart[str(bouquet.id)]['bouquet'] = bouquet
            self.cart[str(bouquet.id)]['price'] = str(bouquet.new_price) if bouquet.new_price else str(bouquet.price)
    
            
        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item
    
    def __contains__(self, bouquet):
        
        return str(bouquet.id) in self.cart
    
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
    
    def get_total_quantity(self, bouquet_id):
        return self.cart.get(bouquet_id, {}).get('quantity', 0)

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
    
    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True