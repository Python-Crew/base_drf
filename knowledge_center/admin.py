from django.contrib import admin

from knowledge_center.models import ArticleRate, KnowledgeCenterArticle, KnowledgeCenterCategory

admin.site.site_header = "Knowledge Center Dashboard"


@admin.register(KnowledgeCenterCategory)
class CategoryAdmin(admin.ModelAdmin):
    # readonly_fields = ['',]
    list_display = ("title", "parent", "main_page_category")
    list_filter = ["title", "parent"]
    list_per_page = 20
    actions_selection_counter = True
    # date_hierarchy = 'name'
    search_fields = ("title", "parent", "main_page_category")
    ordering = ("title",)


@admin.register(KnowledgeCenterArticle)
class ArticleAdmin(admin.ModelAdmin):
    # readonly_fields = ['',]
    list_display = ("pk", "author","Avg_rate")
    list_filter = [
        "author",
    ]
    list_per_page = 20
    actions_selection_counter = True
    search_fields = ("author", "categoty__title")
    ordering = ("category__title",)


@admin.register(ArticleRate)
class ArticleRateAdmin(admin.ModelAdmin):
    # readonly_fields = ['',]
    list_display = ("article_id", "rate")
    list_filter = [
        "article",
    ]
    list_per_page = 20
    actions_selection_counter = True
    search_fields = ("article__id", )
    ordering = ("article",)
