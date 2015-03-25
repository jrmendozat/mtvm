# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Departamento', '0001_initial'),
        ('Persona', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo_status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo_status', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo_trabajador', models.CharField(max_length=50, null=True)),
                ('fecha_ingreso', models.DateField()),
                ('fecha_retiro', models.DateField(blank=True)),
                ('cargo', models.ForeignKey(to='Departamento.Cargo')),
                ('persona', models.ForeignKey(to='Persona.Persona')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Trabajador_status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_inicio_status', models.DateField(auto_now_add=True)),
                ('tipo_status', models.ForeignKey(to='Trabajador.Tipo_status')),
                ('trabajador', models.ForeignKey(to='Trabajador.Trabajador')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
