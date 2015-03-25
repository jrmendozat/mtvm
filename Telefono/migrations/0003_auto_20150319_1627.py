# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Telefono', '0002_auto_20150313_1637'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='telefono',
            options={'verbose_name_plural': 'Telefonos'},
        ),
        migrations.AlterModelOptions(
            name='tipo_telefono',
            options={'verbose_name_plural': 'Tipos de telefonos'},
        ),
    ]
