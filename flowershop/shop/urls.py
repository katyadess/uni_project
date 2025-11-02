from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('main/', views.main, name='main'),
    path('registration/', views.registration, name='registration'),
    path('about_us/', views.about_us, name='about_us'),
    path('delivery/', views.delivery, name='delivery'),
    path('payment/', views.payment, name='payment'),
    path('flower/', views.flower_detail, name='flower_detail'),
]
