from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email= models.EmailField(unique=True)
    telefono = models.CharField(max_length=250,blank=True)
    run = models.CharField(max_length=20,blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

