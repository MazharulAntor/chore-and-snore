from django.shortcuts import render, redirect
from .forms import CustomUserRegistrationForm
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Optional: log them in after registration
            return redirect('home')  # Replace 'home' with your actual home page
    else:
        form = CustomUserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

