from django.contrib import admin
from .models import FoodGroup, Food, ServingPerDay, DirectionalStatement


from django.contrib import admin
from .models import Menu

class MenuAdmin(admin.ModelAdmin):
    list_display = ('user', 'family_member', 'selected')
    list_filter = ('user', 'family_member', 'selected')
admin.site.register(Menu, MenuAdmin)

admin.site.register(FoodGroup)
admin.site.register(Food)
admin.site.register(ServingPerDay)
admin.site.register(DirectionalStatement)
