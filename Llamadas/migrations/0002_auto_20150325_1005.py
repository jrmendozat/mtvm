# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Llamadas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='llamada',
            name='zonadestino',
            field=models.ForeignKey(related_name='zona2', to='Direccion.Zona'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='llamada',
            name='zonaorigen',
            field=models.ForeignKey(related_name='zona1', to='Direccion.Zona'),
            preserve_default=True,
        ),
    ]
