# Generated by Django 3.1 on 2021-10-15 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Page",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("url", models.TextField(unique=True, verbose_name="base url")),
                ("redirect_to", models.TextField(verbose_name="redirect url")),
                (
                    "redirect_status",
                    models.IntegerField(
                        blank=True,
                        choices=[
                            (301, "301"),
                            (302, "302"),
                            (303, "303"),
                            (307, "307"),
                            (308, "308"),
                        ],
                        null=True,
                        verbose_name="redirect status code",
                    ),
                ),
                (
                    "operation",
                    models.CharField(
                        blank=True,
                        choices=[("redirect", "redirect"), ("seo_info", "seo_info")],
                        max_length=100,
                        null=True,
                        verbose_name="operation of page",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SocialMeta",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "meta_name_twitter_card",
                    models.TextField(
                        verbose_name="name='twitter:card'#summery_large_image"
                    ),
                ),
                (
                    "meta_name_twitter_label1",
                    models.TextField(
                        verbose_name="name='twitter:label1'#estimate time for read post"
                    ),
                ),
                (
                    "meta_name_twitter_data1",
                    models.TextField(verbose_name="name='twitter:data1'#10 minutes"),
                ),
                (
                    "meta_property_og_title",
                    models.TextField(
                        verbose_name="property='og:title'#main title of page"
                    ),
                ),
                (
                    "meta_property_og_description",
                    models.TextField(
                        verbose_name="property='og:description'#meta description of page"
                    ),
                ),
                (
                    "link_rel_canonical",
                    models.TextField(verbose_name="rel='canonical'#example.com"),
                ),
                (
                    "page",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="seo.page",
                        verbose_name="page instance",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="GenarallMeta",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("head_title", models.TextField(verbose_name="title of head")),
                (
                    "meta_description",
                    models.TextField(verbose_name="description of head"),
                ),
                (
                    "meta_name_robot_follow_type",
                    models.PositiveSmallIntegerField(
                        choices=[(0, "follow"), (1, "nofollow")],
                        default=0,
                        verbose_name="meta name robot follow type",
                    ),
                ),
                (
                    "meta_name_robot_index_type",
                    models.PositiveSmallIntegerField(
                        choices=[(0, "index"), (1, "noindex")],
                        default=0,
                        verbose_name="meta name robot index type",
                    ),
                ),
                (
                    "meta_name_robot_max_image_preview_type",
                    models.PositiveSmallIntegerField(
                        choices=[(0, "non"), (1, "standard"), (2, "large")],
                        default=2,
                        verbose_name="meta name robot max-image-preview type",
                    ),
                ),
                (
                    "page",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="seo.page",
                        verbose_name="page instance",
                    ),
                ),
            ],
        ),
    ]