from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['password2']:
            try:
                user = User.objects.get(username = request.POST['username'])
                return render(request, 'signup.html', {"UserExists": "Username has already been taken"})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], request.POST['password'])
                auth.login(request, user)
                return render(request, 'welcome.html')
        else:
            return render(request, 'signup.html', {"passwordUnmatched": "Password does not match"})
    else:
        print("Request not post")
        return render(request, 'signup.html')