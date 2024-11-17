from datetime import datetime

from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    birthday = models.DateField(null=True, blank=True)  # Stocke le timestamp
    first_name = models.CharField(max_length=50, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    alias=models.CharField(max_length=50, blank=True, null=True)

    def format_birthday(self):
        """Convert timestamp to a datetime object."""
        if self.birthday:
            return datetime.fromtimestamp(self.birthday/1000 ).strftime('%Y-%m-%d')
        return None

    def __str__(self):
        return f"Profile de {self.user.username}"
