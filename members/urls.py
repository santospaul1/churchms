# In members/urls.py
from django.urls import path


from . import views

urlpatterns = [
    path('', views.member_list, name='member_list'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('add_admin/', views.add_admin, name='add_admin'),
    path('manage-admin/', views.manage_admin, name='manage_admin'),
    path('add/', views.add_member, name='add_member'),
    path('member_registration/', views.member_registration, name='member_registration'),
    path('<int:member_id>/', views.member_detail, name='member_detail'),
    path('<int:member_id>/edit/', views.edit_member, name='edit_member'),
    path('<int:member_id>/delete/', views.delete_member, name='delete_member'),

    path('member_login/', views.member_login, name='member_login'),
    path('view_events/', views.view_event, name='view_events'),
    path('view_meeting/', views.view_meeting, name='view_meeting'),
    path('view_location/', views.view_location, name='view_location'),
    path('volunteer_history/', views.volunteer_history, name='volunteer_history'),
    path('view_servics/', views.view_services, name='view_services'),
    path('member_volunteer_detail/<int:volunteer_id>/', views.member_volunteer_detail, name='member_volunteer_detail'),
    path('edit_member_volunteer/<int:volunteer_id>/', views.edit_member_volunteer, name='edit_member_volunteer'),
    path('member_volunteer/', views.member_volunteer, name='member_volunteer'),
    path('delete_member_volunteer/<int:volunteer_id>', views.delete_member_volunteer, name='delete_member_volunteer'),
    path('groups_list', views.groups_list, name='groups_list'),
    path('groups/<int:group_id>/', views.groupdetail, name='groupdetail'),
    path('contact_us', views.contact_us, name='contact_us'),
    
]
