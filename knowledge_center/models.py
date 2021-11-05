from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.fields.related import ManyToManyField
from mptt.models import MPTTModel, TreeForeignKey
from django.db.models import Avg


class KnowledgeCenterCategory(MPTTModel):
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


class KnowledgeCenterArticle(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, on_delete=SET_NULL)
    text = models.TextField()
    category = ManyToManyField("KnowledgeCenterCategory")

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"


    @property
    def Avg_rate(self):
        print(self)
        ratings=ArticleRate.objects.filter(article=self)
        return ratings.aggregate(Avg_rate=Avg('rate')).get('Avg_rate')


class ArticleRate(models.Model):
    article = models.ForeignKey(
        KnowledgeCenterArticle, on_delete=CASCADE)
    rate = models.FloatField(null=True, blank=True)
