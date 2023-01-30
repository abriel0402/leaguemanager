from . import views
from django.urls import path



urlpatterns = [
    path("", views.index, name="index"),
    path("standings/", views.standings, name="standings"),
    path("stats/", views.stats, name="stats"),
    path("schedule/", views.schedule, name="schedule"),
    path("settings/", views.settings, name="settings"),

]