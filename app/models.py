from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    age = models.PositiveIntegerField(default=20)
    first_name = None

    def __str__(self):
        return f"{self.username} - {self.age}"





