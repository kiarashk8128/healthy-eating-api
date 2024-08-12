from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Family, FamilyMember


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('birthday', 'gender', 'height', 'weight', 'is_family_head')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': (
            'username', 'password1', 'password2', 'first_name', 'last_name', 'birthday', 'gender', 'height', 'weight',
            'is_family_head')}),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_family_head')
    search_fields = ('username', 'email', 'first_name', 'last_name')


@admin.register(Family)
class FamilyAdmin(admin.ModelAdmin):
    filter_horizontal = ('members',)


@admin.register(FamilyMember)
class FamilyMemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'birthday', 'gender', 'height', 'weight')
