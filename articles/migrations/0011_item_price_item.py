# Generated by Django 2.2.7 on 2019-12-13 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0010_remove_item_price_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='price_item',
            field=models.FloatField(default=0, verbose_name='Стоимость вещи'),
        ),
    ]
