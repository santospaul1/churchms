# In your Django app's forms.py
from django import forms
from .models import SmallGroup, Meeting

class SmallGroupForm(forms.ModelForm):
    class Meta:
        model = SmallGroup
        fields = ['name', 'description']

class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = ['date', 'time', 'location']
