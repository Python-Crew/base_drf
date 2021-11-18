from django.contrib import admin
from . import models
from imagekit.admin import AdminThumbnail
from mptt.admin import MPTTModelAdmin


@admin.register(models.BlogCategory)
class BlogCategoryAdmin(MPTTModelAdmin):
    mptt_level_indent = 20
    list_display = ("id", "name", "parent")
    list_display_link = "id"
    list_editable = ("parent", "name")
    sortable = "-id"


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "author",
        "is_published",
        "category",
    )
    list_editable = ("title", "author", "is_published", "category")


@admin.register(models.PostComment)
class PostCommentAdmin(MPTTModelAdmin):
    mptt_level_indent = 20
    list_display = ("id", "author", "post", "is_published", "parent")
    list_editable = ("author", "post", "is_published", "parent")
    sortable = "-id"
