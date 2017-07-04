from django.shortcuts import render, redirect
from TeamManagement.models import Team
from django.contrib.auth.models import User, Group
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def index(request):
    team = Team.objects.order_by('group__name')
    return render(request, 'Teams.html', {'teams': team})


def validateteamname(request):
    name = request.POST.get('teamName')
    teamdescription = request.POST.get('teamDescription')
    teamtype = request.POST.get('teamTypeInput')
    if Group.objects.filter(name__iexact=name).exists():
        return HttpResponse('WRONG')
    else:
        group = Group()
        group.name = name
        group.save()
        team = Team()
        team.teamdescription = teamdescription
        team.teamtype = teamtype
        team.group = group
        team.save()
        return HttpResponse('Nice')
