# Generated by Django 4.0.2 on 2022-04-20 17:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_order_status_alter_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 4, 20, 17, 15, 53, 972768, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(default='received', max_length=50),
        ),
    ]
