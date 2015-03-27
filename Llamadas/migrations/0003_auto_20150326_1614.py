# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Llamadas', '0002_auto_20150325_1005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='llamada',
            name='zonadestino',
        ),
        migrations.RemoveField(
            model_name='llamada',
            name='zonaorigen',
        ),
    ]
