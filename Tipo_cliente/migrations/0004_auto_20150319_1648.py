# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tipo_cliente', '0003_auto_20150319_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipo_cliente',
            name='descripcion',
            field=models.CharField(unique=True, max_length=50),
            preserve_default=True,
        ),
    ]
