# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cliente', '0005_auto_20150319_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente_direccion',
            name='cliente',
            field=models.ForeignKey(default=1, to='Cliente.Cliente'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cliente_direccion',
            name='direccion',
            field=models.OneToOneField(default=1, to='Direccion.Direccion'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cliente_direccion',
            name='sede',
            field=models.OneToOneField(blank=True, to='Sede.Sede'),
            preserve_default=True,
        ),
    ]
