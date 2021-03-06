# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0009_auto_20150825_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statuslog',
            name='user',
            field=models.ForeignKey(related_name='status_logs', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
