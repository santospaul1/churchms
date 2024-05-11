# In management/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('facilities/', views.facility_list, name='facility_list'),
    path('facilities/add/', views.add_facility, name='add_facility'),
    # Define URLs for resource management and booking management
]
