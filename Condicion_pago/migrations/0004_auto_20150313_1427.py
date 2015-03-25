# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Condicion_pago', '0003_auto_20150313_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='condicion_pago',
            name='condicion',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
    ]
