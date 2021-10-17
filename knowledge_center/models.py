from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    title = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="children",
    )
    main_page_category = models.BooleanField(default=False)

    class MPTTMeta:
        order_insertion_by = ["title"]

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
