# Generated by Django 4.2.2 on 2023-06-23 17:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("restaurants", "0013_alter_restaurants_items"),
    ]

    operations = [
        migrations.AlterField(
            model_name="restaurants",
            name="full_details",
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name="restaurants",
            name="items",
            field=models.TextField(null=True),
        ),
    ]
