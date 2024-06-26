# In your Django project's urls.py file
from django import views
from django.urls import path
from .views import add_location, admin_dashboard, contact, contact_list, contact_success, dashboard, delete_location, edit_location, location_list, member_dashboard, user_logout

urlpatterns = [
    # Other URL patterns...
    path(' ', dashboard, name='dashboard'),
    path('contact/', contact, name='contact' ),
    path('contact_success/', contact_success, name='contact_success'),
    path('locations/', location_list, name='location_list'),
    path('locations/add/', add_location, name='add_location'),
    path('locations/<int:location_id>/edit/', edit_location, name='edit_location'),
    path('locations/<int:location_id>/delete/', delete_location, name='delete_location'),
    path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),
    path('member_dashboard/', member_dashboard, name='member_dashboard'),
    path('user_logout', user_logout, name='user_logout'),
    path('contact_list', contact_list, name='contact_list'),
]
