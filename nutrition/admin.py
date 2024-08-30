from django.contrib import admin
from .models import FoodGroup, Food, ServingPerDay, DirectionalStatement

admin.site.register(FoodGroup)
admin.site.register(Food)
admin.site.register(ServingPerDay)
admin.site.register(DirectionalStatement)
