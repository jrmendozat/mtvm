# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sede', '0002_auto_20150319_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipo_ambiente',
            name='tipo_ambiente',
            field=models.CharField(unique=True, max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tipo_sede',
            name='nombre',
            field=models.CharField(unique=True, max_length=50),
            preserve_default=True,
        ),
    ]
