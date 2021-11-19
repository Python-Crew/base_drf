from django.core.mail import message
from django.urls import reverse
import pytest
from user.models import User
from unittest.mock import patch

send_otp_url = reverse("auth-user:auth-user-send-otp")

def test_sending_user_otp_code_without_username_should_fail(client) -> None:
    response = client.post(send_otp_url)
    assert response.status_code == 400


@pytest.mark.django_db
def test_sending_user_otp_code_with_none_existance_phoneno_create_user(client) -> None:
    response = client.post(send_otp_url, data={"username": "09388309605"})
    users = User.objects.filter(phone_no="09388309605")
    assert users.count() == 1
    assert users.first().phone_no == "09388309605"


@pytest.mark.django_db
def test_sending_user_otp_code_with_none_existance_email_create_user(client) -> None:
    response = client.post(send_otp_url, data={"username": "bshadmehr76@gmail.com"})
    users = User.objects.filter(email="bshadmehr76@gmail.com")
    assert users.count() == 1
    assert users.first().email == "bshadmehr76@gmail.com"


@pytest.mark.django_db
def test_sending_user_otp_code_with_none_existance_email_sends_email(settings, client) -> None:
    settings.DEBUG = True
    with patch("user.models.send_mail") as mocked_send_otp_email:
        response = client.post(send_otp_url, data={"username": "bshadmehr76@gmail.com"})
        users = User.objects.filter(email="bshadmehr76@gmail.com")
        assert users.count() == 1
        assert users.first().email == "bshadmehr76@gmail.com"

        otp = response.json()["otp"]

        mocked_send_otp_email.assert_called_once_with(
            subject="BaseDRF activation code",
            message=f"your activation code is {otp}",
            from_email="bshadmehr76@gmail.com",
            recipient_list=["bshadmehr76@gmail.com"],
            fail_silently=False
        )


@pytest.mark.django_db
def test_sending_user_otp_code_with_username_should_fail(client) -> None:
    response = client.post(send_otp_url, data={"username": "bshadmehr76"})
    users = User.objects.filter(username="bshadmehr76")
    assert response.status_code == 404
    assert users.count() == 0
