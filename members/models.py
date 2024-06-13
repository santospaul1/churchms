from django.db import models
from django.contrib.auth.models import User

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20, default=None)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    date_joined = models.DateField(auto_now_add=True)

    def delete(self, *args, **kwargs):
        # Delete the associated user
        self.user.delete()
        super().delete(*args, **kwargs)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    fullname = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=100, unique=True)
    CreationDate = models.DateField(auto_now_add=True)

    def delete(self, *args, **kwargs):
        # Delete the associated user
        self.user.delete()
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.username
