from django.db import models
from django.utils.translation import ugettext as _

from .utils import delete_space_and_slash


class Page(models.Model):
    url = models.TextField(_("base url"), unique=True)
    redirect_to = models.TextField(_("redirect url"))

    REDIRECT_STATUS_301 = 301
    REDIRECT_STATUS_302 = 302
    REDIRECT_STATUS_303 = 303
    REDIRECT_STATUS_307 = 307
    REDIRECT_STATUS_308 = 308
    REDIRECT_STATUS_TYPE = (
        (REDIRECT_STATUS_301, "301:Permanent, Cacheable, Request GET/POST may change"),
        (
            REDIRECT_STATUS_302,
            "302:Temporary, not Cacheable by default, Request GET/POST may change",
        ),
        (REDIRECT_STATUS_303, "303:Temporary, never Cacheable, Request always GET"),
        (
            REDIRECT_STATUS_307,
            "307:Temporary, not Cacheable by default, Request may not change",
        ),
        (
            REDIRECT_STATUS_308,
            "308:Permanent, by default Cacheable, Request may not change",
        ),
    )
    redirect_status = models.IntegerField(
        _("redirect status code"),
        null=True, blank=True,
        choices=REDIRECT_STATUS_TYPE
    )

    OPERATION_REDIRECT = "redirect"
    OPERATION_INCLUDE_SEO_INFO = "seo_info"
    OPERATIONCHOICE = (
        (OPERATION_REDIRECT, "operation redirect"),
        (OPERATION_INCLUDE_SEO_INFO, "operation include SEO info"),
    )
    operation = models.CharField(
        _("operation of page"),
        max_length=100,
        choices=OPERATIONCHOICE,
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return super().__str__()

    def save(self, *args, **kwargs):
        self.url = delete_space_and_slash(self.url)
        self.redirect_to = delete_space_and_slash(self.redirect_to)
        super(Page, self).save(*args, **kwargs)


class SocialMeta(models.Model):
    page = models.OneToOneField(
        "seo.Page", on_delete=models.CASCADE, verbose_name=_("page instance")
    )
    meta_name_twitter_card = models.TextField(
        _("name='twitter:card'#summery_large_image")
    )
    meta_name_twitter_label1 = models.TextField(
        _("name='twitter:label1'#estimate time for read post")
    )
    meta_name_twitter_data1 = models.TextField(_("name='twitter:data1'#10 minutes"))
    meta_property_og_title = models.TextField(
        _("property='og:title'#main title of page")
    )
    meta_property_og_description = models.TextField(
        _("property='og:description'#meta description of page")
    )
    link_rel_canonical = models.TextField(_("rel='canonical'#example.com"))


class GenarallMeta(models.Model):
    page = models.OneToOneField(
        "seo.Page", on_delete=models.CASCADE, verbose_name=_("page instance")
    )
    head_title = models.TextField(
        _("title of head"),
    )
    meta_description = models.TextField(
        _("description of head"),
    )
    META_NAME_ROBOTS_FOLLOW = 0
    META_NAME_ROBOTS_NOFOLOW = 1
    META_NAME_ROBOTS_FOLOW_TYPE = (
        (META_NAME_ROBOTS_FOLLOW, "follow"),
        (META_NAME_ROBOTS_NOFOLOW, "nofollow"),
    )
    meta_name_robot_follow_type = models.PositiveSmallIntegerField(
        _("meta name robot follow type"), choices=META_NAME_ROBOTS_FOLOW_TYPE, default=0
    )
    META_NAME_ROBOTS_INDEX = 0
    META_NAME_ROBOTS_NOINDEX = 1
    META_NAME_ROBOTS_INDEX_TYPE = (
        (META_NAME_ROBOTS_INDEX, "index"),
        (META_NAME_ROBOTS_NOINDEX, "noindex"),
    )
    meta_name_robot_index_type = models.PositiveSmallIntegerField(
        _("meta name robot index type"), choices=META_NAME_ROBOTS_INDEX_TYPE, default=0
    )
    META_NAME_ROBOTS_MAX_IMAGE_PREVIEW_NONE = 0
    META_NAME_ROBOTS_MAX_IMAGE_PREVIEW_STANDARD = 1
    META_NAME_ROBOTS_MAX_IMAGE_PREVIEW_LARGE = 2
    META_NAME_ROBOTS_MAX_IMAGE_PREVIEW_TYPE = (
        (META_NAME_ROBOTS_MAX_IMAGE_PREVIEW_NONE, "non"),
        (META_NAME_ROBOTS_MAX_IMAGE_PREVIEW_STANDARD, "standard"),
        (META_NAME_ROBOTS_MAX_IMAGE_PREVIEW_LARGE, "large"),
    )
    meta_name_robot_max_image_preview_type = models.PositiveSmallIntegerField(
        _("meta name robot max-image-preview type"),
        choices=META_NAME_ROBOTS_MAX_IMAGE_PREVIEW_TYPE,
        default=2,
    )

    def __str__(self) -> str:
        return "header of: " + self.head_title
