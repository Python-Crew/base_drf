from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes.models import ContentType
from payment.banks.paymentstatuses import PaymentStatus
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
    amount = models.DecimalField(
        max_digits=9, decimal_places=2, default="5", verbose_name=_("Amount")
    )

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
