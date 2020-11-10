from django.contrib import admin

from users.models import User


@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "phone")
