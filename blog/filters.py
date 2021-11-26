import django_filters
from .models import PostComment, Post, BlogCategory
from django_filters import rest_framework as filters


class PostFilter(filters.FilterSet):
    category_name = django_filters.CharFilter(
        lookup_expr="contains", field_name="category__name", label="category name"
    )
    author_username = django_filters.CharFilter(
        lookup_expr="contains", field_name="author__username", label="author username"
    )

    class Meta:
        model = Post
        fields = [
            "title",
            "slug",
            "author",
            "author_username",
            "category",
            "category_name",
            "is_published",
        ]


class PostCommentFilter(filters.FilterSet):
    author_username = django_filters.CharFilter(
        lookup_expr="contains", field_name="author__username", label="author username"
    )
    post_author = django_filters.CharFilter(
        lookup_expr="contains", field_name="post__author", label="post author"
    )
    post_is_published = django_filters.BooleanFilter(
        field_name="post__is_published", label="post is published"
    )
    post_category_name = django_filters.CharFilter(
        lookup_expr="contains",
        field_name="post__category__name",
        label="post category name",
    )

    class Meta:
        model = PostComment
        fields = "__all__"
