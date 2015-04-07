# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Telefono', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_principal', models.CharField(max_length=250)),
                ('monto_credito', models.DecimalField(null=True, max_digits=10, decimal_places=2)),
                ('sitio_web', models.CharField(max_length=250, null=True)),
                ('comentarios', models.TextField(null=True)),
                ('adicional1', models.CharField(max_length=50, null=True)),
                ('adicional2', models.CharField(max_length=50, null=True)),
                ('adicional3', models.CharField(max_length=50, null=True)),
                ('adicional4', models.CharField(max_length=50, null=True)),
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
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cliente_telefono',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cliente', models.ForeignKey(to='Cliente.Cliente')),
                ('telefono', models.OneToOneField(to='Telefono.Telefono')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=75)),
                ('cliente', models.ForeignKey(to='Cliente.Cliente')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
