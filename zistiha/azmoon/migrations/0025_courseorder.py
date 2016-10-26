# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-13 12:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('azmoon', '0024_auto_20161013_1617'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=20)),
                ('school_type', models.CharField(default='unknown', max_length=30)),
                ('school_name', models.CharField(default='unknown', max_length=30)),
                ('city', models.CharField(default='unknown', max_length=30)),
                ('provinence', models.CharField(default='unknown', max_length=30)),
                ('parent_phone', models.CharField(max_length=20)),
                ('payment_type', models.CharField(default='once', max_length=10)),
                ('rest_money', models.IntegerField(default=0)),
                ('order_date', models.DateTimeField(auto_now=True)),
                ('Bonus', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='azmoon.Bonus')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='azmoon.Course')),
            ],
        ),
    ]
