from django.utils.translation import gettext_lazy as _
from django.db import models


class OrderStatus(models.TextChoices):
    WAITING_FOR_PAYMENT = "waiting_for_payment", _("Waiting for payment")
    FAILED_PAYMENT = "failed_payment", _("Failed payment")
    CANCEL_ORDER_BY_USER = "cancel_order_by_user", _("Cancel order by user")
    PAID = "paid", _("Paid")
    DELIVER = "deliver", _("Deliver")
    POST = "post", _("Post")


class CurrencyEnum(models.TextChoices):
    IRR = "IRR", _("Rial")
    IRT = "IRT", _("Toman")
    CAD = "cad", _("Canada dollar")

    @classmethod
    def rial_to_toman(cls, amount):
        return amount / 10

    @classmethod
    def toman_to_rial(cls, amount):
        return amount * 10
