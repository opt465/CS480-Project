# Generated by Django 2.0.4 on 2018-06-01 01:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('comicsite', '0029_auto_20180531_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 1, 1, 19, 47, 78788, tzinfo=utc)),
        ),
    ]
