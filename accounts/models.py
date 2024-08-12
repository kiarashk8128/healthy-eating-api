from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(unique=True)
    birthday = models.DateField()
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    height = models.FloatField()  # Height in cm
    weight = models.FloatField()  # Weight in kg
    is_family_head = models.BooleanField(default=False)  # Indicates if the user is the head of a family
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'birthday', 'gender', 'height', 'weight', 'is_family_head']

    def __str__(self):
        return self.username
