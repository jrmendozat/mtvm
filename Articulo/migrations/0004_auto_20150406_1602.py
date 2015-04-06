# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Articulo', '0003_auto_20150406_1526'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articulo_proveedor',
            options={'verbose_name_plural': 'Proveedores de Articulos'},
        ),
        migrations.RemoveField(
            model_name='articulo_proveedor',
            name='proveedor',
        ),
    ]
