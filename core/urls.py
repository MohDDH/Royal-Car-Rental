from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='index'),             
    path('about/', views.about, name='about'),     
    path('service/', views.service, name="service"),
    path('team/', views.team, name="team"),
     path('testimonial/', views.testimonial, name="testimonial"),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login_view, name='login'), 
    path('register/', views.register, name='register'), 
    path('logout/', views.logout_view, name="logout"),
    ##
    path('profile/', views.profile_view, name="profile"),
    path('owner/dashboard/', views.owner_dashboard, name='owner_dashboard'),
    path('owner/<int:owner_id>/cars/', views.owner_cars, name="owner_cars"),
    path('cars/', views.cars_list, name='cars_list'),
    path('owner/add-car/', views.add_car, name="add_car"),
    path('car/<int:id>/', views.car_detail, name='car_detail'), 
    path('booking/', views.booking_view, name='booking'),
    path('contract/', views.contract, name='contract'),
    path('payment/', views.payment, name='payment'),
    path('search/', views.search_cars, name="search_cars"),
]