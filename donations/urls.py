# donations/urls.py
from django.urls import path
from .views import add_spending, make_donation, donation_success, admin_view_donations

urlpatterns = [
    path('make_donation/', make_donation, name='make_donation'),
    path('donation_success/', donation_success, name='donation_success'),
    path('admin_view_donations/', admin_view_donations, name='admin_view_donations'),
    path('admin/add_spending/', add_spending, name='add_spending'),
]

