# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0002_auto_20150816_0515'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('modified_on', models.DateField(auto_now=True)),
                ('title', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=512, null=True, blank=True)),
                ('status', model_utils.fields.StatusField(default=b'in_progress', max_length=100, no_check_for_status=True, choices=[(b'in_progress', b'in_progress'), (b'pending_review', b'pending_review'), (b'completed', b'completed')])),
                ('project', models.ForeignKey(related_name='tasks', to='projects.Project')),
                ('user', models.ForeignKey(related_name='tasks', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('work_type', models.ForeignKey(related_name='tasks', to='core.WorkType')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
