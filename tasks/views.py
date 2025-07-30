from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from .models import Task
from groups.models import Group
from .forms import TaskForm

@login_required
def create_task(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    if request.user != group.leader:
        return HttpResponseForbidden("Only the group leader can create tasks.")

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.group = group
            task.created_by = request.user
            task.save()
            return redirect("group_detail", group_id=group.id)
    else:
        form = TaskForm()

    return render(request, "tasks/create_task.html", {"form": form, "group": group})

@login_required
def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.user != task.group.leader:
        return HttpResponseForbidden("Only the group leader can update tasks.")

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("group_detail", group_id=task.group.id)
    else:
        form = TaskForm(instance=task)

    return render(request, "tasks/update_task.html", {"form": form, "task": task})

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.user != task.group.leader:
        return HttpResponseForbidden("Only the group leader can delete tasks.")
    group_id = task.group.id
    task.delete()
    return redirect("group_detail", group_id=group_id)

@login_required
def toggle_task_completion(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.user != task.assigned_to and request.user != task.created_by:
        return HttpResponseForbidden("You can only complete tasks assigned to you or created by you.")
    task.is_completed = not task.is_completed
    task.save()
    return redirect("group_detail", group_id=task.group.id)