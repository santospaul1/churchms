# In donations/forms.py
from django import forms
from .models import Donation, FinancialTransaction

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['amount', 'donor_name']
        # Add more fields as needed

class FinancialTransactionForm(forms.ModelForm):
    class Meta:
        model = FinancialTransaction
        fields = ['amount', 'description']
        # Add more fields as needed
