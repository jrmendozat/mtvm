# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sede', '0006_auto_20150327_1556'),
    ]

    operations = [
        migrations.CreateModel(
            name='Familia_Mueble',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('familia_muebles', models.CharField(max_length=100)),
                ('adicional1', models.CharField(max_length=250)),
                ('adicional2', models.CharField(max_length=250)),
                ('adicional3', models.CharField(max_length=250)),
                ('adicional4', models.CharField(max_length=250)),
                ('activo', models.BooleanField()),
            ],
            options={
                'verbose_name_plural': 'Familia de Muebles',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Mueble',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mueble', models.CharField(max_length=250)),
                ('trasladable', models.BooleanField()),
                ('ancho', models.DecimalField(max_digits=13, decimal_places=2)),
                ('alto', models.DecimalField(max_digits=13, decimal_places=2)),
                ('largo', models.DecimalField(max_digits=13, decimal_places=2)),
                ('peso', models.DecimalField(max_digits=13, decimal_places=2)),
                ('capacidad_interna', models.DecimalField(max_digits=13, decimal_places=2)),
                ('capacidad_carga', models.DecimalField(max_digits=13, decimal_places=2)),
                ('apilable', models.BooleanField()),
                ('adicional1', models.CharField(max_length=250)),
                ('adicional2', models.CharField(max_length=250)),
                ('adicional3', models.CharField(max_length=250)),
                ('adicional4', models.CharField(max_length=250)),
                ('observaciones', models.TextField()),
                ('activo', models.BooleanField()),
                ('familia', models.ForeignKey(to='Mueble.Familia_Mueble')),
                ('tipo_ambiente', models.ForeignKey(to='Sede.Tipo_Ambiente')),
            ],
            options={
                'verbose_name_plural': 'Muebles',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tamanio_Mueble',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo_tamanio', models.CharField(max_length=100)),
                ('adicional1', models.CharField(max_length=250)),
                ('adicional2', models.CharField(max_length=250)),
                ('adicional3', models.CharField(max_length=250)),
                ('adicional4', models.CharField(max_length=250)),
                ('activo', models.BooleanField()),
            ],
            options={
                'verbose_name_plural': 'Tamanios de Muebles',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tipo_Fragilidad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo_fragilidad', models.CharField(max_length=100)),
                ('adicional1', models.CharField(max_length=250)),
                ('adicional2', models.CharField(max_length=250)),
                ('adicional3', models.CharField(max_length=250)),
                ('adicional4', models.CharField(max_length=250)),
                ('activo', models.BooleanField()),
            ],
            options={
                'verbose_name_plural': 'Tipos de Fradilidad',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tipo_Peso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo_peso', models.CharField(max_length=100)),
                ('peso_promedio', models.DecimalField(max_digits=13, decimal_places=2)),
                ('adicional1', models.CharField(max_length=250)),
                ('adicional2', models.CharField(max_length=250)),
                ('adicional3', models.CharField(max_length=250)),
                ('adicional4', models.CharField(max_length=250)),
                ('activo', models.BooleanField()),
            ],
            options={
                'verbose_name_plural': 'Tipos de Pesos',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='mueble',
            name='tipo_fragil',
            field=models.ForeignKey(to='Mueble.Tipo_Fragilidad'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mueble',
            name='tipo_peso',
            field=models.ForeignKey(to='Mueble.Tipo_Peso'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mueble',
            name='tipo_tamanio',
            field=models.ForeignKey(to='Mueble.Tamanio_Mueble'),
            preserve_default=True,
        ),
    ]
