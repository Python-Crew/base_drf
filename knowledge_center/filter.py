from django_filters import rest_framework as filters
from knowledge_center.models import KnowledgeCenterCategory, KnowledgeCenterArticle


class CategoryFilter(filters.FilterSet):
    class Meta:
        model = KnowledgeCenterCategory
        fields = ("title", "parent")


class ArticleFilter(filters.FilterSet):
    class Meta:
        model = KnowledgeCenterArticle
        fields = ("author", "category")
