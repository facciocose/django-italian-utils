# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('italian_utils', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comune',
            options={'verbose_name': 'comune', 'verbose_name_plural': 'comuni'},
        ),
        migrations.AlterField(
            model_name='comune',
            name='codice_catastale',
            field=models.CharField(max_length=4, unique=True),
        ),
    ]
