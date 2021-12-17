# Generated by Django 3.1 on 2021-12-17 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="amount",
            field=models.IntegerField(default=22, verbose_name="Amount"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="order",
            name="status",
            field=models.CharField(
                choices=[
                    ("waiting_for_payment", "Waiting for payment"),
                    ("failed_payment", "Failed payment"),
                    ("cancel_order_by_user", "Cancel order by user"),
                    ("complete", "Complete"),
                    ("deliver", "Deliver"),
                    ("post", "Post"),
                ],
                max_length=50,
                verbose_name="Status",
            ),
        ),
    ]
