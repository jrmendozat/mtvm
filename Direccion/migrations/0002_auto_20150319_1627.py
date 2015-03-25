# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Direccion', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='direccion',
            options={'verbose_name': 'Direccion', 'verbose_name_plural': 'Direcciones'},
        ),
        migrations.AlterModelOptions(
            name='tipo_direccion',
            options={'verbose_name': 'Tipo de direccion', 'verbose_name_plural': 'Tipos de direccion'},
        ),
    ]
