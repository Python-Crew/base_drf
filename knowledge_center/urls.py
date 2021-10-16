from django.urls import path, include
from .views import *
from rest_framework import routers
from knowledge_center import views
# from .views import show_categories

router = routers.DefaultRouter()
router.register(r'categories', views.CategoryViewSet)


category = views.CategoryViewSet.as_view({
    'get': 'retrieve',
})

urlpatterns = [
    path('faq/', include(router.urls)),
    path('faq/categories/', category, name='category_list'),
    path('faq/categories/<int:pk>/', category, name='category_detail'),
]
