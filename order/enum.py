from django.utils.translation import gettext_lazy as _
from enum import Enum

# TODO how add settings here to add other choices??


class OrderStatus(Enum):
    WAITING = _("Waiting")
    CANCEL_BY_USER = _("Cancel by user")
    COMPLETE = _("Complete")
    DELIVER = _("Deliver")
    POST = _("Post")

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
