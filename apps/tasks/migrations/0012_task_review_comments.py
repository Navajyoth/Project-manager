# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0011_task_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='review_comments',
            field=models.CharField(max_length=1024, null=True, blank=True),
        ),
    ]
