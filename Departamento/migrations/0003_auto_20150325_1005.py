# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Departamento', '0002_auto_20150319_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cargo',
            name='cargo_supervisor',
            field=models.ForeignKey(related_name='cargo_supervisor1', blank=True, to='Departamento.Cargo'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cargo',
            name='codigo',
            field=models.CharField(max_length=20, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cargo',
            name='nombre',
            field=models.CharField(unique=True, max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cargo_tipo',
            name='cargo_tipo',
            field=models.CharField(unique=True, max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='departamento',
            name='codigo',
            field=models.CharField(max_length=20, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='departamento',
            name='nombre',
            field=models.CharField(unique=True, max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='departamento',
            name='unidad_superior',
            field=models.ForeignKey(related_name='unidad_superior1', blank=True, to='Departamento.Departamento'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jerarquia',
            name='nombre',
            field=models.CharField(unique=True, max_length=100),
            preserve_default=True,
        ),
    ]
