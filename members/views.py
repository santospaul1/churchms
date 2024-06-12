from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.db.models import Q

from dashboard.models import Location
from events.models import Event, Service
from volunteers.forms import VolunteerForm
from volunteers.models import Volunteer


from .forms import MemberForm, Volunteer_memberForm
from .models import Member

def member_list(request):
    members = Member.objects.all()
    return render(request, 'members/member_list.html', {'members': members})

def add_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username = form.cleaned_data['email'],
                email = form.cleaned_data['email'],
                password=form.cleaned_data['password'],

            )
            member = form.save(commit=False)
            member.user = user
            member.save()
            return redirect('member_list')
    else:
        form = MemberForm()
    return render(request, 'members/add_edit_member.html', {'form': form})

def member_detail(request, member_id):
    member = get_object_or_404(Member, pk=member_id)
    return render(request, 'members/member_detail.html', {'member': member})

def edit_member(request, member_id):
    member = get_object_or_404(Member, pk=member_id)
    if request.method == 'POST':
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('member_detail', member_id=member_id)
    else:
        form = MemberForm(instance=member)
    return render(request, 'members/add_edit_member.html', {'form': form, 'member': member})


def delete_member(request, member_id):
    member = get_object_or_404(Member, pk=member_id)
    if request.method == 'POST':
        member.delete()
        return redirect('member_list')
    return render(request, 'members/delete_member.html', {'member': member})

def member_login(request):
    error = None

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Try to authenticate using username or email as the username
        user = authenticate(
            request,
            username=username,
            password=password,
        )

        if user is not None:
            try:
                admin_user = Member.objects.get(user=user)
                login(request, user)
                return redirect('member_dashboard')
            except Member.DoesNotExist:
                messages.error(request, 'You are not authorized to access this area')
        else:
            messages.error(request, 'Invalid username or password')
    
    return render(request, 'members/member_login.html', {'error': error})


    #Functions to dislay What member can view
def view_event(request):
    events = Event.objects.all().order_by('-id')    
    return render(request, 'views/event_list.html', {'events': events})

def view_location(request):
    locations = Location.objects.all().order_by('-id')    
    return render(request, 'views/location_list.html', {'locations': locations})

def view_services(request):
    services = Service.objects.all().order_by('-id')    
    return render(request, 'views/service_list.html', {'services': services})

#Member Functions
def member_volunteer(request):
    error = None
    msg = None
    if request.method == 'POST':
        form = Volunteer_memberForm(request.POST)
        if form.is_valid():
            skills = form.cleaned_data['skills']
            interests = form.cleaned_data['interests']
            availability = form.cleaned_data['availability']

            try:
                member = Member.objects.get(user=request.user)
            except Member.DoesNotExist:
                error = "Member profile not found for the current user."
                return render(request, 'functions/add_edit_volunteer.html', {'form': form, 'error':error})
            Volunteer.objects.create(
                Volunteer = member,
                skills = skills,
                interests=interests,
                availability = availability

            )
            msg = "Leave application submitted successfully."
        else:
            error = "Form is not valid."
    else:
        form = Volunteer_memberForm()
    return render(request, 'functions/add_edit_volunteer.html', {'form': form, 'error':error, 'msg':msg})
