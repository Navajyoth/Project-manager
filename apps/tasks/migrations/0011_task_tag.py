# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0010_auto_20150825_1053'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='tag',
            field=models.CharField(max_length=128, null=True, blank=True),
        ),
    ]
