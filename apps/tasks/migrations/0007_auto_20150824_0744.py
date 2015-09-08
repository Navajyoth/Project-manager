# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_auto_20150824_0634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='actual_time',
            field=models.DecimalField(null=True, max_digits=3, decimal_places=1, blank=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='estimated_time',
            field=models.DecimalField(null=True, max_digits=3, decimal_places=1, blank=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='rework_time',
            field=models.DecimalField(null=True, max_digits=3, decimal_places=1, blank=True),
        ),
    ]
