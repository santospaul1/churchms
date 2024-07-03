# donations/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Donation, Spending
from .forms import DonationForm, SpendingForm
from django.db.models import Sum

@login_required
def make_donation(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            donation = form.save(commit=False)
            donation.member = request.user.member
            donation.save()
            return redirect('donation_success')
    else:
        form = DonationForm()
    return render(request, 'donations/make_donation.html', {'form': form})

@login_required
def donation_success(request):
    return render(request, 'donations/donation_success.html')

@login_required
def admin_view_donations(request):
    if not request.user.is_staff:
        return redirect('home')
    donations = Donation.objects.all()
    spendings = Spending.objects.all()
    total_donations = donations.aggregate(Sum('amount'))['amount__sum'] or 0
    total_spent = spendings.aggregate(Sum('amount'))['amount__sum'] or 0
    remaining_balance = total_donations - total_spent
    return render(request, 'donations/admin_view_donations.html', {
        'donations': donations,
        'spendings': spendings,
        'total_donations': total_donations,
        'total_spent': total_spent,
        'remaining_balance': remaining_balance
    })

@login_required
def add_spending(request):
    if not request.user.is_staff:
        return redirect('home')
    if request.method == 'POST':
        form = SpendingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_view_donations')
    else:
        form = SpendingForm()
    return render(request, 'donations/add_spending.html', {'form': form})
