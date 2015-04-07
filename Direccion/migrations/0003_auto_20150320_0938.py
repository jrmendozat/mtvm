# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Direccion', '0002_auto_20150319_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='direccion',
            name='zip1',
            field=models.CharField(default=True, max_length=10, blank=True),
            preserve_default=False,
        ),
    ]
