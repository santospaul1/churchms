from django.shortcuts import get_object_or_404, redirect, render
from .forms import EventForm, ImageForm, MeetingForm, ServiceForm
from .models import Event, Meeting, Service

# Create your views here.
def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

def add_event(request):
    if request.method == 'POST':
        event_form = EventForm(request.POST)
        image_form = ImageForm(request.POST, request.FILES)  # Include request.FILES for file uploads
        if event_form.is_valid() and image_form.is_valid():
            event = event_form.save()
            image = image_form.save(commit=False)
            image.save()
            event.images.add(image)
            return redirect('event_list')
    else:
        event_form = EventForm()
        image_form = ImageForm() 
    return render(request, 'events/add_edit_event.html', {'event_form': event_form, 'image_form': image_form})

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

def edit_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('service_list')
    else:
        form = ServiceForm(instance=service)
    return render(request, 'events/add_edit_service.html', {'form': form})

def delete_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    if request.method == 'POST':
        service.delete()
        return redirect('service_list')
    return render(request, 'events/delete_service.html', {'service': service})

def meeting_list(request):
    if request.method == 'GET':
        meetings = Meeting.objects.all()
        return render(request, 'events/meeting_list.html', {'meetings': meetings})

def add_meeting(request):
    if request.method == 'POST':
        form = MeetingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('meeting_list')
    else:
        form = MeetingForm()
    return render(request, 'events/add_edit_meeting.html', {'form': form})

def edit_meeting(request, meeting_id):
    meeting = get_object_or_404(Meeting, id=meeting_id)
    if request.method == 'POST':
        form = MeetingForm(request.POST, instance=meeting)
        if form.is_valid():
            form.save()
            return redirect('meeting_list')
    else:
        form = MeetingForm(instance=meeting)
    return render(request, 'events/add_edit_meeting.html', {'form': form})

def delete_meeting(request, meeting_id):
    meeting = get_object_or_404(Meeting, id=meeting_id)
    if request.method == 'POST':
        meeting.delete()
        return redirect('meeting_list')
    return render(request, 'events/delete_meeting.html', {'meeting': meeting})
