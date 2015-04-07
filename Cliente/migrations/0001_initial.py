# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Telefono', '0003_auto_20150319_1627'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_principal', models.CharField(max_length=250)),
                ('monto_credito', models.DecimalField(max_digits=10, decimal_places=2, blank=True)),
                ('sitio_web', models.CharField(max_length=250, blank=True)),
                ('comentarios', models.TextField(null=True)),
                ('adicional1', models.CharField(max_length=50, blank=True)),
                ('adicional2', models.CharField(max_length=50, blank=True)),
                ('adicional3', models.CharField(max_length=50, blank=True)),
                ('adicional4', models.CharField(max_length=50, blank=True)),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cliente_Direccion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'verbose_name': 'Direccion del cliente',
                'verbose_name_plural': 'Direcciones del cliente',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cliente_empresa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('principal', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Empresa del cliente',
                'verbose_name_plural': 'Empresas del cliente',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cliente_persona',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('principal', models.BooleanField(default=True)),
                ('cliente', models.ForeignKey(to='Cliente.Cliente')),
            ],
            options={
                'verbose_name': 'Persona del cliente',
                'verbose_name_plural': 'Personas del cliente',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cliente_telefono',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cliente', models.ForeignKey(default=1, to='Cliente.Cliente')),
                ('telefono', models.OneToOneField(default=1, to='Telefono.Telefono')),
            ],
            options={
                'verbose_name': 'Telefono del cliente',
                'verbose_name_plural': 'Telefonos del cliente',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=75)),
                ('cliente', models.ForeignKey(default=1, to='Cliente.Cliente')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
