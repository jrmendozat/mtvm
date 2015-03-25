# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Departamento', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cargo_tipo',
            options={'verbose_name': 'Tipo de cargo', 'verbose_name_plural': 'Tipos de cargo'},
        ),
        migrations.AlterModelOptions(
            name='disenio',
            options={'verbose_name': 'Diseno', 'verbose_name_plural': 'Disenos'},
        ),
    ]
