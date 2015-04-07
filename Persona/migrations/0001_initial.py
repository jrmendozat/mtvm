# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Telefono', '0003_auto_20150319_1627'),
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('apellido1', models.CharField(max_length=100)),
                ('apellido2', models.CharField(max_length=100, blank=True)),
                ('nombre1', models.CharField(max_length=100)),
                ('nombre2', models.CharField(max_length=100, blank=True)),
                ('documento_identidad', models.CharField(max_length=50, blank=True)),
                ('documento_fiscal', models.CharField(max_length=50, blank=True)),
                ('comentarios', models.TextField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Persona_Direccion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('persona', models.ForeignKey(to='Persona.Persona')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Persona_evento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('evento', models.CharField(max_length=250)),
                ('fecha_evento', models.DateField()),
                ('persona', models.ForeignKey(to='Persona.Persona')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Persona_relacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('persona', models.ForeignKey(to='Persona.Persona')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Persona_telefono',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('persona', models.ForeignKey(to='Persona.Persona')),
                ('telefono', models.OneToOneField(to='Telefono.Telefono')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sexo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sexo', models.CharField(unique=True, max_length=25)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tipo_relacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo_relacion', models.CharField(max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tratamiento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tratamiento', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='persona_relacion',
            name='tipo_relacion',
            field=models.ForeignKey(to='Persona.Tipo_relacion'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='persona',
            name='sexo',
            field=models.ForeignKey(to='Persona.Sexo'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='persona',
            name='tratamiento',
            field=models.ForeignKey(to='Persona.Tratamiento', blank=True),
            preserve_default=True,
        ),
    ]
