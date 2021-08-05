from django.db import models

# Create your models here.

class MyPokemon(models.Model):
    name    = models.CharField(blank=True,max_length=50)
    pokedex_id  = models.IntegerField(blank=True)
    base_experience = models.IntegerField(blank=True)
    height  = models.IntegerField(blank=True)
    weight  = models.IntegerField(blank=True)
    type    = models.CharField(max_length=50,default='')
    level   = models.IntegerField(default=1)
    sprite  = models.CharField(max_length=100,default='')

    def __str__(self):
        return self.name