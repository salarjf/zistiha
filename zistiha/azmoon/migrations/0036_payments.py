# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-16 19:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('azmoon', '0035_examorder_examsnumber'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50)),
            ],
        ),
    ]
