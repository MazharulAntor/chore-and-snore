from django.urls import path
from . import views

urlpatterns = [
    path('create/<int:group_id>/', views.create_task, name='create_task'),
    path('update/<int:task_id>/', views.update_task, name='update_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('toggle/<int:task_id>/', views.toggle_task_completion, name='toggle_task_completion'),
]