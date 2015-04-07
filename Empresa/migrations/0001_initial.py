# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Direccion', '0001_initial'),
        ('Telefono', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email_empresa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=75)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=250)),
                ('documento_fiscal', models.CharField(max_length=50, null=True)),
                ('Comentarios', models.TextField(null=True)),
                ('adicional1', models.CharField(max_length=50, null=True)),
                ('adicional2', models.CharField(max_length=50, null=True)),
                ('adicional3', models.CharField(max_length=50, null=True)),
                ('adicional4', models.CharField(max_length=50, null=True)),
                ('activo', models.BooleanField(default=True)),
                ('sitio_web', models.CharField(max_length=250, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Empresa_direccion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('direccion', models.ForeignKey(to='Direccion.Direccion')),
                ('empresa', models.ForeignKey(to='Empresa.Empresa')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Empresa_telefono',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('empresa', models.ForeignKey(to='Empresa.Empresa')),
                ('telefono', models.ForeignKey(to='Telefono.Telefono')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='email_empresa',
            name='empresa',
            field=models.ForeignKey(to='Empresa.Empresa'),
            preserve_default=True,
        ),
    ]
