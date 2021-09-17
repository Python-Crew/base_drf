from user.models import User
from rest_framework import authentication
from rest_framework import exceptions


class EmailAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        email = request.data.get("username")
        password = request.data.get("password")

        try:
            user = User.objects.get(email=email)
            if not user.check_password(password):
                return None, None
        except User.DoesNotExist:
            return None, None

        return user, None


class PhoneNoAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        phone_no = request.data.get("username")
        password = request.data.get("password")

        try:
            user = User.objects.get(email=phone_no)
            if not user.check_password(password):
                return None, None
        except User.DoesNotExist:
            return None, None

        return user, None
