from django.utils.translation import gettext_lazy as _
from django.db import models


class PaymentStatus(models.TextChoices):
    FAILED = _("Failed")
    REDIRECT_TO_BANK = _("Redirect to bank")
    COMPLETE = _("Complete")


class BankType(models.TextChoices):
    ZIBAL = "ZIBAL", _("Zibal")
    STRIPE = "STRIPE", _("Stripe")
