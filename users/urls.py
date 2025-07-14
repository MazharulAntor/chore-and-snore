from django.contrib.auth.views import LoginView
from django.urls import path

from .forms import CustomLoginForm
from .views import register

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='users/login.html', authentication_form=CustomLoginForm),
         name='login'),
]
