# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sede', '0004_sede_sede'),
        ('Cliente', '0002_auto_20150326_1417'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente_direccion',
            name='sede',
        ),
        migrations.AddField(
            model_name='cliente_direccion',
            name='sede1',
            field=models.OneToOneField(default=1, blank=True, to='Sede.Sede'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cliente',
            name='comentarios',
            field=models.TextField(default=True, blank=True),
            preserve_default=False,
        ),
    ]
