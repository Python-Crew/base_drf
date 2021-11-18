from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import AuthViewSet

router = DefaultRouter()
router.register("", AuthViewSet, "auth-user")

urlpatterns = router.urls
