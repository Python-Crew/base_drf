from django.contrib import admin
from .models import SocialMeta, GenarallMeta, Page

# Register your models here.


class SocialMetaInline(admin.TabularInline):
    model = SocialMeta
    max_num = 1


class GenarallMetaInline(admin.TabularInline):
    model = GenarallMeta
    max_num = 1


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    inlines = (SocialMetaInline, GenarallMetaInline)
    list_display = ("id", "url", "redirect_to", "redirect_status", "operation")
    list_editable = ("url", "operation", "redirect_status")
    search_fields = ("id", "redirect_status")
