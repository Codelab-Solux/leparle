from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from accounts.models import CustomUser
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import *
# Create your views here.


# def signupView(req):
#     if req.user.is_authenticated:
#         return redirect('home')

#     form = SignupForm()
#     if req.method == 'POST':
#         form = SignupForm(req.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(req, "Votre compte vien d'être créé.")
#             return redirect('login')
#     else:
#         form = SignupForm()
#     context = {
#         "signup_page": "active",
#         "title": 'signup',
#         'form': form,
#     }
#     return render(req, 'accounts/signup.html', context)


def loginView(req):
    if req.user.is_authenticated:
        return redirect('home')

    if req.method == 'POST':
        username = req.POST.get('username')
        password = req.POST.get('password')

        user = authenticate(req, username=username, password=password)

        if user is not None:
            login(req, user)
            if 'next' in req.POST:
                return redirect(req.POST.get('next'))

            else:
                return redirect('home')
        else:
            messages.info(req, 'Username or Password is incorrect!')
    context = {
        "login_page": "active",
        "title": 'login'}
    return render(req, 'accounts/login.html', context)


@login_required(login_url='login')
def logoutUser(req):
    logout(req)
    return redirect('login')


@login_required(login_url='login')
def users(req):
    user = req.user
    users = CustomUser.objects.all()
    ordering = ['last_name']
    if user.role.sec_level >= 1:
        form = NewUserForm()
        if req.method == 'POST':
            form = NewUserForm(req.POST)
            if form.is_valid():
                form.save()
                messages.success(req, "New user added successfully.")
                return redirect('users')
    else:
        return redirect(req.META.get('HTTP_REFERER'))

    context = {
        "users_page": "active",
        'title': 'users',
        'users': users,
        'ordering': ordering,
        'form': form,
    }
    return render(req, 'accounts/users.html', context)


@ login_required(login_url='login')
def user_profile(req, pk):
    user = req.user
    profile = CustomUser.objects.get(id=pk)

    if user == profile:
        form = EditUserForm(instance=profile)
        if req.method == 'POST':
            form = EditUserForm(req.POST, instance=profile)
            if form.is_valid():
                form.save()
                return redirect('users')

    if user.role.sec_level >= 2:
        form = AdminEditUserForm(instance=profile)
        if req.method == 'POST':
            form = AdminEditUserForm(req.POST, instance=profile)
            if form.is_valid():
                form.save()
                return redirect(req.META.get('HTTP_REFERER'))
    else:
        form = None
    context = {
        "rdv_page": "active",
        'title': 'appointment_detail',
        'profile': profile,
        'form': form,
    }
    return render(req, 'accounts/profile.html', context)
