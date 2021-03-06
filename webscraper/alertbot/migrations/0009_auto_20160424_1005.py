# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-24 10:05
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alertbot', '0008_auto_20160417_0659'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alert',
            old_name='actual_price',
            new_name='act_price',
        ),
        migrations.RenameField(
            model_name='alert',
            old_name='expected_price',
            new_name='exp_from',
        ),
        migrations.AddField(
            model_name='alert',
            name='exp_to',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='mobile',
            field=models.CharField(db_index=True, max_length=10, unique=True, validators=[django.core.validators.MinLengthValidator(10), django.core.validators.RegexValidator('^[789]\\d{9}$', 'Invalid mobile number.')]),
        ),
    ]
