# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-13 17:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_problem_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institution',
            name='status',
            field=models.IntegerField(blank=True, choices=[(1, 'active'), (0, 'passive'), (None, 'unknown')], help_text='active or passive', null=True),
        ),
        migrations.AlterField(
            model_name='institutionproblem',
            name='status',
            field=models.IntegerField(blank=True, choices=[(2, 'resolved'), (1, 'ignored'), (0, 'started'), (None, 'unknown')], help_text='active or passive', null=True),
        ),
        migrations.AlterField(
            model_name='problem',
            name='status',
            field=models.IntegerField(blank=True, choices=[(1, 'active'), (0, 'passive'), (None, 'unknown')], help_text='state in which our problem is currently', null=True),
        ),
    ]
