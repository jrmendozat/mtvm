# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Trabajador', '0002_auto_20150319_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipo_status',
            name='tipo_status',
            field=models.CharField(unique=True, max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='trabajador',
            name='codigo_trabajador',
            field=models.CharField(max_length=50, blank=True),
            preserve_default=True,
        ),
    ]
