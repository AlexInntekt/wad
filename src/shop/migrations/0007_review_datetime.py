# Generated by Django 2.2 on 2020-05-17 11:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_review_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 17, 11, 12, 58, 46263)),
        ),
    ]
