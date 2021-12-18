from django.conf import settings
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import gettext_lazy as _
from order.orderstatuses import OrderStatus, CurrencyEnum


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    placement_date = models.DateTimeField(
        _("Placement date"),
    )
    status = models.CharField(_("Status"), choices=OrderStatus.choices, max_length=50)
    currency = models.CharField(
        _("Currency"), choices=CurrencyEnum.choices, max_length=50
    )
    amount = models.IntegerField(_("Amount"))
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    def __str__(self):
        return self.user.username
