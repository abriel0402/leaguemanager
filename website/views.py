from django.shortcuts import render
import random
from website.forms import *





def getTeams():
    TEAMS_OBJECTS = Team.objects.all()
    TeamsList = []
    for obj in TEAMS_OBJECTS:
        TeamsList.append(obj)
    return TeamsList


#n = num of games
#teams = shuffled teams
def generateSchedule(weeks):
    teams = getTeams()
    schedule = []
    if len(teams) % 2 == 0:
        for i in range(weeks):
            teams = getTeams()
            while len(teams) != 0:
                n = random.randint(0,len(teams)-1)
                team1 = teams[n]
                teams.remove(team1)
                n = random.randint(0,len(teams)-1)
                team2 = teams[n]
                teams.remove(team2)
                game = [team1, team2]
                schedule.append(game)
                
            
   
    return schedule
    

# Create your views here.

def index(request):
    return render(request, "website/index.html")

def standings(request):
    TEAMS = getTeams()
    def sortWins(e):
        return e.wins
    TEAMS.sort(reverse=True, key=sortWins)

    return render(request, "website/standings.html", {
        "sorted": TEAMS,
    })


def stats(request):
    return render(request, "website/stats.html")


def schedule(request):
    TEAMS = getTeams()
    random.shuffle(TEAMS)
    schedule = generateSchedule((len(TEAMS)-1)*2)



    return render(request, "website/schedule.html", {
        "schedule": schedule,
    })

def settings(request):

    return render(request, "website/settings.html")

def teamManagement(request):
    form = CreateTeamForm()
    if request.method == "POST":
        
        form = CreateTeamForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
    
    TEAMS = Team.objects.all()

    
    return render(request, 'website/teamManagement.html', {
        "teams": TEAMS,
        "form": form,
    })