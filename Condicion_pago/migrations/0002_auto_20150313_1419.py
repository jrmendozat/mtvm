# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Condicion_pago', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='condicion_pago',
            name='adicional1',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
