# Generated by Django 2.0.4 on 2018-05-31 17:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('comicsite', '0020_auto_20180531_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 31, 17, 38, 20, 35264, tzinfo=utc)),
        ),
    ]
