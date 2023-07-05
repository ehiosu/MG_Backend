from django.db import models
from django.contrib.auth.models import User
from django.db import models
# Create your models here.



class Item(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Character(models.Model):
    name = models.CharField(max_length=100)
    level = models.IntegerField()
    player = models.ForeignKey(User, on_delete=models.CASCADE, related_name='characters')

    def __str__(self):
        return self.name

class Inventory(models.Model):
    character = models.OneToOneField(Character, on_delete=models.CASCADE, related_name='inventory')
    items = models.ManyToManyField(Item)

    def __str__(self):
        return f"Inventory of {self.character}"
