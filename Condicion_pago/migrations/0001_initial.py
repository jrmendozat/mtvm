# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Condicion_pago',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('condicion', models.CharField(max_length=10)),
                ('dias', models.PositiveIntegerField()),
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
    ]
