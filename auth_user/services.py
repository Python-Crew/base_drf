from user.models import User
from rest_framework import exceptions


def get_user(username):
    user = None

    if "@" in username:
        try:
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            user = User.objects.create(username=username, email=username)
    elif username.isdigit():
        try:
            user = User.objects.get(phone_no=username)
        except User.DoesNotExist:
            user = User.objects.create(username=username, phone_no=username)
    else:
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise exceptions.NotFound("User matching username was not found!")

    return user
