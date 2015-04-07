# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cliente', '0007_auto_20150320_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente_direccion',
            name='direc',
            field=models.OneToOneField(default=1, blank=True, to='Direccion.Direccion'),
            preserve_default=True,
        ),
    ]
