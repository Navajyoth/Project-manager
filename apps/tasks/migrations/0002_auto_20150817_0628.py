# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=model_utils.fields.StatusField(default=b'backlog', max_length=100, no_check_for_status=True, choices=[(0, 'dummy')]),
        ),
        migrations.AlterField(
            model_name='task',
            name='work_type',
            field=models.ForeignKey(related_name='tasks', blank=True, to='core.WorkType', null=True),
        ),
    ]
