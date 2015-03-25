# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cliente', '0003_auto_20150313_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente_telefono',
            name='cliente',
            field=models.ForeignKey(default=1, to='Cliente.Cliente'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cliente_telefono',
            name='telefono',
            field=models.OneToOneField(default=1, to='Telefono.Telefono'),
            preserve_default=True,
        ),
    ]
