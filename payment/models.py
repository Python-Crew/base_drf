from django.db import models
from django.utils.translation import gettext_lazy as _
import importlib
from django.conf import settings
from django.contrib.contenttypes.models import ContentType


if getattr(settings, "PAYMENT_STATUSES", None) is not None:
    package, attr = settings.PAYMENT_STATUSES.rsplit(".", 1)
    PaymentStatus = getattr(importlib.import_module(package), attr)
else:
    from payment.banks.paymentstatuses import PaymentStatus

if getattr(settings, "BANK_TYPE", None) is not None:
    package, attr = settings.BANK_TYPE.rsplit(".", 1)
    BankType = getattr(importlib.import_module(package), attr)
else:
    from payment.banks.paymentstatuses import BankType


class PaymentRecord(models.Model):
    order = models.ForeignKey(
        "order.Order",
        on_delete=models.CASCADE,
        related_name="payment_record",
        verbose_name=_("Order"),
    )
    status = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        choices=PaymentStatus.choices,
        verbose_name=_("Status"),
    )
    bank_type = models.CharField(
        max_length=50,
        choices=BankType.choices,
        verbose_name=_("Bank"),
    )
    amount = models.CharField(
        max_length=10, null=False, blank=False, verbose_name=_("Amount")
    )
    # Reference number return from bank
    transaction_code = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        verbose_name=_("Transaction code"),
    )
    response_result = models.TextField(
        null=True, blank=True, verbose_name=_("Bank result")
    )
    callback_url = models.TextField(
        null=False, blank=False, verbose_name=_("Callback url")
    )
    extra_information = models.TextField(
        null=True, blank=True, verbose_name=_("Extra information")
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )
    update_at = models.DateTimeField(
        auto_now=True,
        editable=False,
    )

    class Meta:
        verbose_name = _("Payment record")
        verbose_name_plural = _("Payment records")

    def __str__(self):
        return "{}-{}".format(self.pk, self.transaction_code)
