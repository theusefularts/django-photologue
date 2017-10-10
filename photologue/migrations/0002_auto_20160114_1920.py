# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photologue', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='slug',
            field=models.SlugField(help_text='A "slug" is a unique URL-friendly title for an object.', unique=True, verbose_name='slug'),
        ),
    ]
