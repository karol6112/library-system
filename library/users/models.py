from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=255, blank=False)
    id_number = models.CharField(max_length=9, blank=False, unique=True)

    def __str__(self):
        return self.username
