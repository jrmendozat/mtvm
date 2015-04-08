# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Proveedor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='adicional1',
            field=models.CharField(max_length=250, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='adicional2',
            field=models.CharField(max_length=250, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='adicional3',
            field=models.CharField(max_length=250, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tipo_proveedor',
            name='adicional1',
            field=models.CharField(max_length=250, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tipo_proveedor',
            name='adicional2',
            field=models.CharField(max_length=250, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tipo_proveedor',
            name='adicional3',
            field=models.CharField(max_length=250, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tipo_proveedor',
            name='adicional4',
            field=models.CharField(max_length=250, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tipo_proveedor',
            name='tipo_proveedor',
            field=models.CharField(unique=True, max_length=100),
            preserve_default=True,
        ),
    ]
