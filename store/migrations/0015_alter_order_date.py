# Generated by Django 4.0.2 on 2022-04-20 17:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_alter_order_date_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 4, 20, 17, 27, 54, 786575, tzinfo=utc)),
        ),
    ]
