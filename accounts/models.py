from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=10, null=True, blank=True)
    last_name = models.CharField(max_length=10, null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
