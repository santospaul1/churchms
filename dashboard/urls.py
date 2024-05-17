# In your Django project's urls.py file
from django.urls import path
from .views import CustomLoginView, RegisterView, contact, contact_success, dashboard

urlpatterns = [
    # Other URL patterns...
    path(' ', dashboard, name='dashboard'),
    path('contact/', contact, name='contact' ),
    path('contact_success/', contact_success, name='contact_success'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
]
