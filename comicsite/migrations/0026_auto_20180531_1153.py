# Generated by Django 2.0.4 on 2018-05-31 18:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('comicsite', '0025_auto_20180531_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favoritecomics',
            name='comicid',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 31, 18, 53, 20, 565357, tzinfo=utc)),
        ),
    ]