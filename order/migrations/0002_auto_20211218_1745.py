# Generated by Django 3.1 on 2021-12-18 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="currency",
            field=models.CharField(
                choices=[("IRR", "Rial"), ("IRT", "Toman"), ("cad", "Canada dollar")],
                max_length=50,
                verbose_name="Currency",
            ),
        ),
    ]
