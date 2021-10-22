from django.urls import path, include
from .views import *
from rest_framework import routers
from knowledge_center import views

# from .views import show_categories

router = routers.DefaultRouter()
router.register(r"categories", views.CategoryViewSet)
router.register(r"articles", views.ArticleViewSet)


category = views.CategoryViewSet.as_view({"get": "retrieve"})
main_page_category = views.CategoryViewSet.as_view({"get": "selected"})
article = views.ArticleViewSet.as_view({"get": "retrieve"})

urlpatterns = [
    path("knowledge_center/", include(router.urls)),
    path("knowledge_center/categories/", category, name="category_list"),
    path("knowledge_center/categories/<int:pk>/",category, name="category_detail"),
    path("knowledge_center/categories/selected",main_page_category, name="main_page_categories"),
    path("knowledge_center/articles/",article, name="article_list"),
    path("knowledge_center/articles/<int:pk>/",article, name="article_detail"),
]
