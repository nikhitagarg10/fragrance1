# Generated by Django 4.0.2 on 2022-04-18 04:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_alter_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 4, 18, 4, 59, 54, 484652, tzinfo=utc)),
        ),
    ]
