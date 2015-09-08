# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0007_auto_20150824_0744'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatusLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=16)),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
                ('task', models.ForeignKey(related_name='status_logs', to='tasks.Task')),
                ('user', models.ForeignKey(related_name='status_logs', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
