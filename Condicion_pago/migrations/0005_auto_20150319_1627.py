# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Condicion_pago', '0004_auto_20150313_1427'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='condicion_pago',
            options={'verbose_name': 'Condicion de pago', 'verbose_name_plural': 'Condiciones de pago'},
        ),
    ]
