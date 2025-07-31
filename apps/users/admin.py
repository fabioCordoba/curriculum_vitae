from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from apps.users.models.user import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    pass
