# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-21 20:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('start', models.DateTimeField(auto_now=True)),
                ('duration', models.DateTimeField()),
                ('link', models.URLField()),
                ('image', models.ImageField(upload_to=b'')),
            ],
        ),
    ]
