from os import read
from rest_framework import serializers
from . import models
from django.conf import settings

from django.contrib.auth import get_user_model
User = get_user_model()

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ("username", "first_name", "last_name")


class PostModelSerializer(serializers.ModelSerializer):
    thumbnail = serializers.CharField(source="thumbnail_image.url")
    webp_image = serializers.CharField(source="webp_image.url")
    # author_detail = UserModelSerializer(source="author", read_only=True)

    class Meta:
        model = models.Post
        exclude = ("image",)
