# Generated by Django 4.2.5 on 2024-04-28 13:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0004_rename_price_product_p_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="p_price",
            field=models.DecimalField(decimal_places=1, max_digits=30),
        ),
    ]
