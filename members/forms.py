# In members/forms.py
from django import forms

from volunteers.models import Volunteer
from .models import Member

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['first_name', 'last_name', 'email','password', 'phone_number', 'address']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3}),
             'password': forms.PasswordInput()
        }

class Volunteer_memberForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = [ 'skills', 'interests', 'availability']
        widgets = {
            'skills': forms.CheckboxSelectMultiple,
            'interests': forms.CheckboxSelectMultiple,
            'availability': forms.DateInput(attrs={'type': 'date'}),
        }

