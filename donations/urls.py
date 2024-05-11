# In donations/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('donations/', views.donation_list, name='donation_list'),
    path('donations/add/', views.add_donation, name='add_donation'),
    path('finance/', views.finance_list, name='finance_list'),
    path('finance/add/', views.add_transaction, name='add_transaction'),
]
