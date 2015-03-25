# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tipo_cliente', '0002_auto_20150313_1427'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tipo_cliente',
            options={'verbose_name_plural': 'Tipos de clientes'},
        ),
        migrations.AlterModelOptions(
            name='tipo_precio',
            options={'verbose_name_plural': 'Tipos de precios'},
        ),
        migrations.AlterField(
            model_name='tipo_precio',
            name='nombre',
            field=models.CharField(unique=True, max_length=50),
            preserve_default=True,
        ),
    ]
