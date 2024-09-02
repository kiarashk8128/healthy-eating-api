from django.db import models
from accounts.models import CustomUser, FamilyMember


class FoodGroup(models.Model):
    id = models.AutoField(primary_key=True)
    fgid = models.CharField(max_length=10)
    fgcat_id = models.CharField(max_length=10, unique=True)
    fgcat = models.CharField(max_length=255)
    foodgroup = models.CharField(max_length=255)

    def __str__(self):
        return self.fgcat_id


class DirectionalStatement(models.Model):
    id = models.AutoField(primary_key=True)
    fgid = models.CharField(max_length=10)
    directional_statement = models.TextField()

    def __str__(self):
        return self.directional_statement


class Food(models.Model):
    id = models.AutoField(primary_key=True)
    fgid = models.CharField(max_length=10)
    fgcat_id = models.ForeignKey(FoodGroup, on_delete=models.CASCADE)
    srvg_sz = models.CharField(max_length=50)
    food = models.CharField(max_length=255)

    def __str__(self):
        return self.food


class ServingPerDay(models.Model):
    id = models.AutoField(primary_key=True)
    fgid = models.CharField(max_length=10)
    gender = models.CharField(max_length=10, default='Unknown')
    ages = models.CharField(max_length=50, default='Unknown')
    servings = models.CharField(max_length=50, default='Unknown')

    def __str__(self):
        return f"{self.gender} ({self.ages}) - {self.servings} servings - {self.fgid} fgid"


class Menu(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    family_member = models.ForeignKey(FamilyMember, on_delete=models.CASCADE, null=True, blank=True)
    menu_data = models.JSONField()  # Store the menu in a structured JSON format
    selected = models.BooleanField(default=False)

    def __str__(self):
        if self.family_member:
            return f"Menu for {self.family_member.first_name} {self.family_member.last_name} (Family Member of {self.user.username})"
        return f"Menu for {self.user.username}"
