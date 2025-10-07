from django.shortcuts import render

# for Puplic Pages

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')

def team(request):
    return render(request, 'team.html')

def testimonial(request):
    return render(request, 'testimonial.html')

def contact(request):
    return render(request, 'contact.html')

def login_view(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def logout_view(request):
    pass

####

# Main Functional Views

def profile_view(request):
    pass

def owner_dashboard(request):
    pass

def owner_cars(request, owner_id):
    pass

def cars_list(request):
    pass

def add_car(request):
    pass

def car_detail(request, id):
    pass

def booking_view(request):
    pass

def contract(request):
    pass

def payment(request):
    pass

def search_cars(request):
    pass

def approve_booking(request, booking_id):
    pass

def reject_booking(request, booking_id):
    pass
