from .models import *
from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField


class KnowledgeCenterCategorySerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="category_detail")
    children = RecursiveField(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Knowledge_Center_Category
        fields = ["url", "id", "title", "children", "main_page_category"]


class KnowledgeCenterArticleSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Knowledge_Center_Article
        fields = ["category", "author", "text", "rate"]
        read_only_fields = ["category"]
