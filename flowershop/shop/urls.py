from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('main/', views.main, name='main'),
    path('registration/', views.registration, name='registration'),
    path('flower/', views.flower_detail, name='flower_detail'),
]
