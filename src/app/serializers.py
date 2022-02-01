from rest_framework import serializers
from .models import Musics, Author, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "title")


class MusicsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musics
        fields = ("id", "title", "author", "category")

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['category'] = CategorySerializer(instance.category, many=True).data

        return data


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'musics')
