from django.contrib import admin
from .models import  Car, Booking, User

admin.site.register(User)
admin.site.register(Car)
admin.site.register(Booking)