from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from .models import User
# Register your models here.
@admin.register(User)
class Useradmin(DjangoUserAdmin):
    list_display = ("id", )
