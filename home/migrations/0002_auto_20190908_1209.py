# Generated by Django 2.2.4 on 2019-09-08 06:39

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='author',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 8, 12, 9, 8, 320025)),
        ),
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('content', models.TextField()),
                ('posted_on', models.DateTimeField(default=datetime.datetime(2019, 9, 8, 12, 9, 8, 320025))),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Author')),
            ],
        ),
    ]