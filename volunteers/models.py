from django.db import models
from members.models import Member

class Volunteer(models.Model):
    SKILL_CHOICES = [
        ('teaching', 'Teaching'),
        ('cooking', 'Cooking'),
        ('driving', 'Driving'),
        ('cleaning', 'Cleaning'),
        # Add more skills as needed
    ]

    INTEREST_CHOICES = SKILL_CHOICES  # Assuming interests are the same as skills. Adjust as needed.
    volunteer = models.ForeignKey(Member, on_delete=models.CASCADE, default=None, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=False)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True, max_length=20)
    skills = models.CharField(max_length=255, blank=True)
    interests = models.CharField(max_length=255, blank=True)
    availability = models.DateField(blank=True, null=True)

    def get_skills_display(self):
        return ', '.join(self.skills.split(','))

    def get_interests_display(self):
        return ', '.join(self.interests.split(','))
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
