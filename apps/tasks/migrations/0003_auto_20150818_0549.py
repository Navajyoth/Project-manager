# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_technology'),
        ('tasks', '0002_auto_20150817_0628'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='actual_time',
            field=models.PositiveSmallIntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='task',
            name='estimated_time',
            field=models.PositiveSmallIntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='task',
            name='rework_time',
            field=models.PositiveSmallIntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='task',
            name='technology',
            field=models.ForeignKey(related_name='tasks', blank=True, to='core.Technology', null=True),
        ),
    ]
