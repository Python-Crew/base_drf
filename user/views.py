from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .serializers import MyTokenObtainPairSerializer
from django.shortcuts import render


class MyTokenObtainPairView(TokenObtainPairView):
    def get_serializer_class(self):
        return MyTokenObtainPairSerializer
