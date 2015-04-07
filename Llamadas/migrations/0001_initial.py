# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Pais', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='llamada',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('horaini', models.TimeField(auto_now_add=True)),
                ('horafin', models.TimeField()),
                ('tipollamada', models.CharField(default=b'1', max_length=1, choices=[(b'1', b'Entrante'), (b'2', b'Saliente')])),
                ('status', models.CharField(max_length=10)),
                ('nrocotizacion', models.CharField(max_length=20)),
                ('nombrecli', models.CharField(max_length=250)),
                ('telefono', models.CharField(max_length=15)),
                ('celular', models.CharField(max_length=15)),
                ('motivo', models.CharField(max_length=50, choices=[(b'Cotizacion Mudanza', b'Cotizaci\xc3\xb3n Mudanza'), (b'Confirmacion Mudanza', b'Confirmaci\xc3\xb3n Mudanza'), (b'Cambio de Fecha Mudanza', b'Cambio de Fecha Mudanza'), (b'Cambio Visita Cotizador', b'Cambio Visita Cotizador'), (b'Cancela Visita Cotizador', b'Cancela Visita Cotizador'), (b'Cancelacion Mudanza', b'Cancelaci\xc3\xb3n Mudanza'), (b'Seguimiento de Ventas', b'Seguimiento de Ventas'), (b'Consulta', b'Consulta'), (b'Gestion de Canastos', b'Gesti\xc3\xb3n de Canastos'), (b'Llamada Perdida', b'Llamada Perdida'), (b'Interno', b'Interno'), (b'Empresas', b'Empresas'), (b'Control de Calidad', b'Control de Calidad'), (b'N/S', b'N/S'), (b'Otros', b'Otros'), (b'Reclamo Mudanza', b'Reclamo Mudanza')])),
                ('observacion', models.CharField(max_length=250)),
                ('direccorigen', models.CharField(max_length=250)),
                ('barrioorigen', models.CharField(max_length=100)),
                ('tipoorigen', models.CharField(max_length=100)),
                ('ambptos', models.PositiveIntegerField()),
                ('direccdestino', models.CharField(max_length=250)),
                ('barriodestino', models.CharField(max_length=100)),
                ('fuentereclutamiento', models.CharField(max_length=200)),
                ('barriopublicidad', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=75)),
                ('fechacotiz', models.DateField()),
                ('horacotiz', models.TimeField()),
                ('nombrecotiz', models.CharField(max_length=250)),
                ('nombrequieningreso', models.CharField(max_length=250)),
                ('duracionllamada', models.TimeField()),
                ('zonadestino', models.ForeignKey(related_name='zona2', to='Pais.Zona')),
                ('zonaorigen', models.ForeignKey(related_name='zona1', to='Pais.Zona')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
