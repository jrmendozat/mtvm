# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Telefono', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telefono',
            name='tipo_telefono',
            field=models.ForeignKey(default=1, to='Telefono.Tipo_telefono'),
            preserve_default=True,
        ),
    ]
