from django.db import models
from django.conf import settings
from mptt.models import MPTTModel, TreeForeignKey
from django.core.validators import MaxValueValidator, MinValueValidator


class Knowledge_Center_Category(MPTTModel):
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


class Knowledge_Center_Article(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    category = models.ManyToManyField(Knowledge_Center_Category)
    rate = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)]
    )

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
