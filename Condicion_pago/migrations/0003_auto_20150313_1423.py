# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Condicion_pago', '0002_auto_20150313_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='condicion_pago',
            name='adicional1',
            field=models.CharField(max_length=50, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='condicion_pago',
            name='adicional2',
            field=models.CharField(default=True, max_length=50, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='condicion_pago',
            name='adicional3',
            field=models.CharField(default=True, max_length=50, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='condicion_pago',
            name='adicional4',
            field=models.CharField(default=True, max_length=50, blank=True),
            preserve_default=False,
        ),
    ]
