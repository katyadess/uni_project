from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.home, name='home'),
    path('registration/', views.registration, name='registration'),
    path('logout/', views.shop_logout, name='shop_logout'),
    path('profile/', views.profile, name='profile'),
    path('change_password/', views.change_password, name='change_password'),
    path('main/', views.main, name='main'),
    path('about_us/', views.about_us, name='about_us'),
    path('delivery/', views.delivery, name='delivery'),
    path('payment/', views.payment, name='payment'),
    path('pro_tovar/<int:id>/', views.pro_tovar, name='pro_tovar'),
    path('sposob_oplaty/<int:order_id>', views.sposob_oplaty, name='sposob_oplaty'),
    path('oplata/<int:order_id>', views.oplata, name='oplata'),
]