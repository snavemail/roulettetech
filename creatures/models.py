from django.db import models


# Create your models here.
class Creature(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    ability = models.CharField(max_length=50)
    power = models.IntegerField(default=0)
    defense = models.IntegerField(default=0)

    def __str__(self):
        return self.name
