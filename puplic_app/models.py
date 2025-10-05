from django.db import models

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # لاحقًا نضيف تشفير
    phone = models.CharField(max_length=20, blank=True, null=True)
    role = models.CharField(
        max_length=20,
        choices=[('owner', 'Owner'), ('renter', 'Renter')],
        default='renter'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username