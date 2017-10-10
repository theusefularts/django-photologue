# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import photologue.models
import django.utils.timezone
import django.core.validators
import sortedm2m.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
	('photologue', '0003_auto_20160115_1134'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='sites',
            field=models.ManyToManyField(to='sites.Site', verbose_name='sites', blank=True),
        ),
        migrations.AddField(
            model_name='gallery',
            name='sites',
            field=models.ManyToManyField(to='sites.Site', verbose_name='sites', blank=True),
        ),
    ]
