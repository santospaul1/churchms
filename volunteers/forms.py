from django import forms
from .models import Volunteer

class VolunteerForm(forms.ModelForm):
    skills = forms.MultipleChoiceField(choices=Volunteer.SKILL_CHOICES, widget=forms.CheckboxSelectMultiple, required=False)
    interests = forms.MultipleChoiceField(choices=Volunteer.INTEREST_CHOICES, widget=forms.CheckboxSelectMultiple, required=False)
    class Meta:
        model = Volunteer
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'address', 'skills', 'interests', 'availability']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 2}),
            'availability': forms.DateInput(attrs={'type': 'date'}),
        }
    def save(self, commit=True):
        volunteer = super().save(commit=False)
        volunteer.skills = ','.join(self.cleaned_data['skills'])
        volunteer.interests = ','.join(self.cleaned_data['interests'])
        if commit:
            volunteer.save()
        return volunteer
