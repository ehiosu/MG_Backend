from django.db import models
from django.contrib.auth.models import User
from django.db import models

# Create your models here.



class Item(models.Model):
    name = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name

class Character(models.Model):
    name = models.CharField(max_length=100)
    level = models.IntegerField()
    player = models.ForeignKey(User, on_delete=models.CASCADE, related_name='characters')
    active_slots = models.JSONField(default=dict)


    def __str__(self):
        return self.name

class Inventory(models.Model):
    character = models.OneToOneField(Character, on_delete=models.CASCADE, related_name='inventory')
    items = models.ManyToManyField(Item)

    def __str__(self):
        return f"Inventory of {self.character}"


class  Weapon(Item):
    DAMAGE_TYPES = (
        ('Physical', 'Physical'),
        ('Fire', 'Fire'),
        ('Water', 'Water'),
        ('Wind', 'Wind'),
        ('Light', 'Light'),
        ('Dark', 'Dark'),
    )

    damage_type = models.CharField(choices=DAMAGE_TYPES, max_length=10)
    strength = models.IntegerField()
    intelligence = models.IntegerField()
    dexterity = models.IntegerField()


class ItemWeapon(models.Model):
    DAMAGE_TYPES = (
        ('Physical', 'Physical'),
        ('Fire', 'Fire'),
        ('Water', 'Water'),
        ('Wind', 'Wind'),
        ('Light', 'Light'),
        ('Dark', 'Dark'),
    )
    item = models.OneToOneField(Item, on_delete=models.CASCADE,primary_key=True)
    damage_type = models.CharField(choices=DAMAGE_TYPES, max_length=10)
    strength = models.IntegerField()
    intelligence = models.IntegerField()
    dexterity = models.IntegerField()

    def __str__(self):
        return f"Weapon (ID: {self.pk})"
