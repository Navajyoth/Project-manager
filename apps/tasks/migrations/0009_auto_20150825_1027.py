# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0008_statuslog'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='statuslog',
            options={'ordering': ('-pk',)},
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=256),
        ),
    ]
