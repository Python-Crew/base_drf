from django.utils.translation import gettext_lazy as _
from django.db import models


class OrderStatus(models.TextChoices):
    WAITING = "waiting", _("Waiting")
    CANCEL_BY_USER = "cancel_by_user", _("Cancel by user")
    COMPLETE = "complete", _("Complete")
    DELIVER = "deliver", _("Deliver")
    POST = "post", _("Post")
