from user.models import User


def get_user(username):
    user = None

    try:
        if "@" in username:
            user = User.objects.get(email=username)
        elif username.isdigit():
            user = User.objects.get(phone_no=username)
        else:
            user = User.objects.get(username=username)
    except User.DoesNotExist:
        pass

    return user
