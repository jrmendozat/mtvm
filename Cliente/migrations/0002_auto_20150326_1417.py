# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Empresa', '0001_initial'),
        ('Segmento', '0003_auto_20150320_0842'),
        ('Sede', '0004_sede_sede'),
        ('Cliente', '0001_initial'),
        ('Direccion', '0001_initial'),
        ('Persona', '0001_initial'),
        ('Tipo_cliente', '0004_auto_20150319_1648'),
        ('Condicion_pago', '0006_auto_20150325_1005'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente_persona',
            name='persona',
            field=models.ForeignKey(to='Persona.Persona'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cliente_empresa',
            name='cliente',
            field=models.ForeignKey(to='Cliente.Cliente'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cliente_empresa',
            name='empresa',
            field=models.ForeignKey(to='Empresa.Empresa'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cliente_direccion',
            name='cliente',
            field=models.ForeignKey(default=1, to='Cliente.Cliente'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cliente_direccion',
            name='direc',
            field=models.OneToOneField(default=1, blank=True, to='Direccion.Direccion'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cliente_direccion',
            name='sede',
            field=models.OneToOneField(blank=True, to='Sede.Sede'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cliente',
            name='condicion_pago',
            field=models.ForeignKey(to='Condicion_pago.Condicion_pago', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cliente',
            name='segmento',
            field=models.ForeignKey(to='Segmento.Segmento', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cliente',
            name='tipo_cliente',
            field=models.ForeignKey(to='Tipo_cliente.Tipo_cliente', blank=True),
            preserve_default=True,
        ),
    ]
