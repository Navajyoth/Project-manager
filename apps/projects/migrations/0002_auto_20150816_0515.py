# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectWork',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('count', models.PositiveSmallIntegerField()),
                ('rate', models.DecimalField(max_digits=20, decimal_places=2)),
                ('work_type', models.ForeignKey(related_name='works', to='core.WorkType')),
            ],
        ),
        migrations.RemoveField(
            model_name='project',
            name='project_name',
        ),
        migrations.AddField(
            model_name='project',
            name='name',
            field=models.CharField(default='asd', max_length=64),
            preserve_default=False,
        ),
    ]
