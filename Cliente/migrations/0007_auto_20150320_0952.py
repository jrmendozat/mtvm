# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cliente', '0006_auto_20150320_0945'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente_direccion',
            old_name='direccion',
            new_name='direc',
        ),
    ]
