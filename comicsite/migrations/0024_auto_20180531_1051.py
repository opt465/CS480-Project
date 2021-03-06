# Generated by Django 2.0.4 on 2018-05-31 17:51

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('comicsite', '0023_auto_20180531_1050'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavoriteComics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comicid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comicsite.Comic')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'fav_comic',
                'managed': True,
            },
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 31, 17, 51, 3, 686541, tzinfo=utc)),
        ),
    ]
