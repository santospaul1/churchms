# donations/forms.py
from django import forms
from .models import Donation, Spending

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        
        fields = ['amount', 'description']
        
class SpendingForm(forms.ModelForm):
    class Meta:
        model = Spending
        fields = ['amount', 'description']