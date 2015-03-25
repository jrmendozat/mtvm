# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Empresa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='Comentarios',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='empresa',
            name='adicional1',
            field=models.CharField(max_length=50, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='empresa',
            name='adicional2',
            field=models.CharField(max_length=50, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='empresa',
            name='adicional3',
            field=models.CharField(max_length=50, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='empresa',
            name='adicional4',
            field=models.CharField(max_length=50, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='empresa',
            name='documento_fiscal',
            field=models.CharField(max_length=50, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='empresa',
            name='nombre',
            field=models.CharField(unique=True, max_length=250),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='empresa',
            name='sitio_web',
            field=models.CharField(max_length=250, blank=True),
            preserve_default=True,
        ),
    ]
