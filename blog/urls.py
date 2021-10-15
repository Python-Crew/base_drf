from django.urls import path
from . import views
from rest_framework import routers

router = routers.SimpleRouter()

router.register(r"post", views.PostModelViewSet)

urlpatterns = [
] + router.urls