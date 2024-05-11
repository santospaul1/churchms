# In management/views.py
from django.shortcuts import render, redirect
from .models import Facility, Resource, Booking
from .forms import FacilityForm, ResourceForm, BookingForm

def facility_list(request):
    facilities = Facility.objects.all()
    return render(request, 'management/facility_list.html', {'facilities': facilities})

def add_facility(request):
    if request.method == 'POST':
        form = FacilityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('facility_list')
    else:
        form = FacilityForm()
    return render(request, 'management/add_edit_facility.html', {'form': form})

# Similarly, implement views for resource management and booking management
