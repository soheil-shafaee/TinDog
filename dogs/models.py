from django.db import models
from django.urls import reverse


class Dog(models.Model):
    name = models.CharField(max_length=200)
    breed = models.CharField(max_length=250)
    age = models.PositiveIntegerField()
    children = models.PositiveIntegerField(blank=True, null=True)
    vaccinated = models.BooleanField(default=True)
    explain = models.TextField()
    location = models.CharField(max_length=200)
    gender = models.CharField(max_length=10)
    dog_photo = models.ImageField(upload_to='dogs_photo/')

    def __str__(self):
        return f'{self.name}: {self.breed}'

    def get_absolute_url(self):
        return reverse('dogs_detail_view', args=[self.id])

