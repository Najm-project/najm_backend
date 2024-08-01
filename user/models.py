from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class User(AbstractUser):
    phone_number = models.CharField(max_length=13, unique=True, null=True, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'user'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
