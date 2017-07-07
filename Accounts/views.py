from django.shortcuts import render
from Accounts.forms import SignUpForm, LogInForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from Accounts.models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.


def register(request):
    if request.user.is_authenticated():
        return redirect('mainpage')
    else:
        if request.method == 'POST':
            registration = SignUpForm(request.POST)
            if registration.is_valid():
                registration.save()
                username = registration.cleaned_data.get('username')
                raw_password = registration.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                userprofile = UserProfile(request.user.id)
                userprofile.save()
                return redirect('mainpage')
        else:
            registration = SignUpForm()

        return render(request, 'register.html', {'registration': registration})


def login_view(request):
    if request.user.is_authenticated():
        return redirect('mainpage')
    else:
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


@login_required
def mainpage(request):
    return render(request, 'Mainpage.html')


def homepage(request):
    if request.user.is_authenticated():
        return redirect('mainpage')
    else:
        return render(request, 'HomePage.html')


@staff_member_required
def members(request):
    list_of_users = User.objects.filter(is_staff=False).order_by('last_name')
    return render(request, 'members.html', {'users': list_of_users})


@staff_member_required
def deleteuser(request, userid):
    User.objects.filter(id=userid).delete()
    return redirect('members')
