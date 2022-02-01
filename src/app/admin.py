from django.contrib import admin
from .models import Musics, Author, Category


@admin.register(Musics)
class MusicAdmin(admin.ModelAdmin):
    list_display = ("id",)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("id",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id",)