from . import views
from django.urls import path



urlpatterns = [
    path("", views.index, name="index"),
    path("standings/", views.standings, name="standings"),
    path("stats/", views.stats, name="stats"),
    path("schedule/", views.schedule, name="schedule"),
    path("settings/", views.settings, name="settings"),
    path("team-management/", views.teamManagement, name="teamManagement"),
    path("player-management/", views.playerManagement, name="playerManagement"),
    path("league-management/", views.leagueManagement, name="leagueManagement"),
    path("team/<int:teamID>/", views.team, name="team"),
    path("player/<int:playerID>/", views.player, name="player"),


]