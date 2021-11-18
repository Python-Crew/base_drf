from os import read
from rest_framework import serializers
from . import models


class PostModelSerializer(serializers.ModelSerializer):
    thumbnail = serializers.SerializerMethodField("get_thumbnail_image")
    webp_image = serializers.SerializerMethodField("get_webp_image")
    author_username = serializers.CharField(source="author.username", read_only=True)
    author_first_name = serializers.CharField(
        source="author.first_name", read_only=True
    )
    author_last_name = serializers.CharField(source="author.last_name", read_only=True)
    category_name = serializers.CharField(source="category.name", read_only=True)

    def get_thumbnail_image(self, obj):
        if obj.thumbnail_image:
            thumbnail = obj.thumbnail_image.url
            return thumbnail

    def get_webp_image(self, obj):
        if obj.webp_image:
            webp = obj.webp_image.url
            return webp

    class Meta:
        model = models.Post
        exclude = ("image",)


class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BlogCategory
        fields = "__all__"


class PostCommentSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source="author.usesrname", read_only=True)
    author_first_name = serializers.CharField(
        source="author.first_name", read_only=True
    )
    author_last_name = serializers.CharField(source="author.last_name", read_only=True)

    class Meta:
        model = models.PostComment
        fields = "__all__"
