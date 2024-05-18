# In volunteers/models.py
from django.db import models

class Volunteer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    skills = models.TextField(blank=True)
    interests = models.TextField(blank=True)
    availability = models.TextField(blank=True)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"



