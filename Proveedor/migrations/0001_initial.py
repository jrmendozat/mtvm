# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Direccion', '0001_initial'),
        ('Telefono', '0003_auto_20150319_1627'),
        ('Segmento', '0003_auto_20150320_0842'),
        ('Condicion_pago', '0006_auto_20150325_1005'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email_Proveedor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=75)),
            ],
            options={
                'verbose_name_plural': 'Email de proveedores',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('proveedor', models.CharField(max_length=250)),
                ('monto_credito', models.DecimalField(max_digits=13, decimal_places=2)),
                ('sitio_web', models.URLField()),
                ('comentarios', models.TextField()),
                ('adicional1', models.CharField(max_length=250)),
                ('adicional2', models.CharField(max_length=250)),
                ('adicional3', models.CharField(max_length=250)),
                ('activo', models.BooleanField(default=True)),
                ('condicion_pago', models.ForeignKey(to='Condicion_pago.Condicion_pago')),
                ('segmento', models.ForeignKey(to='Segmento.Segmento')),
            ],
            options={
                'verbose_name_plural': 'Proveedores',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Proveedor_Direccion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('direccion', models.OneToOneField(to='Direccion.Direccion')),
                ('proveedor', models.ForeignKey(to='Proveedor.Proveedor')),
            ],
            options={
                'verbose_name_plural': 'Direcciones de proveedores',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Proveedor_Telefono',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('proveedor', models.ForeignKey(to='Proveedor.Proveedor')),
                ('telefono', models.ForeignKey(to='Telefono.Telefono')),
            ],
            options={
                'verbose_name_plural': 'Telefonos de proveedores',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tipo_Proveedor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo_proveedor', models.CharField(max_length=100)),
                ('adicional1', models.CharField(max_length=250)),
                ('adicional2', models.CharField(max_length=250)),
                ('adicional3', models.CharField(max_length=250)),
                ('adicional4', models.CharField(max_length=250)),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Tipos proveedores',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='proveedor',
            name='tipo_proveedor',
            field=models.ForeignKey(to='Proveedor.Tipo_Proveedor'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='email_proveedor',
            name='proveedor',
            field=models.ForeignKey(to='Proveedor.Proveedor'),
            preserve_default=True,
        ),
    ]
