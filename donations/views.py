# In donations/views.py
from django.shortcuts import render, redirect
from .models import Donation, FinancialTransaction
from .forms import DonationForm, FinancialTransactionForm

def donation_list(request):
    donations = Donation.objects.all()
    return render(request, 'donations/donation_list.html', {'donations': donations})

def add_donation(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('donation_list')
    else:
        form = DonationForm()
    return render(request, 'donations/add_edit_donation.html', {'form': form})

def finance_list(request):
    transactions = FinancialTransaction.objects.all()
    return render(request, 'donations/finance_list.html', {'transactions': transactions})

def add_transaction(request):
    if request.method == 'POST':
        form = FinancialTransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('finance_list')
    else:
        form = FinancialTransactionForm()
    return render(request, 'donations/add_edit_transaction.html', {'form': form})
