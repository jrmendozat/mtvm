# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Articulo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo_unidad',
            name='principal',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
