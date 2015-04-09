# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Vehiculo', '0001_initial'),
        ('Articulo', '0006_auto_20150408_0949'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipamiento_Transporte',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=100)),
                ('cantidad', models.DecimalField(max_digits=13, decimal_places=2)),
                ('costo', models.DecimalField(max_digits=13, decimal_places=2)),
                ('adicional1', models.CharField(max_length=250, blank=True)),
                ('adicional2', models.CharField(max_length=250, blank=True)),
                ('adicional3', models.CharField(max_length=250, blank=True)),
                ('adicional4', models.CharField(max_length=250, blank=True)),
                ('articulo', models.ForeignKey(to='Articulo.Articulo')),
            ],
            options={
                'verbose_name_plural': 'Equipamientos de Transportes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Transporte',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('transporte', models.CharField(unique=True, max_length=100)),
                ('adicional1', models.CharField(max_length=250, blank=True)),
                ('adicional2', models.CharField(max_length=250, blank=True)),
                ('adicional3', models.CharField(max_length=250, blank=True)),
                ('adicional4', models.CharField(max_length=250, blank=True)),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Transportes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Transporte_cuadrilla',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('observaciones', models.CharField(max_length=250)),
                ('adicional1', models.CharField(max_length=250, blank=True)),
                ('adicional2', models.CharField(max_length=250, blank=True)),
                ('adicional3', models.CharField(max_length=250, blank=True)),
                ('adicional4', models.CharField(max_length=250, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Transporte_rol',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rol', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=250)),
                ('adicional1', models.CharField(max_length=250, blank=True)),
                ('adicional2', models.CharField(max_length=250, blank=True)),
                ('adicional3', models.CharField(max_length=250, blank=True)),
                ('adicional4', models.CharField(max_length=250, blank=True)),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Rol de Transportes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Transporte_Vehiculo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('transporte', models.ForeignKey(to='Transporte.Transporte')),
                ('vehiculo', models.ForeignKey(to='Vehiculo.Vehiculo')),
            ],
            options={
                'verbose_name_plural': 'Vehiculos de Transportes',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='transporte_cuadrilla',
            name='rol',
            field=models.ForeignKey(to='Transporte.Transporte_rol'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='transporte_cuadrilla',
            name='transporte',
            field=models.ForeignKey(to='Transporte.Transporte'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='equipamiento_transporte',
            name='transporte',
            field=models.ForeignKey(to='Transporte.Transporte'),
            preserve_default=True,
        ),
    ]
