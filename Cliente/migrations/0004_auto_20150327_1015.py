# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cliente', '0003_auto_20150326_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente_direccion',
            name='sede1',
            field=models.OneToOneField(null=True, blank=True, to='Sede.Sede'),
            preserve_default=True,
        ),
    ]
