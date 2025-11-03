from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(FlowerType)
admin.site.register(Bouquet)
admin.site.register(BouquetReview)
admin.site.register(UserData)

