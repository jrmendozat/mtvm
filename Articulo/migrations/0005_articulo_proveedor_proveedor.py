# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Proveedor', '0001_initial'),
        ('Articulo', '0004_auto_20150406_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo_proveedor',
            name='proveedor',
            field=models.ForeignKey(default=True, to='Proveedor.Proveedor'),
            preserve_default=False,
        ),
    ]
