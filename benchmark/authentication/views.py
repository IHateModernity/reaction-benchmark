from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages


def authentication(request):
    if "register" in request.method == "POST":  # add the name "register" in your html button
        form = UserCreationForm

    if "login" in request.method == "POST":  # add the name "login" in your html button
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ('Wrong username or password. Try again.'))
            return redirect('authentication')


    return render(request, 'authentication/register_login.html')

