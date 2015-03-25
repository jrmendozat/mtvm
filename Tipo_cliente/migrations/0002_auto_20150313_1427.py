# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tipo_cliente', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipo_cliente',
            name='adicional1',
            field=models.CharField(default=True, max_length=50, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tipo_cliente',
            name='adicional2',
            field=models.CharField(default=True, max_length=50, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tipo_cliente',
            name='adicional3',
            field=models.CharField(default=True, max_length=50, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tipo_cliente',
            name='adicional4',
            field=models.CharField(default=True, max_length=50, blank=True),
            preserve_default=False,
        ),
    ]
