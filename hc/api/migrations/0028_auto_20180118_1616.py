# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-18 16:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0027_auto_20180118_1147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='check',
            name='nag_mode',
        ),
        migrations.AlterField(
            model_name='check',
            name='status',
            field=models.CharField(choices=[('up', 'Up'), ('down', 'Down'), ('new', 'New'), ('paused', 'Paused')], default='new', max_length=6),
        ),
    ]