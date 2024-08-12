from django.contrib.auth.models import AbstractUser
from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthday = models.DateField()
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    height = models.FloatField()  # Height in cm
    weight = models.FloatField()  # Weight in kg
    is_family_head = models.BooleanField(default=False)  # Indicates if the user is the head of a family

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'birthday', 'gender', 'height', 'weight']

    def __str__(self):
        return self.username


class Family(models.Model):
    head = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='family_head')
    members = models.ManyToManyField(CustomUser, related_name='family_members')

    def __str__(self):
        return f"{self.head.email}'s Family"
