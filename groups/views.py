from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Group
from django.contrib.auth import get_user_model
from django.contrib import messages

User = get_user_model()


@login_required
def dashboard(request):
    user = request.user
    leading_groups = user.leading_groups.all()  # where user is leader
    member_groups = user.joined_groups.exclude(leader=user)  # where user is just a member

    return render(request, 'groups/dashboard.html', {
        'leading_groups': leading_groups,
        'member_groups': member_groups
    })


@login_required
def create_group(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            group = Group.objects.create(name=name, leader=request.user)
            group.members.add(request.user)
            messages.success(request, "Group created successfully.")
            return redirect('group_detail', group_id=group.id)
    return render(request, 'groups/create_group.html')


@login_required
def group_detail(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    is_leader = request.user == group.leader
    return render(request, 'groups/group_detail.html', {
        'group': group,
        'is_leader': is_leader,
        'members': group.members.all()
    })


@login_required
def add_member(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    if request.user != group.leader:
        messages.error(request, "Only the leader can add members.")
        return redirect('group_detail', group_id=group.id)

    if request.method == 'POST':
        username = request.POST.get('username')
        try:
            user = User.objects.get(username=username)
            group.members.add(user)
            messages.success(request, f"{username} added to group.")
        except User.DoesNotExist:
            messages.error(request, "User not found.")
        return redirect('group_detail', group_id=group.id)

    return render(request, 'groups/add_member.html', {'group': group})


@login_required
def transfer_leadership(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    if request.user != group.leader:
        messages.error(request, "Only the leader can transfer leadership.")
        return redirect('group_detail', group_id=group.id)

    if request.method == 'POST':
        new_leader_id = request.POST.get('new_leader')
        new_leader = get_object_or_404(User, id=new_leader_id)
        group.leader = new_leader
        group.save()
        messages.success(request, "Leadership transferred.")
        return redirect('group_detail', group_id=group.id)

    members = group.members.exclude(id=request.user.id)
    return render(request, 'groups/transfer_leader.html', {
        'group': group,
        'members': members
    })


@login_required
def leave_group(request, group_id):
    group = get_object_or_404(Group, id=group_id)

    if request.user == group.leader:
        messages.error(request, "Transfer leadership before leaving.")
        return redirect('transfer_leadership', group_id=group.id)

    group.members.remove(request.user)
    messages.success(request, "You left the group.")
    return redirect('dashboard')
