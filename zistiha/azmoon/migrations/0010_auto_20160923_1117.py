# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-23 11:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('azmoon', '0009_auto_20160923_1114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='examsubmition',
            name='seckey',
        ),
        migrations.AddField(
            model_name='examsubmition',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='azmoon.ExamOrder'),
        ),
    ]