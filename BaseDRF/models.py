from django.db import models
from django.utils.translation import ugettext as _


class TimestampModel(models.Model):
    created_at = models.DateTimeField(
        _("created at"),
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        _("updated at"),
        auto_now=True
    )
    class Meta:
        abstract = True