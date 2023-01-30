from django.shortcuts import render




teams = []






# Create your views here.

def index(request):
    return render(request, "website/index.html")

def standings(request):
    return render(request, "website/standings.html")


def stats(request):
    return render(request, "website/stats.html")


def schedule(request):
    return render(request, "website/schedule.html")

def settings(request):


    return render(request, "website/settings.html")