import importlib
from django.conf import settings
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import gettext_lazy as _

if getattr(settings, "ORDER_STATUSES", None) is not None:
    from BaseDRF.settings import ORDER_STATUSES
    package, attr = ORDER_STATUSES.rsplit(".", 1)
    module = importlib.import_module(package)
    OrderStatus = getattr(module, attr)
else:
    from order.statuses import OrderStatus


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)
    placement_date = models.DateTimeField(
        _("Placement date"),
    )
    status = models.CharField(_("status"), choices=OrderStatus.choices, max_length=30)
    bank_type = models.CharField(
        max_length=50,
        verbose_name=_("Bank"),
    )
    # It's local and generate locally
    tracking_code = models.CharField(
        max_length=255, null=False, blank=False, verbose_name=_("Tracking code")
    )
    # Reference number return from bank
    reference_number = models.CharField(
        unique=True,
        max_length=255,
        null=False,
        blank=False,
        verbose_name=_("Reference number"),
    )
    response_result = models.TextField(
        null=True, blank=True, verbose_name=_("Bank result")
    )
    extra_information = models.TextField(
        null=True, blank=True, verbose_name=_("Extra information")
    )

    def __str__(self):
        return self.user.username
