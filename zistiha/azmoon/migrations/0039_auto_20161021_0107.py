# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-20 21:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('azmoon', '0038_auto_20161021_0103'),
    ]

    operations = [
        migrations.RenameField(
            model_name='examorder',
            old_name='ordersnumber',
            new_name='examsnumber',
        ),
    ]
