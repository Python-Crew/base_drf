from django.core import mail


def test_send_email_should_succeed(settings, mailoutbox) -> None:
    settings.EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"

    assert len(mailoutbox) == 0
    mail.send_mail(
        subject="Test",
        message="Test",
        from_email="sample@sample.com",
        recipient_list=["sample@sample.com"],
        fail_silently=False
    )

    assert len(mailoutbox) == 1
    assert mailoutbox[0].subject == "Test"
