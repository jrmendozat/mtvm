# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sede', '0003_auto_20150325_1005'),
    ]

    operations = [
        migrations.AddField(
            model_name='sede',
            name='sede',
            field=models.CharField(default=True, max_length=250),
            preserve_default=False,
        ),
    ]
