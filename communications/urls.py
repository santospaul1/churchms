# In communication/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('conversations/', views.conversation_list, name='conversation_list'),
    path('conversations/<int:conversation_id>/', views.conversation_detail, name='conversation_detail'),
    path('conversations/<int:conversation_id>/send/', views.send_message, name='send_message'),
]
