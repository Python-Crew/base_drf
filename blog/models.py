import imagekit
from BaseDRF.models import TimestampModel
from django.db import models

from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from mptt.models import MPTTModel, TreeForeignKey
from BaseDRF import settings
from ckeditor_uploader.fields import RichTextUploadingField


class BlogCategory(MPTTModel):
    name = models.CharField(max_length=500, unique=True)
    parent = TreeForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="children"
    )

    class MPTTMeta:
        order_insertion_by = ["name"]

    def __str__(self) -> str:
        return self.name


class Post(TimestampModel):
    title = models.CharField(_("title of post"), max_length=1000, unique=True)
    slug = models.SlugField(
        _("slug of post"), max_length=1000, unique=True, null=True, blank=True
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name=_("author"), on_delete=models.CASCADE
    )
    image = models.ImageField(
        _("title image"), upload_to="PostImages/", null="True", blank="True"
    )
    thumbnail_image = ImageSpecField(
        source="image",
        processors=[ResizeToFill(200, 200)],
        format="webp",
        options={"quality": 60},
    )
    webp_image = ImageSpecField(
        source="image",
        # processors=[ResizeToFill(1280, 720)],
        format="webp",
        options={"quality": 70},
    )
    content = RichTextUploadingField(
        _("content of post, use one just h1 for header in content"),
        blank=True,
        null=True,
    )
    is_published = models.BooleanField(_("can publish post?"))
    category = models.ForeignKey(
        "blog.BlogCategory",
        verbose_name=_("category of post"),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)


class PostComment(TimestampModel, MPTTModel):
    """
    comment of post
    """

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name=_("author"), on_delete=models.CASCADE
    )
    post = models.ForeignKey("blog.Post", verbose_name="post", on_delete=models.CASCADE)
    content = models.TextField(_("text of post"))
    is_published = models.BooleanField(_("can publish comment?"), default=True)
    parent = TreeForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="children"
    )

    def __str__(self) -> str:
        name = str(self.author.username) + "/" + str(self.post.title)
        return name
