from django.urls import path
from . import views

app_name = 'core_app'

urlpatterns = [
    path('booking/', views.booking, name='booking'),
    path('car/<int:id>/', views.car_detail, name='car_detail'), 
    path('cars/', views.cars_list, name='cars_list'),
    path('contract/', views.contract, name='contract'),
    path('owner/dashboard/', views.owner_dashboard, name='owner_dashboard'),
    path('payment/', views.payment, name='payment'),
    path('profile/', views.user_profile, name='user_profile'),
]