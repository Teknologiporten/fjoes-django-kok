from django.db import models

# Create your models here.

class AnimalType(models.Model):
    type = models.CharField(max_length=30, default=' ')
    def __str__(self):
        return self.type

class Animal(models.Model):
    name = models.CharField(max_length=30, default=' ')
    age = models.IntegerField()
    type = models.ForeignKey(AnimalType, on_delete=models.CASCADE)

    M = 'Male'
    F = 'Female'
    GENDER_CHOICES = (
        (M, 'M'), 
        (F, 'F')
    )
    gender = models.CharField(max_length=30, choices=GENDER_CHOICES)

    def __str__(self):
        return self.name