from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from members.models import Member
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib.auth import authenticate, login
# Create your views here.
def dashboard(request):
    # Add any logic here to fetch data for the dashboard
    # For example, you can fetch recent events, statistics, etc.
    member_count = Member.objects.count()
    context = {
        'member_count':member_count
    }
    return render(request, 'dashboard.html', context)

class CustomLoginView(LoginView):
    template_name = 'login.html' 

    def get_success_url(self):
        # Customize the redirect URL after successful login
        return reverse_lazy('dashboard') 
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')  # Redirect to a success page
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def contact_success(request):
    return render(request, 'contact_success.html')

class RegisterView(FormView):
    template_name = 'register.html'  # Path to your registration template
    form_class = UserCreationForm
    success_url = '/login/'

    def form_valid(self, form):
        # Save the user to the database
        form.save()
        # Optionally, log the user in after registration
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)