# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_manager',
            field=models.BooleanField(default=False, help_text='Designates whether user is manager.', verbose_name='manager'),
        ),
    ]
