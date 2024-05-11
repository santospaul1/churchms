# In volunteers/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.volunteer_list, name='volunteer_list'),
    path('add/', views.add_volunteer, name='add_volunteer'),
    path('<int:volunteer_id>/', views.volunteer_detail, name='volunteer_detail'),
    path('<int:volunteer_id>/edit/', views.edit_volunteer, name='edit_volunteer'),
    path('<int:volunteer_id>/delete/', views.delete_volunteer, name='delete_volunteer'),
]
