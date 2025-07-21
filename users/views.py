from django.shortcuts import render, redirect
from .forms import CustomUserRegistrationForm
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = CustomUserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

