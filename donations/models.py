# In donations/models.py
from django.db import models

class Donation(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    donor_name = models.CharField(max_length=255)
    donation_date = models.DateField(auto_now_add=True)
    # Add more fields as needed

class FinancialTransaction(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateField(auto_now_add=True)
    description = models.TextField()
    # Add more fields as needed
