# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Pais', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('direccion', models.CharField(max_length=500)),
                ('punto_referencia', models.CharField(max_length=250)),
                ('zip1', models.CharField(max_length=10, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tipo_direccion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo_direccion', models.CharField(max_length=10)),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='direccion',
            name='tipo_direccion',
            field=models.ForeignKey(to='Direccion.Tipo_direccion'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='direccion',
            name='zona',
            field=models.ForeignKey(to='Pais.Zona'),
            preserve_default=True,
        ),
    ]
