from django.shortcuts import render

def booking(request):
    return render(request, 'booking.html')

def car_detail(request):
    return render(request, 'car_detail.html')

def cars_list(request):
    return render(request, 'cars_list.html')

def contract(request):
    return render(request, 'contract.html')

def owner_dashboard(request):
    return render(request, 'owner_dashboard.html')

def payment(request):
    return render(request, 'payment.html')

def user_profile(request):
    return render(request, 'user_profile.html')