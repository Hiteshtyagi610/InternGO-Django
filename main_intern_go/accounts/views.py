from django.shortcuts import render

def login(request):
    return render(request, 'accounts/login.html')

def profile(request):
    return render(request, 'accounts/profile.html')

def register(request):
    return render(request, 'accounts/register'
    '.html')