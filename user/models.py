from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.core.mail import send_mail
from BaseDRF.settings import OTP_EXPIRE_TIME

from pyotp import TOTP, random_base32


class UserManager(BaseUserManager):
    def create_user(self, username, email, phone_no, password, **extra_fields):
        if not email and not phone_no:
            raise ValueError("Eigther email or phone_no must be set")

        if not email:
            email = None
        if not phone_no:
            phone_no = None

        if not username:
            if email:
                username = email
            if phone_no:
                username = phone_no

        user = self.model(
            username=username, email=email, phone_no=phone_no, **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, phone_no, password, **extra_fields):
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(username, email, phone_no, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)

    username = models.CharField(unique=True, max_length=45, null=True, blank=True)
    email = models.CharField(unique=True, max_length=45, null=True, blank=True)
    phone_no = models.CharField(unique=True, max_length=45, null=True, blank=True)

    # used for hashing
    key = models.CharField(max_length=40, blank=True, default=random_base32)

    date_joined = models.DateTimeField(default=timezone.now, editable=False)
    is_active = models.BooleanField(default=False)
    is_valid = models.BooleanField(default=False)

    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "phone_no"]

    objects = UserManager()

    class Meta:
        db_table = "users"

    def clean(self):
        cleaned_data = super().clean()
        if not self.email and not self.phone_no:
            raise ValidationError(
                {
                    "email": "Eigther email or phone_no must be set",
                    "phone_no": "Eigther email or phone_no must be set",
                }
            )

    def verify_otp(self, otp):
        if not self.key or not otp:
            return False

        try:
            delta = self.otp.delta_time
        except:
            delta = 0

        return TOTP(self.key, interval=OTP_EXPIRE_TIME).verify(
            otp, for_time=int(timezone.now().timestamp()) - delta
        )

    def sendOTP(self, otp, **params):
        if self.email:
            send_mail(
                "BaseDRF activation code",
                f"your activation code is {otp}",
                "bshadmehr76@gmail.com",
                [self.email],
                fail_silently=False,
            )
