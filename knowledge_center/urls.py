from django.urls import path
from .views import *
from .views import show_categories



urlpatterns = [
    path('categories/', show_categories),
]