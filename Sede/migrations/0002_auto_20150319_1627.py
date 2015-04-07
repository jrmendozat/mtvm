# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sede', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ambiente',
            options={'verbose_name': 'Ambiente', 'verbose_name_plural': 'Ambientes'},
        ),
        migrations.AlterModelOptions(
            name='sede',
            options={'verbose_name': 'Sede', 'verbose_name_plural': 'Sedes'},
        ),
        migrations.AlterModelOptions(
            name='Tipo_Ambiente',
            options={'verbose_name': 'Tipo de ambiente', 'verbose_name_plural': 'Tipos de ambientes'},
        ),
        migrations.AlterModelOptions(
            name='tipo_sede',
            options={'verbose_name': 'Tipo de sede', 'verbose_name_plural': 'Tipos de sede'},
        ),
    ]
