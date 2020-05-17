# Generated by Django 2.2 on 2020-05-17 22:57

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20200517_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoryimage',
            name='category',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='shop.Category'),
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='shop.Category'),
        ),
        migrations.AlterField(
            model_name='review',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 17, 22, 57, 33, 318787)),
        ),
    ]
