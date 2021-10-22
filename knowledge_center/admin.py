from django.contrib import admin
from knowledge_center.views import *

admin.site.site_header = "FAQ Dashboard"


@admin.register(Knowledge_Center_Category)
class CategoryAdmin(admin.ModelAdmin):
    # readonly_fields = ['',]
    list_display = ("title", "parent", "main_page_category")
    list_filter = ["title", "parent"]
    list_per_page = 20
    actions_selection_counter = True
    # date_hierarchy = 'name'
    search_fields = ("title", "parent", "main_page_category")
    ordering = ("title",)


@admin.register(Knowledge_Center_Article)
class ArticleAdmin(admin.ModelAdmin):
    # readonly_fields = ['',]
    list_display = ("pk", "author", "rate")
    list_filter = ["author",]
    list_per_page = 20
    actions_selection_counter = True
    search_fields = ("author", "categoty__title")
    ordering = ("category__title",)
