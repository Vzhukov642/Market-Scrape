# Generated by Django 2.2.7 on 2019-12-20 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0015_auto_20191220_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price_item',
            field=models.FloatField(db_index=True, max_length=10, verbose_name='Стоимость вещи'),
        ),
    ]
