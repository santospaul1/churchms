# In events/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('add/', views.add_event, name='add_event'),
    path('<int:event_id>/', views.event_detail, name='event_detail'),
    path('<int:event_id>/edit/', views.edit_event, name='edit_event'),
    path('<int:event_id>/delete/', views.delete_event, name='delete_event'),
    path('services/', views.service_list, name='service_list'),
    path('services/add/', views.add_service, name='add_service'),
    path('meetings/', views.meeting_list, name='meeting_list'),
    path('meetings/add/', views.add_meeting, name='add_meeting'),
]
