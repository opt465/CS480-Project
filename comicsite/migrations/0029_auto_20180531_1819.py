# Generated by Django 2.0.4 on 2018-06-01 01:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('comicsite', '0028_auto_20180531_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follow',
            name='following',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 1, 1, 19, 41, 89039, tzinfo=utc)),
        ),
    ]
