# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sede', '0005_auto_20150327_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ambiente',
            name='ambiente',
            field=models.ForeignKey(to='Sede.Tipo_Ambiente'),
            preserve_default=True,
        ),
    ]
