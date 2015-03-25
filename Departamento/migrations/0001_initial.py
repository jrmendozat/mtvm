# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=20, null=True)),
                ('nombre', models.CharField(max_length=100)),
                ('cargo_supervisor', models.ForeignKey(related_name='cargo_supervisor1', to='Departamento.Cargo', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cargo_tipo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cargo_tipo', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=20, null=True)),
                ('nombre', models.CharField(max_length=100)),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Disenio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('linea_tipo', models.IntegerField()),
                ('linea_grosor', models.IntegerField()),
                ('linea_color', models.CharField(default=b'000000', max_length=7)),
                ('relleno_color', models.CharField(default=b'FFFFFF', max_length=7)),
                ('ancho', models.IntegerField(default=64)),
                ('alto', models.IntegerField(default=40)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Jerarquia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('disenio', models.ForeignKey(to='Departamento.Disenio')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='departamento',
            name='disenio',
            field=models.ForeignKey(to='Departamento.Disenio'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='departamento',
            name='tipo_jerarquia',
            field=models.ForeignKey(to='Departamento.Jerarquia'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='departamento',
            name='unidad_superior',
            field=models.ForeignKey(related_name='unidad_superior1', to='Departamento.Departamento', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cargo',
            name='cargo_tipo',
            field=models.ForeignKey(to='Departamento.Cargo_tipo'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cargo',
            name='departamento',
            field=models.ForeignKey(to='Departamento.Departamento'),
            preserve_default=True,
        ),
    ]
