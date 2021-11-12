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
        model = KnowledgeCenterCategory
        fields = ["url", "id", "title", "children", "main_page_category"]


class KnowledgeCenterArticleSerilizer(serializers.ModelSerializer):
    class Meta:
        model = KnowledgeCenterArticle
        fields = ["category", "author", "text", "Avg_rate"]


class ArticleRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleRate
        fields = ["article", "rate"]
