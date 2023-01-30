from django.db import models

# Create your models here.

class Team(models.Model):
    city = models.CharField(min_length=4, max_length=32)
    name = models.CharField(min_length=4, max_length=32)
    wins = models.IntegerField()
    losses = models.IntegerField()


class Player(models.Model):
    first = models.CharField(min_length=2, max_length=16)
    last = models.CharField(min_length=2, max_length=16)
    number = models.IntegerField()
    