# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-27 20:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('azmoon', '0012_auto_20160923_1335'),
    ]

    operations = [
        migrations.AddField(
            model_name='examsubmition',
            name='submitted',
            field=models.CharField(default='salam', max_length=500),
        ),
    ]