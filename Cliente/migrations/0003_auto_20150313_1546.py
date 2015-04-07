# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cliente', '0002_auto_20150310_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='adicional1',
            field=models.CharField(default=True, max_length=50, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cliente',
            name='adicional2',
            field=models.CharField(default=True, max_length=50, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cliente',
            name='adicional3',
            field=models.CharField(default=True, max_length=50, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cliente',
            name='adicional4',
            field=models.CharField(default=True, max_length=50, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cliente',
            name='condicion_pago',
            field=models.ForeignKey(default=True, blank=True, to='Condicion_pago.Condicion_pago'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cliente',
            name='monto_credito',
            field=models.DecimalField(default=True, max_digits=10, decimal_places=2, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cliente',
            name='segmento',
            field=models.ForeignKey(default=True, blank=True, to='Segmento.Segmento'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cliente',
            name='sitio_web',
            field=models.CharField(default=True, max_length=250, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cliente',
            name='tipo_cliente',
            field=models.ForeignKey(default=True, blank=True, to='Tipo_cliente.Tipo_cliente'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cliente_telefono',
            name='cliente',
            field=models.ForeignKey(related_name='id_cliente', to='Cliente.Cliente'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cliente_telefono',
            name='telefono',
            field=models.OneToOneField(related_name='id_telefono', to='Telefono.Telefono'),
            preserve_default=True,
        ),
    ]
