from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import CustomUser
from .forms import CustomUserForm

def register_view(request):
    if request.user.is_authenticated:
        return redirect('user:index')

    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Hello, {user.first_name}!")
            return redirect('user:index')

    else:
        form = CustomUserForm()
    return render(request, 'registration/signup.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('user:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('user:index')
        else:
            messages.error(request, f"Invalid email or password")
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('user:login')


@login_required
def user_list_view(request):
    users = CustomUser.objects.all()
    return render(request, 'user_list.html', {'users': users})


@login_required
def user_detail_view(request, user_id):
    target_user = get_object_or_404(CustomUser, pk=user_id)
    return render(request, 'user_detail.html', {'target_user': target_user})