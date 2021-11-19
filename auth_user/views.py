from django.http.response import JsonResponse
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
        return TOTP(user.key, interval=OTP_EXPIRE_TIME).at(now)

    @action(
        methods=["post"],
        detail=False,
        serializer_class=SendOTPSerializer,
        url_name="send-otp"
    )
    def send_otp(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = get_user(serializer.validated_data["username"])
            otp = self.__class__.generate_otp(user)
            user.sendOTP(otp=otp)
            if settings.DEBUG:
                return Response({"otp": otp})
            return Response("sent")
        return JsonResponse(serializer.errors, status=400)

    @action(
        methods=["post"],
        detail=False,
        permission_classes=[IsAuthenticated],
    )
    def sample_auth(self, request, *args, **kwargs):
        print(request.user.phone_no)
        return Response("sent")
