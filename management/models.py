# In management/models.py
from django.db import models

class Facility(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Resource(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Booking(models.Model):
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    # Add more fields as needed
