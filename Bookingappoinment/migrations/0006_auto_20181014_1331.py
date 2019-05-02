# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-10-14 11:31
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0005_auto_20181013_2339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookappointment',
            name='appointments',
        ),
        migrations.AddField(
            model_name='appointment',
            name='file_number',
            field=models.CharField(default=datetime.datetime(2018, 10, 14, 11, 31, 1, 184566, tzinfo=utc), max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appointment',
            name='is_doctor',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='appointment',
            name='time',
            field=models.CharField(default=datetime.datetime(2018, 10, 14, 11, 31, 12, 56458, tzinfo=utc), max_length=250),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='BookAppointment',
        ),
    ]