# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Trabajador', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tipo_status',
            options={'verbose_name_plural': 'Tipos de status de trabajadores'},
        ),
        migrations.AlterModelOptions(
            name='trabajador',
            options={'verbose_name_plural': 'Trabajadores'},
        ),
        migrations.AlterModelOptions(
            name='trabajador_status',
            options={'verbose_name_plural': 'Status de trabajadores'},
        ),
    ]
