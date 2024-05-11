from django.shortcuts import get_object_or_404, redirect, render
# In members/views.py
from django.shortcuts import render

from .forms import MemberForm
from .models import Member

def member_list(request):
    members = Member.objects.all()
    return render(request, 'members/member_list.html', {'members': members})

def add_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('member_list')
    else:
        form = MemberForm()
    return render(request, 'members/add_edit_member.html', {'form': form})

def member_detail(request, member_id):
    member = get_object_or_404(Member, pk=member_id)
    return render(request, 'members/member_detail.html', {'member': member})

def edit_member(request, member_id):
    member = get_object_or_404(Member, pk=member_id)
    if request.method == 'POST':
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('member_detail', member_id=member_id)
    else:
        form = MemberForm(instance=member)
    return render(request, 'members/add_edit_member.html', {'form': form, 'member': member})

def delete_member(request, member_id):
    member = get_object_or_404(Member, pk=member_id)
    if request.method == 'POST':
        member.delete()
        return redirect('member_list')
    return render(request, 'members/delete_member.html', {'member': member})