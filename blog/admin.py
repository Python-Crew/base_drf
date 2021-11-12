from django.contrib import admin
import imagekit
from . import models
from django.utils.html import format_html
from imagekit.admin import AdminThumbnail
from mptt.admin import MPTTModelAdmin

from django import forms
from ckeditor.widgets import CKEditorWidget


class PostAdminForm(forms.ModelForm):
    content_b = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = models.Post
        fields = ('__all__')


@admin.register(models.BlogCategory)
class BlogCategoryAdmin(MPTTModelAdmin):
    mptt_level_indent = 20
    list_display = ("id", "name", "parent")
    list_display_link = "id"
    list_editable = ("parent", "name")
    sortable = "-id"


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    admin_thumbnail = AdminThumbnail(image_field="image")
    list_display = (
        "id",
        "title",
        "author",
        "is_published",
        "category",
        "admin_thumbnail",
    )
    list_editable = ("title", "author", "is_published", "category")


@admin.register(models.PostComment)
class PostCommentAdmin(MPTTModelAdmin):
    mptt_level_indent = 20
    list_display = ("id", "author", "post", "is_published", "parent")
    list_editable = ("author", "post", "is_published", "parent")
    sortable = "-id"
