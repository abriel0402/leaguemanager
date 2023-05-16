from django.shortcuts import render

from website.forms import *


TEAMS = Team.objects.all()













# Create your views here.

def index(request):
    return render(request, "website/index.html")

def standings(request):
    TEAMS_OBJECTS = Team.objects.all()
    TeamsList = []
    for obj in TEAMS_OBJECTS:
        TeamsList.append(obj)
    def sortWins(e):
        return e.wins
    TeamsList.sort(reverse=True, key=sortWins)




    return render(request, "website/standings.html", {
        "sorted": TeamsList,
    })


def stats(request):
    return render(request, "website/stats.html")


def schedule(request):
    return render(request, "website/schedule.html")

def settings(request):

    return render(request, "website/settings.html")

def teamManagement(request):
    form = CreateTeamForm()
    if request.method == "POST":
        
        form = CreateTeamForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            print("saved")
    
    TEAMS = Team.objects.all()

    
    return render(request, 'website/teamManagement.html', {
        "teams": TEAMS,
        "form": form,
    })