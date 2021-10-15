from django.contrib import admin
import imagekit
from . import models
from django.utils.html import format_html
from imagekit.admin import AdminThumbnail

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id", "name", "parent"
    )
    list_editable = (
        "name", "parent"
    )


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):

    admin_thumbnail = AdminThumbnail(image_field='image')
    list_display = (
        "id", "title", "author", "is_published", "category",
        'admin_thumbnail'
    )
    list_editable = (
        "title", "author", "is_published", "category"
    )


@admin.register(models.PostComment)
class PostCommentAdmin(admin.ModelAdmin):
    list_display = (
        "id", "author", "post", "is_published", "parent"
    )
    list_editable = (
        "author", "post", "is_published", "parent"
    )
