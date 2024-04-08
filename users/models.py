from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    name = models.CharField(max_length=30, verbose_name='имя')
    is_active = models.BooleanField(default=False, verbose_name='активный')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
