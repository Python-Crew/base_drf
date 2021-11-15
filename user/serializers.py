from rest_framework import serializers, exceptions
from django.contrib.auth import authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User
from django.contrib.auth.models import update_last_login
from rest_framework_simplejwt.settings import api_settings as simplejwt_api_settings


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        try:
            request = self.context["request"]
        except KeyError:
            pass

        try:
            if "@" in request.data.get("username"):
                self.user = User.objects.get(email=request.data.get("username"))
            elif request.data.get("username").isdigit():
                self.user = User.objects.get(phone_no=request.data.get("username"))
            else:
                self.user = User.objects.get(username=request.data.get("username"))
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed(
                self.error_messages["no_active_account"],
                "no_active_account",
            )

        if self.user.check_password(request.data.get("password")):
            pass
        elif self.user.verify_otp(request.data.get("password")):
            pass
        else:
            raise exceptions.AuthenticationFailed(
                self.error_messages["no_active_account"],
                "no_active_account",
            )

        if not simplejwt_api_settings.USER_AUTHENTICATION_RULE(self.user):
            raise exceptions.AuthenticationFailed(
                self.error_messages["no_active_account"],
                "no_active_account",
            )

        data = {}

        refresh = self.get_token(self.user)

        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)

        if simplejwt_api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return data
