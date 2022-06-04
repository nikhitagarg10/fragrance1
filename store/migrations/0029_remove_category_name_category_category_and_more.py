# Generated by Django 4.0.2 on 2022-05-15 04:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0028_rename_type_product_typee_alter_order_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='name',
        ),
        migrations.AddField(
            model_name='category',
            name='category',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 5, 15, 4, 43, 32, 112125, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='product',
            name='typee',
            field=models.IntegerField(choices=[(1, 'Woody'), (2, 'Floral'), (3, 'Oriental'), (4, 'Fresh'), (5, 'Celebrity Scents')], null=True),
        ),
    ]
