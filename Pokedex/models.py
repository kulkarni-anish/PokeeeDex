from django.db import models

# Create your models here.
class verybasic(models.Model):
    hello   = models.TextField(blank=True)
    pokemon = models.BooleanField(default=True)
    price   = models.IntegerField(default=100)
    description = models.TextField(default="hello my pokemon")