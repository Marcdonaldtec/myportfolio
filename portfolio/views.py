from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from .models import Profile

def home(request):
    return render(request, 'portfolio/home.html')

def about_me(request):
    profile = Profile.objects.first()
    return render(request, 'portfolio/about_me.html', {'profile': profile})
