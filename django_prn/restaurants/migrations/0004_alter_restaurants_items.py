# Generated by Django 4.2.2 on 2023-06-23 13:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "restaurants",
            "0003_remove_restaurants_items_data_restaurants_items_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="restaurants",
            name="items",
            field=models.TextField(),
        ),
    ]
