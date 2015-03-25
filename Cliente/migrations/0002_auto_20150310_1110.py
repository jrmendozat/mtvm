# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Segmento', '0001_initial'),
        ('Tipo_cliente', '0001_initial'),
        ('Empresa', '0001_initial'),
        ('Cliente', '0001_initial'),
        ('Direccion', '0001_initial'),
        ('Sede', '0001_initial'),
        ('Persona', '0001_initial'),
        ('Condicion_pago', '0001_initial'),
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
            field=models.ForeignKey(to='Cliente.Cliente'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cliente_direccion',
            name='direccion',
            field=models.OneToOneField(to='Direccion.Direccion'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cliente_direccion',
            name='sede',
            field=models.OneToOneField(to='Sede.Sede'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cliente',
            name='condicion_pago',
            field=models.ForeignKey(to='Condicion_pago.Condicion_pago', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cliente',
            name='segmento',
            field=models.ForeignKey(to='Segmento.Segmento', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cliente',
            name='tipo_cliente',
            field=models.ForeignKey(to='Tipo_cliente.Tipo_cliente', null=True),
            preserve_default=True,
        ),
    ]
