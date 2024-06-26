from django.shortcuts import get_object_or_404, render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from dashboard.models import Contact, Location
from django.contrib.auth.decorators import login_required
from events.models import Event, Meeting, Service
from groups.models import SmallGroup
from members.models import Member
from django.shortcuts import render, redirect
from django.utils import timezone
from volunteers.models import Volunteer
from .forms import ContactForm, LocationForm
from django.contrib.auth import logout


def dashboard(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')  # Redirect to a success page
    else:
        form = ContactForm()
    current_date = timezone.now().date()
    services = Service.objects.all()
    events = Event.objects.filter(date__gte=current_date).order_by('date')
    locations = Location.objects.all()
    meetings = Meeting.objects.filter(date__gte=current_date).order_by('date')
    context = {
        'services':services,
        'events':events,
        'locations':locations,
        'meetings':meetings,
        'form':form
    }
    return render(request, 'dashboard.html', context)

@login_required
def admin_dashboard(request):
    member_count = Member.objects.count()
    volunteers_count = Volunteer.objects.count()
    groups_count = SmallGroup.objects.count()
    services_count = Service.objects.count()
    events_count = Event.objects.count()
    location_count = Location.objects.count()
    context = {
        'member_count':member_count,
        'volunteers_count':volunteers_count,
        'groups_count':groups_count,
        'services_count':services_count,
        'events_count':events_count,
        'location_count':location_count,
        



    }
    return render(request, 'admin_dashboard.html', context)

@login_required
def member_dashboard(request):

    current_date = timezone.now().date()
    # Add any logic here to fetch data for the dashboard
    # For example, you can fetch recent events, statistics, etc.
    services = Service.objects.all()
    upcoming_events = Event.objects.filter(date__gte=current_date).order_by('date')
    locations = Location.objects.all()
    upcoming_meetings = Meeting.objects.filter(date__gte=current_date).order_by('date')
    events = Event.objects.all()
    context = {
        'services':services,
        'events':events,
        'locations':locations,
        'upcoming_events': upcoming_events,
        'upcoming_meetings':upcoming_meetings
        
    }
    return render(request, 'member_dashboard.html', context)

@login_required
def user_logout(request):
    logout(request)
    return redirect('dashboard')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')  # Redirect to a success page
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def contact_list(request):
    # Add any logic here to fetch data for the dashboard
    # For example, you can fetch recent events, statistics, etc.
    contacts = Contact.objects.all().order_by('-id')

    context = {
        'contacts':contacts,
    }
    return render(request, 'contact_list.html', context)

def contact_success(request):
    return render(request, 'contact_success.html')
    
def location_list(request):
    locations = Location.objects.all()
    return render(request, 'location_list.html', {'locations': locations})

def add_location(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('location_list')
    else:
        form = LocationForm()
    return render(request, 'add_edit_location.html', {'form': form})

def edit_location(request, location_id):
    location = get_object_or_404(Location, id=location_id)
    if request.method == 'POST':
        form = LocationForm(request.POST, instance=location)
        if form.is_valid():
            form.save()
            return redirect('location_list')
    else:
        form = LocationForm(instance=location)
    return render(request, 'add_edit_location.html', {'form': form})

def delete_location(request, location_id):
    location = get_object_or_404(Location, id=location_id)
    if request.method == 'POST':
        location.delete()
        return redirect('location_list')
    return render(request, 'delete_location.html', {'location': location})