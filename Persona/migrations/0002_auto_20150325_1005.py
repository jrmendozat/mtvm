# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Persona', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='apellido2',
            field=models.CharField(max_length=100, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='persona',
            name='comentarios',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='persona',
            name='documento_fiscal',
            field=models.CharField(max_length=50, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='persona',
            name='documento_identidad',
            field=models.CharField(max_length=50, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='persona',
            name='nombre2',
            field=models.CharField(max_length=100, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='persona',
            name='tratamiento',
            field=models.ForeignKey(to='Persona.Tratamiento', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sexo',
            name='sexo',
            field=models.CharField(unique=True, max_length=25),
            preserve_default=True,
        ),
    ]
