from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLE_CHOICES = [
        ('USER', 'User'),
        ('ADMIN', 'Admin'),
    ]
    nickname = models.CharField(max_length=50, unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='USER')
    
    def __str__(self):
        return self.nickname