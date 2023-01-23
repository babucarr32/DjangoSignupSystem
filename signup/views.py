from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['password2']:
            try:
                user = User.objects.get(username = request.POST['username'])
                return render(request, {"UserExists": "Username has already been taken"})
            except User.DoesNotExist:
                user.objects.create_user(request.POST['username'], request.POST['passsword'])
                auth.login(request, user)
                return redirect('/')
    return render(request, 'signup.html')