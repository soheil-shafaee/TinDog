from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .forms import CustomUserChange, CustomUserCreation


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreation
    form = CustomUserChange
    model = CustomUser
    list_display = ['username', 'email', 'age', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age',)}),)
    add_fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age',)}),)


admin.site.register(CustomUser, CustomUserAdmin)
