from django.urls import path, include
from .views import (
    ArticleDetailAPIView,
    ArticleListAPIView,
    ArticleRateViewSet,
    CategoryDetailAPIView,
    CategoryListAPIView,
    CategorySelectedAPIView,
)
from rest_framework import routers

# from .views import show_categories

router = routers.DefaultRouter()

category_list = CategoryListAPIView.as_view()
category_detail = CategoryDetailAPIView.as_view()
article_list = ArticleListAPIView.as_view()
article_detail = ArticleDetailAPIView.as_view()
main_page_category = CategorySelectedAPIView.as_view({"get": "selected"})
article_rate = ArticleRateViewSet.as_view({"post": "create", "get": "retrieve"})

urlpatterns = [
    path("knowledge_center/", include(router.urls)),
    path("knowledge_center/categories/", category_list, name="category_list"),
    path(
        "knowledge_center/categories/<int:pk>/", category_detail, name="category_detail"
    ),
    path(
        "knowledge_center/selected_categories",
        main_page_category,
        name="main_page_categories",
    ),
    path("knowledge_center/articles/", article_list, name="article_list"),
    path("knowledge_center/articles/<int:pk>/", article_detail, name="article_detail"),
    path("knowledge_center/article_rate/<int:pk>/", article_rate, name="article_rate"),
]
