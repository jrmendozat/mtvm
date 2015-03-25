# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Segmento', '0002_auto_20150313_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='segmento',
            name='segmento',
            field=models.CharField(unique=True, max_length=50),
            preserve_default=True,
        ),
    ]
