from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from .models import Page, SocialMeta, GenarallMeta


class PageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = "__all__"


class SocialMetaModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMeta
        exclude = ("id", "page")


class GenarallMetaModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenarallMeta
        exclude = ("id", "page")


class CombineSerializer(serializers.Serializer):
    social_meta = serializers.SerializerMethodField("get_social")
    generall_meta = serializers.SerializerMethodField("get_generall")

    def get_social(self, obj):
        social_mata = SocialMeta.objects.get(page=obj)
        data = SocialMetaModelSerializer(
            social_mata,
        ).data
        return data

    def get_generall(self, obj):
        generall_meta = GenarallMeta.objects.get(page=obj)
        data = GenarallMetaModelSerializer(
            generall_meta,
        ).data
        return data
