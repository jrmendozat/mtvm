# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Articulo', '0005_articulo_proveedor_proveedor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo_clase',
            name='clase',
            field=models.CharField(unique=True, max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='categoria_articulo',
            name='categoria',
            field=models.CharField(unique=True, max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tipo_costo',
            name='tipo_costo',
            field=models.CharField(unique=True, max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='unidad',
            name='unidad',
            field=models.CharField(unique=True, max_length=100),
            preserve_default=True,
        ),
    ]
