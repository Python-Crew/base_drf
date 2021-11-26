from django.urls import path
from . import views
from rest_framework import routers

router = routers.SimpleRouter()

router.register(r"blog-category", views.BlogCategoryViewSet, basename="blog_category")
router.register(r"post", views.PostModelViewSet, basename="post")
router.register(r"post-comment", views.PostComment, basename="post_comment")

urlpatterns = router.urls
