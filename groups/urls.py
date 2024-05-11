# In your Django app's urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('groups/', views.group_list, name='group_list'),
    path('groups/add/', views.add_group, name='add_group'),
    path('groups/<int:group_id>/', views.group_detail, name='group_detail'),
    path('groups/<int:group_id>/meetings/add/', views.add_meeting, name='add_meeting'),
]
