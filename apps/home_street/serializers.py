from rest_framework import serializers
from .models import (
    News, Menu, Settings, Home, About, AboutExtra,
    Subject, SubjectSection, History, Review, Gallery, HeaderFooterSettings
)


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'title', 'body', 'published_at']


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'title', 'url', 'order', 'created_at']


class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = ['id', 'key', 'value', 'updated_at']


class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = ['id', 'title', 'subtitle', 'image', 'button_text', 'button_url', 'is_active']


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ['id', 'title', 'description', 'image_main', 'image_secondary', 'button_text', 'button_url']


class AboutExtraSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutExtra
        fields = ['id', 'title', 'description', 'image']


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'title', 'description', 'image', 'button_text', 'button_url', 'order']


class SubjectSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectSection
        fields = ['id', 'title']


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ['id', 'year', 'title', 'description', 'image', 'order']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'name', 'text', 'rating', 'created_at', 'is_active']


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ['id', 'image', 'title', 'description', 'year', 'order']


class HeaderFooterSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeaderFooterSettings
        fields = ['id', 'name', 'logo', 'instagram_url', 'faacebook_url', 'working_hours', 'address', 'views_counter', 'map_iframe']
