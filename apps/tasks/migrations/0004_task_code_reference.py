# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_auto_20150818_0549'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='code_reference',
            field=models.CharField(max_length=512, null=True, blank=True),
        ),
    ]
