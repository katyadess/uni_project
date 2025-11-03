from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('registration/', views.registration, name='registration'),
    path('main/', views.main, name='main'),
    path('about_us/', views.about_us, name='about_us'),
    path('delivery/', views.delivery, name='delivery'),
    path('payment/', views.payment, name='payment'),
    path('pro_tovar/', views.pro_tovar, name='pro_tovar'),
    path('oplata/', views.oplata, name='oplata'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.shop_logout, name='shop_logout'),
    path('sposob_oplaty/', views.sposob_oplaty, name='sposob_oplaty'),
]
