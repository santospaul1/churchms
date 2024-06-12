from django import forms
from .models import Volunteer

class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'address', 'skills', 'interests', 'availability']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 2}),
            'skills': forms.CheckboxSelectMultiple,
            'interests': forms.CheckboxSelectMultiple,
            'availability': forms.DateInput(attrs={'type': 'date'}),
        }
