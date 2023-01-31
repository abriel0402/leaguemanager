from django.db import models

# Create your models here.

class Team(models.Model):
    city = models.CharField(max_length=32)
    name = models.CharField(max_length=32)
    wins = models.IntegerField()
    losses = models.IntegerField()

    def __str__(self):
        return self.city + " " + self.name


class Player(models.Model):
    first = models.CharField(max_length=32)
    last = models.CharField(max_length=32)
    number = models.IntegerField()

    def __str__(self):
        return self.first + " " + self.last