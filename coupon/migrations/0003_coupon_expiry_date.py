# Generated by Django 5.0.2 on 2024-04-16 11:58

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("coupon", "0002_remove_coupon_is_available"),
    ]

    operations = [
        migrations.AddField(
            model_name="coupon",
            name="expiry_date",
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
