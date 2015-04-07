# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ambiente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sede',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('piso', models.IntegerField(default=0)),
                ('piso_por_escalera', models.IntegerField(default=0)),
                ('numero_ambiente', models.IntegerField(default=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tipo_Ambiente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo_ambiente', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tipo_sede',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='sede',
            name='tipo',
            field=models.ForeignKey(to='Sede.Tipo_sede'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ambiente',
            name='ambiente',
            field=models.ForeignKey(to='Sede.Tipo_Ambiente'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ambiente',
            name='sede',
            field=models.ForeignKey(to='Sede.Sede'),
            preserve_default=True,
        ),
    ]
