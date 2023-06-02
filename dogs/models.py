from django.db import models


class Dog(models.Model):
    name = models.CharField(max_length=200)
    breed = models.CharField(max_length=250)
    age = models.PositiveIntegerField()
    children = models.PositiveIntegerField(blank=True, null=True)
    location = models.CharField(max_length=200)
    vaccinated = models.BooleanField()

    def __str__(self):
        return f'{self.name}: {self.location}'
