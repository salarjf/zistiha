# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-20 21:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('azmoon', '0037_remove_bonus_used_flag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='examorder',
            old_name='examsnumber',
            new_name='ordersnumber',
        ),
    ]