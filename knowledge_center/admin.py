from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from knowledge_center.models import (
    ArticleRate,
    KnowledgeCenterArticle,
    KnowledgeCenterCategory,
)

admin.site.site_header = "Knowledge Center Dashboard"


@admin.register(KnowledgeCenterCategory)
class CategoryAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = (
        "tree_actions",
        "indented_title",
        "related_articles_count",
        "related_articles_cumulative_count",
    )
    list_display_links = ("indented_title",)

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative article count
        qs = KnowledgeCenterCategory.objects.add_related_count(
            qs,
            KnowledgeCenterArticle,
            "category",
            "articles_cumulative_count",
            cumulative=True,
        )

        # Add non cumulative article count
        qs = KnowledgeCenterCategory.objects.add_related_count(
            qs, KnowledgeCenterArticle, "category", "articles_count", cumulative=False
        )
        return qs

    def related_articles_count(self, instance):
        return instance.articles_count

    related_articles_count.short_description = (
        " articles count related to this category"
    )

    def related_articles_cumulative_count(self, instance):
        return instance.articles_cumulative_count

    related_articles_cumulative_count.short_description = (
        "articles count belongs to parent+children categories"
    )


@admin.register(KnowledgeCenterArticle)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("pk", "author", "avg_rate")
    list_filter = [
        "author",
    ]
    list_per_page = 20
    actions_selection_counter = True
    search_fields = ("author", "categoty__title")
    ordering = ("category__title",)


@admin.register(ArticleRate)
class ArticleRateAdmin(admin.ModelAdmin):
    list_display = ("article_id", "rate")
    list_filter = [
        "article",
    ]
    list_per_page = 20
    actions_selection_counter = True
    search_fields = ("article__id",)
    ordering = ("article",)
