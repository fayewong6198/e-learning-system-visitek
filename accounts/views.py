from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from .form import RegisterForm, LoginForm, CustomUserChangeForm, CustomPasswordChangeForm, CustomPasswordResetForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def login(request):
    form = LoginForm()
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'accounts/login.html', {'form': form})

    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        auth_login(request, user)
        return redirect('/')
    return render(request, 'accounts/login.html', {'form': form})

def logout(request):
  auth_logout(request)
  return redirect('/accounts/login')

def register(request):
    if request.method == "GET":
        form = RegisterForm()
        return render(request, 'accounts/register.html', {'form': form})

    form = RegisterForm(request.POST)
    if form.is_valid():
        user = form.save(commit=False)
        user.save()
        return redirect('/')
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def update_profile(request):
    if request.method == "GET":
        form = CustomUserChangeForm(instance = request.user)
        return render(request, 'accounts/update-profile.html', {'form': form})

    form = CustomUserChangeForm(data=request.POST, instance=request.user)
    if form.is_valid():
        user = form.save(commit=False)
        user.save()
    return  redirect('/accounts/update-profile')

@login_required
def change_password(request):
    if request.method == 'GET':
        form = CustomPasswordChangeForm(request.user)
        return render(request, 'accounts/change-password.html', {'form': form})

  
    form = CustomPasswordChangeForm(request.user, request.POST)
    if form.is_valid():
        print("--------------------------------------")
        print("Form is valid");
        user = form.save(commit=False)
        update_session_auth_hash(request, user) 
        user.save()
        return  redirect('/accounts/update-profile')
    messages.error(request, 'Please correct the error below.')
    return render(request, 'accounts/change-password.html', {'form': form})


def reset_password(request):
    if request.method == 'GET':
        form = CustomPasswordResetForm()
        return render(request, 'accounts/reset-password.html', {'form': form})





