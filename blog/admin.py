from django.contrib import admin
from .models import PostComment, Post, BlogCategory
from mptt.admin import MPTTModelAdmin


@admin.register(BlogCategory)
class BlogCategoryAdmin(MPTTModelAdmin):
    mptt_level_indent = 20
    list_display = ("id", "name", "parent")
    list_display_link = "id"
    list_editable = ("parent", "name")
    sortable = "-id"


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "author",
        "is_published",
        "category",
    )
    list_editable = ("title", "author", "is_published", "category")


@admin.register(PostComment)
class PostCommentAdmin(MPTTModelAdmin):
    mptt_level_indent = 20
    list_display = ("id", "author", "post", "is_published", "parent")
    list_editable = ("author", "post", "is_published", "parent")
    sortable = "-id"
