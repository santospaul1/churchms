# In management/forms.py
from django import forms
from .models import Facility, Resource, Booking

class FacilityForm(forms.ModelForm):
    class Meta:
        model = Facility
        fields = ['name', 'description']

class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['name', 'description']

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['facility', 'resource', 'date', 'start_time', 'end_time']
