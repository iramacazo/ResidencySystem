from django.shortcuts import render, redirect
from TeamManagement.models import Team
from django.contrib.auth.models import User, Group
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.


@login_required
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


@staff_member_required
def deleteteam(request, groupid):
    Group.objects.filter(id=groupid).delete()
    return redirect('index')
