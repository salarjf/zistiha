# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-16 08:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('azmoon', '0033_bonus_used'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseorder',
            name='rest_money',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='courseorder',
            name='should_pay',
            field=models.FloatField(default=0),
        ),
    ]
