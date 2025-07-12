from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (("Additional Info", {"fields": ("occupation", "phone_number", "address")}),)
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional Info", {"classes": ("wide",), "fields": ("occupation", "phone_number", "address")}),)


admin.site.register(CustomUser, CustomUserAdmin)
