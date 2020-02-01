# Generated by Django 2.2.4 on 2019-09-08 06:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20190908_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 8, 12, 27, 53, 921248)),
        ),
        migrations.AlterField(
            model_name='author',
            name='username',
            field=models.CharField(max_length=25, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='posted_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 8, 12, 27, 53, 921248)),
        ),
    ]