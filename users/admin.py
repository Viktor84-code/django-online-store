from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ("id", "email", "phone", "country", "is_staff")
    ordering = ("email",)  # <--- меняем username на email
    fieldsets = UserAdmin.fieldsets + (
        ("Дополнительная информация", {"fields": ("phone", "avatar", "country")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Дополнительная информация", {"fields": ("phone", "avatar", "country")}),
    )
