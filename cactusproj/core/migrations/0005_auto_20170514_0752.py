# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-14 07:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20170514_0750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='name',
            field=models.CharField(default='some_name', max_length=256),
        ),
    ]
