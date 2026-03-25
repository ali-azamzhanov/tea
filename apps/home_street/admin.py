from django.contrib import admin
from .models import News, Program, UsefulLink


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'published_at')
    search_fields = ('title', 'body')


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    search_fields = ('name', 'description')


@admin.register(UsefulLink)
class UsefulLinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url', 'created_at')
    search_fields = ('title', 'description')
