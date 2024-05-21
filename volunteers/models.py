from django.db import models
from multiselectfield import MultiSelectField

class Volunteer(models.Model):
    SKILL_CHOICES = [
        ('teaching', 'Teaching'),
        ('cooking', 'Cooking'),
        ('driving', 'Driving'),
        ('cleaning', 'Cleaning'),
        # Add more skills as needed
    ]

    INTEREST_CHOICES = SKILL_CHOICES  # Assuming interests are the same as skills. Adjust as needed.

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    skills = MultiSelectField(choices=SKILL_CHOICES, blank=True, max_choices=10, max_length=100)
    interests = MultiSelectField(choices=INTEREST_CHOICES, blank=True, max_choices=10, max_length=100)
    availability = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
