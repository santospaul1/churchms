from django.shortcuts import get_object_or_404, redirect, render

from .forms import EventForm, MeetingForm, ServiceForm
from .models import Event, Meeting, Service
# Create your views here.
def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'events/add_edit_event.html', {'form': form})

def edit_event(request, event_id):
    event = Event.objects.get(id=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm(instance=event)
    return render(request, 'events/add_edit_event.html', {'form': form})

def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'events/event_detail.html', {'event': event})

def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        event.delete()
        return redirect('event_list')
    return render(request, 'events/delete_event.html', {'event': event})

def service_list(request):
    services = Service.objects.all()
    return render(request, 'events/service_list.html', {'services': services})

def add_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('service_list')
    else:
        form = ServiceForm()
    return render(request, 'events/add_edit_service.html', {'form': form})

def meeting_list(request):
    meetings = Meeting.objects.all()
    return render(request, 'events/meeting_list.html', {'meetings': meetings})

def add_meeting(request):
    if request.method == 'POST':
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('meeting_list')
    else:
        form = MeetingForm()
    return render(request, 'events/add_edit_meeting.html', {'form': form})