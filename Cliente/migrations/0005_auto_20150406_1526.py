# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cliente', '0004_auto_20150327_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='sitio_web',
            field=models.URLField(),
            preserve_default=True,
        ),
    ]
