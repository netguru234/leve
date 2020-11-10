from django.contrib import admin

from users.models import User


@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username", "get_user_full_name", "email", "phone")

    def get_user_full_name(self, obj):
        return f"{obj.get_full_name()}"

    get_user_full_name.short_description = "Full Name"
