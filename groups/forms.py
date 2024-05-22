# In your Django app's forms.py
from django import forms
from .models import GroupMember, SmallGroup, Meeting

class SmallGroupForm(forms.ModelForm):
    class Meta:
        model = SmallGroup
        fields = ['name', 'description']

class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = ['date', 'time', 'location']

class GroupMemberForm(forms.ModelForm):
    class Meta:
        model = GroupMember
        fields = ['member']