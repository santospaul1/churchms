# In volunteers/views.py
from django.shortcuts import render, redirect
from .models import Volunteer
from .forms import VolunteerForm

def volunteer_list(request):
    volunteers = Volunteer.objects.all().order_by('-id')

    return render(request, 'volunteers/volunteer_list.html', {'volunteers': volunteers})

def add_volunteer(request):
    if request.method == 'POST':
        form = VolunteerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('volunteer_list')
    else:
        form = VolunteerForm()
    return render(request, 'volunteers/add_edit_volunteer.html', {'form': form})

def edit_volunteer(request, volunteer_id):
    volunteer = Volunteer.objects.get(id=volunteer_id)
    if request.method == 'POST':
        form = VolunteerForm(request.POST, instance=volunteer)
        if form.is_valid():
            form.save()
            return redirect('volunteer_list')
    else:
        form = VolunteerForm(instance=volunteer)
    return render(request, 'volunteers/add_edit_volunteer.html', {'form': form})

def volunteer_detail(request, volunteer_id):
    volunteer = Volunteer.objects.get(id=volunteer_id)
    return render(request, 'volunteers/volunteer_detail.html', {'volunteer': volunteer})

def delete_volunteer(request, volunteer_id):
    volunteer = Volunteer.objects.get(id=volunteer_id)
    if request.method == 'POST':
        volunteer.delete()
        return redirect('volunteer_list')
    return render(request, 'volunteers/delete_volunteer.html', {'volunteer': volunteer})
