from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import gettext_lazy as _
from django_prices.models import MoneyField
from order.orderstatuses import OrderStatus
from django.db import models
from babel.numbers import list_currencies

CURRENCY_CHOICES = [(currency, currency) for currency in list_currencies()]


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    placement_date = models.DateTimeField(
        _("Placement date"),
    )
    status = models.CharField(_("Status"), choices=OrderStatus.choices, max_length=50)
    currency = models.CharField(max_length=3, default="BTC", choices=CURRENCY_CHOICES)
    price_amount = models.DecimalField(max_digits=9, decimal_places=2, default="5")
    price = MoneyField(amount_field="price_amount", currency_field="currency")
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    def __str__(self):
        return self.user.username
