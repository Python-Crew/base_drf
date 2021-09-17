from auth_user.services import (
    get_user,
)
from django.conf import settings
from django.utils import timezone
from BaseDRF.settings import OTP_EXPIRE_TIME
from pyotp import TOTP
from rest_framework import response
from rest_framework.authtoken.views import Token
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from user.models import User

from .serializers import (
    SendOTPSerializer,
)


class AuthViewSet(GenericViewSet):
    permission_classes = []

    @staticmethod
    def generate_otp(user: User) -> str:
        now = int(timezone.now().timestamp())
        print(OTP_EXPIRE_TIME)
        print(TOTP(user.key, interval=OTP_EXPIRE_TIME).at(now))
        return TOTP(user.key, interval=OTP_EXPIRE_TIME).at(now)

    @action(
        methods=["post"],
        detail=False,
        serializer_class=SendOTPSerializer,
    )
    def send_otp(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = get_user(serializer.validated_data["username"])
        print(user)
        otp = self.__class__.generate_otp(user)
        user.sendOTP(otp=otp)
        if settings.DEBUG:
            return Response({"otp": otp})
        return Response("sent")
