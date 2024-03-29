# Generated by Django 4.0.2 on 2022-05-29 11:33

import datetime
import django.core.validators
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0040_rate_order_alter_order_date_alter_order_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 5, 29, 11, 33, 37, 99158, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='rate',
            name='rating',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
