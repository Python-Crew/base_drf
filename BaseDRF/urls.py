from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from user.views import MyTokenObtainPairView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("auth_user.urls")),
    path("api/token/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
