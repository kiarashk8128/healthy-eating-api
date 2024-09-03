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
        # Superuser doesn't need to provide these fields
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        # Remove fields not required for superuser
        extra_fields.pop('birthday', None)
        extra_fields.pop('gender', None)
        extra_fields.pop('height', None)
        extra_fields.pop('weight', None)
        extra_fields.pop('is_family_head', None)

        return self.create_user(username, email, password, **extra_fields)


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')],
                              blank=True, null=True)
    height = models.FloatField(blank=True, null=True)  # Height in cm
    weight = models.FloatField(blank=True, null=True)  # Weight in kg
    is_family_head = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

    def __str__(self):
        return self.username


class FamilyMember(models.Model):
    family_head = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='family_members')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthday = models.DateField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    height = models.FloatField()  # Height in cm
    weight = models.FloatField()  # Weight in kg

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
