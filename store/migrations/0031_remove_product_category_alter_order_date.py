# Generated by Django 4.0.2 on 2022-05-15 06:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0030_remove_category_category_remove_product_typee_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 5, 15, 6, 29, 31, 812943, tzinfo=utc)),
        ),
    ]
