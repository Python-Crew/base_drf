from django.utils.translation import gettext_lazy as _
from django.db import models


class PaymentStatus(models.TextChoices):
    WAITING = _("Waiting")
    FAILED = _("Failed")
    REDIRECT_TO_BANK = _("Redirect to bank")
    RETURN_FROM_BANK = _("Return from bank")
    CANCEL_BY_USER = _("Cancel by user")
    EXPIRE_GATEWAY_TOKEN = _("Expire gateway token")
    EXPIRE_VERIFY_PAYMENT = _("Expire verify payment")
    COMPLETE = _("Complete")


class BankType(models.TextChoices):
    ZIBAL = "ZIBAL", _("Zibal")
