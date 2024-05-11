"""
URL configuration for churchms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from donations.views import donation_list
from events.views import event_list
from members.views import member_detail, member_list
from volunteers.views import volunteer_list

urlpatterns = [
path('', member_list, name='member_list'),
path('events/', event_list, name='event_list'),
path('volunteers/', volunteer_list, name='volunteer_list'),
path('donations/', donation_list, name='donation_list'),

    
    path('admin/', admin.site.urls),

    path('', include('members.urls')),
    path('events/', include('events.urls')),
    path('volunteers/', include('volunteers.urls')),
    path('donations/', include('donations.urls')),

    
]