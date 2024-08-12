from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, FamilyMember
from .forms import CustomUserCreationForm, CustomUserChangeForm


class FamilyMemberInline(admin.TabularInline):
    model = FamilyMember
    extra = 1  # Allow adding multiple family members


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('birthday', 'gender', 'height', 'weight')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': (
            'username', 'password1', 'password2', 'email', 'first_name', 'last_name', 'birthday', 'gender', 'height',
            'weight')}),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')

    def get_inline_instances(self, request, obj=None):
        if obj and obj.is_family_head:
            return [FamilyMemberInline(self.model, self.admin_site)]
        return []


# Register the models
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(FamilyMember)
