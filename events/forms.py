# In events/forms.py
from django import forms
from .models import Event, Meeting, Service, Image

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'date', 'time', 'location']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }
class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'date', 'time', 'location', 'description']

class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = ['name', 'date', 'time', 'location', 'description', 'images']

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image']