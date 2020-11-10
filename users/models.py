from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phone = models.CharField(max_length=50, default="")

    def __str__(self):
        return f"{self.get_full_name()}"
