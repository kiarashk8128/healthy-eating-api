from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        return self.create_user(username, email, password, **extra_fields)


class CustomUser(AbstractUser):
    email = models.EmailField()
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')],
                              blank=True, null=True)
    height = models.FloatField(blank=True, null=True)  # Height in cm
    weight = models.FloatField(blank=True, null=True)  # Weight in kg
    is_family_head = models.BooleanField(default=False)  # Indicates if the user is the head of a family

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

    def __str__(self):
        return self.username


class Family(models.Model):
    head = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='family_head')
    members = models.ManyToManyField('FamilyMember', related_name='families')

    def __str__(self):
        return f"{self.head.username}'s Family"


class FamilyMember(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthday = models.DateField()
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    height = models.FloatField()  # Height in cm
    weight = models.FloatField()  # Weight in kg
    family = models.ForeignKey(Family, on_delete=models.CASCADE, related_name='family_members')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
