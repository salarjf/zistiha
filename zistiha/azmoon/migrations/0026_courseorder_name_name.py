# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-13 14:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('azmoon', '0025_courseorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseorder',
            name='name_name',
            field=models.CharField(default='None', max_length=20),
        ),
    ]
