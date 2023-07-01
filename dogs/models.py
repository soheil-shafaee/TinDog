from django.db import models
from django.urls import reverse

# ------- Constant ------------
GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
)


class Dog(models.Model):
    name = models.CharField(max_length=200)
    breed = models.CharField(max_length=250)
    age = models.PositiveIntegerField()
    children = models.PositiveIntegerField(blank=True, null=True)
    vaccinated = models.BooleanField(default=True)
    explain = models.TextField()
    location = models.CharField(max_length=200)
    sex = models.CharField(max_length=1, blank=True, choices=GENDER_CHOICES)
    dog_photo = models.ImageField(upload_to='dogs_photo/', blank=True, null=True)

    def __str__(self):
        return f'{self.name}: {self.breed}'

    def get_absolute_url(self):
        return reverse('dogs_detail_view', args=[self.id])

