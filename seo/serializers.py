from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from . import models


class PageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Page
        fields = "__all__"


class SocialMetaModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SocialMeta
        exclude = ("id", "page")


class GenarallMetaModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GenarallMeta
        exclude = ("id", "page")


class CombineSerializer(serializers.Serializer):
    social_meta = serializers.SerializerMethodField("get_social")
    generall_meta = serializers.SerializerMethodField("get_generall")

    def get_social(self, obj):
        social_mata = models.SocialMeta.objects.get(page=obj)
        data = SocialMetaModelSerializer(
            social_mata,
        ).data
        return data

    def get_generall(self, obj):
        generall_meta = models.GenarallMeta.objects.get(page=obj)
        data = GenarallMetaModelSerializer(
            generall_meta,
        ).data
        return data
