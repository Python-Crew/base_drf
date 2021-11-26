from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from user.views import MyTokenObtainPairView

from django.views.decorators.csrf import csrf_exempt
from blog.views import MyImageUploadView

from rest_framework import routers

router = routers.DefaultRouter()


urlpatterns = (
    [
        path("admin/", admin.site.urls),
        path("auth/", include("auth_user.urls")),
        path("blog/", include("blog.urls")),
        path("api-auth/", include("rest_framework.urls")),
        path("api/token/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
        path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
        path(
            "ckeditor/upload/",
            csrf_exempt(MyImageUploadView.as_view()),
            name="ckeditor_upload",
        ),
        path("ckeditor/", include("ckeditor_uploader.urls")),
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
