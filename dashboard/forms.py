# forms.py
from django import forms
from .models import Contact, Location

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'message']
class MemberContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['message']

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['name', 'address', 'city', 'state', 'zip_code']
        widget = {
            'address': forms.Textarea(attrs={'rows': 2}),
        }