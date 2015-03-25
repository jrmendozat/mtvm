# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo_cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=50)),
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
            name='Tipo_precio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='tipo_cliente',
            name='precio',
            field=models.ForeignKey(to='Tipo_cliente.Tipo_precio'),
            preserve_default=True,
        ),
    ]
