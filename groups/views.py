# In your Django app's views.py
from django.shortcuts import get_object_or_404, render, redirect
from .models import SmallGroup, GroupMember, Meeting
from .forms import GroupMemberForm, SmallGroupForm, MeetingForm
from django.contrib.auth.models import User

def add_group_member(request, group_id):
    group = get_object_or_404(SmallGroup, id=group_id)
    if request.method == 'POST':
        form = GroupMemberForm(request.POST)
        if form.is_valid():
            group_member = form.save(commit=False)
            group_member.group = group
            group_member.save()
            return redirect('group_detail', group_id=group.id)
    else:
        form = GroupMemberForm()
    return render(request, 'groups/add_group_member.html', {'form': form, 'group': group})

def remove_group_member(request, group_id, member_id):
    group = get_object_or_404(SmallGroup, id=group_id)
    member = get_object_or_404(User, id=member_id)
    GroupMember.objects.filter(group=group, member=member).delete()
    return redirect('group_detail', group_id=group.id)

def group_list(request):
    groups = SmallGroup.objects.all().order_by('-id')

    return render(request, 'groups/group_list.html', {'groups': groups})

def add_group(request):
    if request.method == 'POST':
        form = SmallGroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('group_list')
    else:
        form = SmallGroupForm()
    return render(request, 'groups/add_edit_group.html', {'form': form})

def add_meeting(request, group_id):
    group = SmallGroup.objects.get(pk=group_id)
    if request.method == 'POST':
        form = MeetingForm(request.POST)
        if form.is_valid():
            meeting = form.save(commit=False)
            meeting.group = group
            meeting.save()
            return redirect('group_detail', group_id=group_id)
    else:
        form = MeetingForm()
    return render(request, 'groups/add_meeting.html', {'form': form, 'group': group})

def group_detail(request, group_id):
    group = SmallGroup.objects.get(pk=group_id)
    meeting = Meeting.objects.all()

    return render(request, 'groups/group_detail.html', {'group': group, 'meeting':meeting})