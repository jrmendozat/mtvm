# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Pais', '0002_auto_20150319_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ciudad',
            name='ciudad',
            field=models.CharField(unique=True, max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pais',
            name='pais',
            field=models.CharField(unique=True, max_length=250),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='provincia',
            name='provincia',
            field=models.CharField(unique=True, max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='zona',
            name='zona',
            field=models.CharField(unique=True, max_length=100),
            preserve_default=True,
        ),
    ]
