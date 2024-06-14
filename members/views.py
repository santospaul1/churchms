from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from dashboard.forms import MemberContactForm
from dashboard.models import Contact, Location
from events.models import Event, Meeting, Service
from groups.models import  SmallGroup
from volunteers.models import Volunteer
from .forms import AdminLoginForm, MemberForm, MemberRegistrationForm, Volunteer_memberForm
from .models import Admin, Member

def admin_login(request):
    if request.method == 'POST':
        form = AdminLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                try:
                    admin = Admin.objects.get(user=user)
                    login(request, user)
                    return redirect('admin_dashboard')  # Redirect to admin dashboard after login
                except Admin.DoesNotExist:
                    form.add_error(None, 'You do not have admin privileges.')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = AdminLoginForm()
    
    return render(request, 'members/admin_login.html', {'form': form})

@login_required
def add_admin(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = request.POST.get('username')

        # Create a new User instance
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        # Create a new Admin instance and associate it with the created user
        admin = Admin.objects.create(
            user=user,
            fullname=fullname,
            email=email,
            username=username
        )

        messages.success(request, 'New admin has been added successfully')
        return redirect('manage_admin')  # Redirect to the same page to show the message

    return render(request, 'admin/add_admin.html')

@login_required
def manage_admin(request):
    if request.method == "GET" and 'del' in request.GET:
        id = request.GET.get('del')
        try:
            admin = Admin.objects.get(id=id)

            admin.delete()
            messages.success(request, "The selected admin account has been deleted")
        except Admin.DoesNotExist:
            messages.error(request, "Admin account not found")

    admins = Admin.objects.all()
    return render(request, 'admin/manage_admin.html', {'admins': admins})

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

def member_registration(request):
    if request.method == 'POST':
        form = MemberRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('member_dashboard')  # Redirect to member dashboard after registration
    else:
        form = MemberRegistrationForm()
    
    return render(request, 'members/member_registration.html', {'form': form})

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
                return redirect('view_services')
            except Member.DoesNotExist:
                messages.error(request, 'You are not authorized to access this area')
        else:
            messages.error(request, 'Invalid username or password')
    
    return render(request, 'members/member_login.html', {'error': error})


    #Functions to dislay What member can view
def view_event(request):
    current_date = timezone.now().date()
    events = Event.objects.filter(date__gte=current_date).order_by('date')
    all_events = Event.objects.all().order_by('-id')    
    return render(request, 'views/event_list.html', {'events': events, 'all_events':all_events})

def view_meeting(request):
    current_date = timezone.now().date()
    events = Meeting.objects.filter(date__gte=current_date).order_by('date')
    all_events = Meeting.objects.all().order_by('-id')    
    return render(request, 'views/event_list.html', {'events': events, 'all_events':all_events})


def view_location(request):
    locations = Location.objects.all().order_by('-id')    
    return render(request, 'views/location_list.html', {'locations': locations})

def view_services(request):
    services = Service.objects.all().order_by('-id')    
    return render(request, 'views/service_list.html', {'services': services})
def groups_list(request):
    groups = SmallGroup.objects.all().order_by('-id')

    return render(request, 'views/group_list.html', {'groups': groups})

@login_required
def volunteer_history(request):
    user = request.user

    try:
        # Retrieve the Member instance associated with the logged-in user
        volunteer = Member.objects.get(user=user)
    except Member.DoesNotExist:
        # Handle the case where the Member instance does not exist
        error = "Member profile not found for the current user."
        

    # Filter volunteer history by the Employee instance
    volunteer_history = Volunteer.objects.filter(volunteer=volunteer).order_by('-id')
    

    context = {
        'volunteer_history': volunteer_history
    }

    return render(request, 'views/volunteer_history.html', context)


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
                volunteer = member,
                skills = skills,
                interests=interests,
                availability = availability

            )
            return redirect('volunteer_history')
        else:
            error = "Form is not valid."
    else:
        form = Volunteer_memberForm()
    return render(request, 'functions/add_edit_volunteer.html', {'form': form, 'error':error, 'msg':msg})

def edit_member_volunteer(request, volunteer_id):
    volunteer = Volunteer.objects.get(id=volunteer_id)
    if request.method == 'POST':
        form = Volunteer_memberForm(request.POST, instance=volunteer)
        if form.is_valid():
            form.save()
            return redirect('volunteer_history')
    else:
        form = Volunteer_memberForm(instance=volunteer)
    return render(request, 'views/add_edit_volunteer.html', {'form': form})


def member_volunteer_detail(request, volunteer_id):
    volunteer = Volunteer.objects.get(id=volunteer_id)
    return render(request, 'views/volunteer_detail.html', {'volunteer': volunteer})

def delete_member_volunteer(request, volunteer_id):
    volunteer = Volunteer.objects.get(id=volunteer_id)
    if request.method == 'POST':
        volunteer.delete()
        return redirect('volunteer_history')
    return render(request, 'views/delete_volunteer.html', {'volunteer': volunteer})


def groupdetail(request, group_id):
    group = SmallGroup.objects.get(pk=group_id)
    
    return render(request, 'views/group_detail.html', {'group': group,})


def contact_us(request):
    error = None
    msg = None
    if request.method == 'POST':
        form = MemberContactForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            
            try:
                member = Member.objects.get(user=request.user)
            except Member.DoesNotExist:
                error = "Member profile not found for the current user."
                return render(request, 'views/contact.html', {'form': form, 'error':error})
            
            Contact.objects.create(
                sender=member,
                message= message
            )
            msg = "Form submitted successfully."
            return redirect('contact_success')  # Redirect to a success page
        else:
            error = "Form is not valid."
    else:
        form = MemberContactForm()
    return render(request, 'views/contact.html', {'form': form, 'msg':msg, 'error':error})

