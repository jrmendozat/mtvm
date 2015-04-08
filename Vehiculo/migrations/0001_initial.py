# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Modelo_Vehiculo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('modelo_vehiculo', models.CharField(max_length=100)),
                ('capacidad_peso', models.IntegerField()),
                ('capacidad_x', models.DecimalField(max_digits=6, decimal_places=2)),
                ('capacidad_y', models.DecimalField(max_digits=6, decimal_places=2)),
                ('capacidad_z', models.DecimalField(max_digits=6, decimal_places=2)),
                ('capacidad_m3', models.DecimalField(max_digits=6, decimal_places=2)),
                ('adicional1', models.CharField(max_length=250, blank=True)),
                ('adicional2', models.CharField(max_length=250, blank=True)),
                ('adicional3', models.CharField(max_length=250, blank=True)),
                ('adicional4', models.CharField(max_length=250, blank=True)),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Modelos de Vehiculos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tipo_Vehiculo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo_vehiculo', models.CharField(unique=True, max_length=100)),
                ('adicional1', models.CharField(max_length=250, blank=True)),
                ('adicional2', models.CharField(max_length=250, blank=True)),
                ('adicional3', models.CharField(max_length=250, blank=True)),
                ('adicional4', models.CharField(max_length=250, blank=True)),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Tipos de Vehiculos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero_vehiculo', models.CharField(max_length=10)),
                ('vehiculo', models.CharField(max_length=100)),
                ('patente', models.CharField(max_length=100)),
                ('adicional1', models.CharField(max_length=250, blank=True)),
                ('adicional2', models.CharField(max_length=250, blank=True)),
                ('adicional3', models.CharField(max_length=250, blank=True)),
                ('adicional4', models.CharField(max_length=250, blank=True)),
                ('activo', models.BooleanField(default=True)),
                ('modelo_vehiculo', models.ForeignKey(to='Vehiculo.Modelo_Vehiculo')),
                ('tipo_vehiculo', models.ForeignKey(to='Vehiculo.Tipo_Vehiculo')),
            ],
            options={
                'verbose_name_plural': 'Vehiculos',
            },
            bases=(models.Model,),
        ),
    ]
