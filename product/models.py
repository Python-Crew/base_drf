from django.db import models
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    title = models.CharField(_("Title"), max_length=40)
    price = models.IntegerField(_("Price"))
    sale_price = models.IntegerField(_("Sale price"))

    def __str__(self):
        return self.title
