# Generated by Django 2.2.4 on 2019-09-08 09:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20190908_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 8, 9, 23, 35, 314708, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='posted_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 8, 9, 23, 35, 314708, tzinfo=utc)),
        ),
    ]
