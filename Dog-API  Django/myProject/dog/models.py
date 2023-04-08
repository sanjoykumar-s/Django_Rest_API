from django import forms
from django.db import models
from . import choices


# Create your models here.
class Breed(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=30, choices=choices.SIZE_CHOICE)
    friendliness = models.IntegerField(choices=choices.CHOICES_INT)
    trainability = models.IntegerField(choices=choices.CHOICES_INT)
    sheddingamount = models.IntegerField(choices=choices.CHOICES_INT)

    def __str__(self):
        return self.name


class Dog(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    gender = models.CharField(max_length=15, choices=choices.GENDER)
    color = models.CharField(max_length=50)
    favoritefood = models.CharField(max_length=50)
    favoritetoy = models.CharField(max_length=50)

    def __str__(self):
        return self.name
