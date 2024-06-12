# In members/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.member_list, name='member_list'),
    path('add/', views.add_member, name='add_member'),
    path('<int:member_id>/', views.member_detail, name='member_detail'),
    path('<int:member_id>/edit/', views.edit_member, name='edit_member'),
    path('<int:member_id>/delete/', views.delete_member, name='delete_member'),

    path('member_login/', views.member_login, name='member_login'),
    path('view_events/', views.view_event, name='view_events'),
    path('view_location/', views.view_location, name='view_location'),
    path('view_servics/', views.view_services, name='view_services'),
    path('member_volunteer/', views.member_volunteer, name='member_volunteer')
]
