from django.db.models.fields import EmailField
from rest_framework import serializers, exceptions
from rest_framework.authtoken.serializers import AuthTokenSerializer


class SendOTPSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
