from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Q
from django.core.mail import send_mail
from django.conf import settings
from .models import Booking, Car

User = get_user_model()
# for Puplic Pages

def index(request):
    owners = User.objects.filter(role="owner", is_approved=True)
    cars = Car.objects.all()
    return render(request, "index.html", {"owners": owners, "cars": cars})

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





# ===========================
# CONTACT FORM
# ===========================
def contact(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        subject = request.POST.get("subject", "").strip()
        message = request.POST.get("message", "").strip()

        if not all([name, email, subject, message]):
            messages.error(request, "❌ Please fill in all fields.")
            return redirect("contact")

        to_email = getattr(settings, "CONTACT_EMAIL", settings.DEFAULT_FROM_EMAIL)
        full_subject = f"[Royal Cars Contact] {subject}"
        full_message = f"From: {name} <{email}>\n\nMessage:\n{message}"

        try:
            send_mail(full_subject, full_message, settings.DEFAULT_FROM_EMAIL, [to_email])
            messages.success(request, "✅ Your message has been sent successfully.")
        except Exception as e:
            messages.error(request, f"❌ Failed to send message: {e}")

        return redirect("contact")

    return render(request, "contact.html", {"CONTACT_EMAIL": getattr(settings, "CONTACT_EMAIL", None)})