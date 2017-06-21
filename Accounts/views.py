from django.shortcuts import render
from Accounts.forms import SignUpForm, LogInForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

# Create your views here.


def register(request):
    if request.method == 'POST':
        registration = SignUpForm(request.POST)
        if registration.is_valid():
            registration.save()
            username = registration.cleaned_data.get('username')
            raw_password = registration.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('mainpage')
    else:
        registration = SignUpForm()

    return render(request, 'register.html', {'registration': registration})


def login_view(request):
    if request.method == 'POST':
        login_form = LogInForm(request.POST)
        username = login_form.request['username']
        password = login_form.request['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('mainpage')

    else:
        login_form = LogInForm()

    return render(request, 'login.html', {'login': login_form})
