from django.contrib.auth.models import Permission
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.generics import CreateAPIView
from .serializers import NotificationInputsSerializer
class Notification(CreateAPIView):
    serializer_class = NotificationInputsSerializer
    # Permission_classes = ?
    def perform_create(self, serializer):
        return super().perform_create(serializer) 
