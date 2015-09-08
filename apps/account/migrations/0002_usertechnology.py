# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_technology'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserTechnology',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('technology', models.ForeignKey(related_name='users', to='core.Technology')),
                ('user', models.ForeignKey(related_name='technologies', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
