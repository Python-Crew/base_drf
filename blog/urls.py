from django.urls import path
from . import views
from rest_framework import routers

router = routers.SimpleRouter()

router.register(r"blog-category", views.BlogCategoryViewSet)
router.register(r"post", views.PostModelViewSet)
router.register(r"post-comment", views.PostComment)

urlpatterns = [] + router.urls
