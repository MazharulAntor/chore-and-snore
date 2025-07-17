from django.urls import path
from . import views
from .views import dashboard

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('create/', views.create_group, name='create_group'),
    path('<int:group_id>/', views.group_detail, name='group_detail'),
    path('<int:group_id>/add-member/', views.add_member, name='add_member'),
    path('<int:group_id>/transfer-leader/', views.transfer_leadership, name='transfer_leadership'),
    path('<int:group_id>/leave/', views.leave_group, name='leave_group'),
]
