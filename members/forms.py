from django import forms
from django.contrib.auth.models import User
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

class MemberRegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Member
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'address']

        widgets = {
            'address': forms.Textarea(attrs={'rows': 2}),
        }

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
            email=self.cleaned_data['email'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name']
        )
        member = super().save(commit=False)
        member.user = user
        member.password = self.cleaned_data['password']
        if commit:
            member.save()
        return member

class AdminLoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


class Volunteer_memberForm(forms.ModelForm):
    skills = forms.MultipleChoiceField(choices=Volunteer.SKILL_CHOICES, widget=forms.CheckboxSelectMultiple, required=False)
    interests = forms.MultipleChoiceField(choices=Volunteer.INTEREST_CHOICES, widget=forms.CheckboxSelectMultiple, required=False)
    class Meta:
        model = Volunteer
        fields = [ 'skills', 'interests', 'availability']
        widgets = {
            'availability': forms.DateInput(attrs={'type': 'date'}),
        }

    def save(self, commit=True):
        Volunteer.volunteer = super().save(commit=False)
        Volunteer.volunteer.skills = ','.join(self.cleaned_data['skills'])
        Volunteer.volunteer.interests = ','.join(self.cleaned_data['interests'])
        if commit:
            Volunteer.volunteer.save()
        return Volunteer.volunteer