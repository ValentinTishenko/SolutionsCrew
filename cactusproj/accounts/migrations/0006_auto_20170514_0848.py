# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-14 08:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20170514_0845'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LikedFund',
            new_name='LikedProblem',
        ),
    ]
