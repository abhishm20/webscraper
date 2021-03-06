# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-11 05:19
from __future__ import unicode_literals

import alertbot.models
import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('alertbot', '0002_auto_20160410_1831'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actual_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('expected_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('url', models.CharField(max_length=1000)),
                ('name', models.CharField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alertbot.User')),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(default=alertbot.models.get_random_token, max_length=500)),
                ('ttl', models.DateTimeField(default=datetime.datetime(2016, 4, 11, 5, 29, 38, 181789, tzinfo=utc))),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alertbot.User')),
            ],
        ),
    ]
