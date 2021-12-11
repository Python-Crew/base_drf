from django.conf import settings
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from order.enum import OrderStatus
from django.utils.translation import gettext_lazy as _


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)
    placement_date = models.DateTimeField(
        _("Placement date"),
    )
    status = models.CharField(_("status"), choices=OrderStatus.choices(), max_length=30)

    def __str__(self):
        return self.user.username


class OrderLine(models.Model):
    order = models.ForeignKey("order.Order", on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")
    quantity = models.IntegerField(default=1)

    def save(self, **kwargs):
        if self.quantity == 0:
            self.delete()

    # TODO how set total price or sale price???
