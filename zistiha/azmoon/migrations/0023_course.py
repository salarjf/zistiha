# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-13 12:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('azmoon', '0022_delete_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('Description', models.TextField(verbose_name='nothing!')),
                ('cost', models.IntegerField(default=0)),
                ('start', models.DateTimeField()),
            ],
        ),
    ]
