# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Articulo', '0002_auto_20150401_0930'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articulo_costo',
            options={'verbose_name_plural': 'Costos de Articulos'},
        ),
        migrations.AlterField(
            model_name='articulo_proveedor',
            name='adicional1',
            field=models.CharField(max_length=250, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='articulo_proveedor',
            name='adicional2',
            field=models.CharField(max_length=250, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='articulo_proveedor',
            name='adicional3',
            field=models.CharField(max_length=250, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='articulo_proveedor',
            name='adicional4',
            field=models.CharField(max_length=250, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='unidad',
            name='adicional1',
            field=models.CharField(max_length=250, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='unidad',
            name='adicional2',
            field=models.CharField(max_length=250, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='unidad',
            name='adicional3',
            field=models.CharField(max_length=250, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='unidad',
            name='adicional4',
            field=models.CharField(max_length=250, blank=True),
            preserve_default=True,
        ),
    ]
