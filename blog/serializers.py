from os import read
from rest_framework import serializers
from . import models
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = (
            "username", "first_name", "last_name"
        )


class PostModelSerializer(serializers.ModelSerializer):
    thumbnail = serializers.SerializerMethodField("get_thumbnail")
    webp_image = serializers.SerializerMethodField("get_webp_image")
    author_detail = UserModelSerializer(source="author", read_only=True)

    def get_thumbnail(self, obj):
        thumbnail = obj.thumbnail_image.url
        return thumbnail

    def get_webp_image(self, obj):
        webp_image = obj.webp_image.url
        return webp_image

    class Meta:
        model = models.Post
        exclude = ("image", "author")
