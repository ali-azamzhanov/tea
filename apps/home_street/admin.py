from django.contrib import admin
from .models import (
    News, Menu, Settings, Home, About, AboutExtra,
    Subject, SubjectSection, History, Review, Gallery, HeaderFooterSettings
)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'published_at')
    search_fields = ('title', 'body')


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'order', 'created_at')
    search_fields = ('title',)
    ordering = ('order',)


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'key', 'updated_at')
    search_fields = ('key',)


@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_active')
    search_fields = ('title', 'subtitle')
    list_filter = ('is_active',)


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title', 'description')


@admin.register(AboutExtra)
class AboutExtraAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title', 'description')


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'order')
    search_fields = ('title', 'description')
    ordering = ('order',)


@admin.register(SubjectSection)
class SubjectSectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)


@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'year', 'title', 'order')
    search_fields = ('title', 'description')
    ordering = ('order',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'rating', 'is_active', 'created_at')
    search_fields = ('name', 'text')
    list_filter = ('is_active', 'rating')


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'year', 'order')
    search_fields = ('title', 'description')
    ordering = ('order',)


@admin.register(HeaderFooterSettings)
class HeaderFooterSettingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'working_hours', 'address')
    search_fields = ('name', 'address')
