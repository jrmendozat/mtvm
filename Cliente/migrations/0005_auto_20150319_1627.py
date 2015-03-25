# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cliente', '0004_auto_20150317_1531'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliente_direccion',
            options={'verbose_name': 'Direccion del cliente', 'verbose_name_plural': 'Direcciones del cliente'},
        ),
        migrations.AlterModelOptions(
            name='cliente_empresa',
            options={'verbose_name': 'Empresa del cliente', 'verbose_name_plural': 'Empresas del cliente'},
        ),
        migrations.AlterModelOptions(
            name='cliente_persona',
            options={'verbose_name': 'Persona del cliente', 'verbose_name_plural': 'Personas del cliente'},
        ),
        migrations.AlterModelOptions(
            name='cliente_telefono',
            options={'verbose_name': 'Telefono del cliente', 'verbose_name_plural': 'Telefonos del cliente'},
        ),
        migrations.AlterField(
            model_name='email',
            name='cliente',
            field=models.ForeignKey(default=1, to='Cliente.Cliente'),
            preserve_default=True,
        ),
    ]
