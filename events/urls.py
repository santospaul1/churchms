# In events/urls.py
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static


from . import views

urlpatterns = [
    path('events/', views.event_list, name='event_list'),
    path('events/add/', views.add_event, name='add_event'),
    path('events/<int:event_id>/edit/', views.edit_event, name='edit_event'),
    path('events/<int:event_id>/', views.event_detail, name='event_detail'),
    path('events/<int:event_id>/delete/', views.delete_event, name='delete_event'),
    path('services/', views.service_list, name='service_list'),
    path('services/add/', views.add_service, name='add_service'),
    path('services/<int:service_id>/edit/', views.edit_service, name='edit_service'),
    path('services/<int:service_id>/delete/', views.delete_service, name='delete_service'),
	path('services/<int:service_id>/', views.service_detail, name='service_detail'),
    path('meetings/', views.meeting_list, name='meeting_list'),
    path('meetings/add/', views.add_meeting, name='add_meeting'),
    path('meetings/<int:meeting_id>/edit/', views.edit_meeting, name='edit_meeting'),
    path('meetings/<int:meeting_id>/delete/', views.delete_meeting, name='delete_meeting'),
]
if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL,
						document_root=settings.MEDIA_ROOT)
