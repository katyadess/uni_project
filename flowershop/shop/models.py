from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.
class FlowerType(models.Model):
    name = models.CharField(max_length=50, unique=True)
 
    def __str__(self):
        return self.name
    
class Bouquet(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва букета")
    flowers = models.ManyToManyField(FlowerType, related_name="bouquets", verbose_name="Квіти у складі")
    composition = models.TextField(verbose_name="Склад")
    description = models.TextField(verbose_name="Опис")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Ціна")
    new_price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, verbose_name="Нова ціна")
    image = models.ImageField(upload_to="bouquets/", verbose_name="Зображення")

    def __str__(self):
            return self.name
    
    def get_absolute_url(self):
        return reverse('shop:pro_tovar', args=[str(self.id)])
    
    def discount(self):
        if self.new_price:
            return round((self.price - self.new_price) / self.price * 100)
        return None
        
class BouquetReview(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bouquet = models.ForeignKey(Bouquet, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField(verbose_name='Відгук')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Відгук"
        verbose_name_plural = "Відгуки"
        
    def __str__(self):
        return f"Відгук від {self.user.email} на {self.bouquet.name}"
    

class UserData(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    telephone = models.CharField(max_length=20)
    
    class Meta:
        verbose_name = 'UserData'
        verbose_name_plural = 'UserData'
        
    def __str__(self) -> str:
        return self.user.email 
    

