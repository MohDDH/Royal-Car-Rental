from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.conf import settings

# User Class
class User(AbstractUser):
    class Roles(models.TextChoices):
        USER = "user", "User"
        OWNER = "owner", "Owner"
        ADMIN = "admin", "Admin"

    role = models.CharField(max_length=20, choices=Roles.choices, default=Roles.USER)
    phone = models.CharField(max_length=32, blank=True)
    company_name = models.CharField(max_length=160, blank=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"

    @property
    def is_owner(self):
        return self.role == self.Roles.OWNER

    @property
    def is_admin(self):
        return self.role == self.Roles.ADMIN


# Car Class
class Car(models.Model):
    TRANSMISSION_CHOICES = [
        ("AUTO", "Automatic"),
        ("MANUAL", "Manual"),
    ]

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="cars",
        limit_choices_to={"role": "owner"},
        null=True,
        blank=True,
    )
    name = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    transmission = models.CharField(max_length=20, choices=TRANSMISSION_CHOICES)
    mileage = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="cars/", blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.year})"

    class Meta:
        ordering = ["-year", "name"]


# Booking Class
class Booking(models.Model):
    STATUS_PENDING = "pending"
    STATUS_APPROVED = "approved"
    STATUS_REJECTED = "rejected"

    STATUS_CHOICES = [
        (STATUS_PENDING, "Pending"),
        (STATUS_APPROVED, "Approved"),
        (STATUS_REJECTED, "Rejected"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="bookings",
        null=True,
        blank=True,
    )
    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
        related_name="bookings",
        null=True,
        blank=True,
    )
    pickup_location = models.CharField(max_length=200)
    drop_location = models.CharField(max_length=200)
    pickup_date = models.DateField()
    pickup_time = models.TimeField()
    special_request = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_PENDING)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Booking #{self.pk} - {self.user} → {self.car}"

    class Meta:
        ordering = ["-created_at"]

