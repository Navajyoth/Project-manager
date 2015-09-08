# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_auto_20150820_0934'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ('user', 'pk')},
        ),
    ]
