# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tipo_cliente', '0004_auto_20150319_1648'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('articulo', models.CharField(max_length=100)),
                ('adicional1', models.CharField(max_length=250, blank=True)),
                ('adicional2', models.CharField(max_length=250, blank=True)),
                ('adicional3', models.CharField(max_length=250, blank=True)),
                ('adicional4', models.CharField(max_length=250, blank=True)),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Articulos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Articulo_Clase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('clase', models.CharField(max_length=100)),
                ('adicional1', models.CharField(max_length=250, blank=True)),
                ('adicional2', models.CharField(max_length=250, blank=True)),
                ('adicional3', models.CharField(max_length=250, blank=True)),
                ('adicional4', models.CharField(max_length=250, blank=True)),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Clases de Articulos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Articulo_Costo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('monto', models.DecimalField(max_digits=13, decimal_places=2)),
                ('desde', models.DateField()),
                ('hasta', models.DateField()),
                ('descripcion', models.CharField(max_length=100)),
                ('activo', models.BooleanField(default=True)),
                ('articulo', models.ForeignKey(to='Articulo.Articulo')),
            ],
            options={
                'verbose_name_plural': 'Articulos Costos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Articulo_Precio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('monto', models.DecimalField(max_digits=13, decimal_places=2)),
                ('desde', models.DateField()),
                ('hasta', models.DateField()),
                ('descripcion', models.CharField(max_length=250)),
                ('activo', models.BooleanField(default=True)),
                ('articulo', models.ForeignKey(to='Articulo.Articulo')),
                ('tipo_precio', models.ForeignKey(to='Tipo_cliente.Tipo_precio')),
            ],
            options={
                'verbose_name_plural': 'Precios de Articulos ',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Articulo_Proveedor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('proveedor', models.IntegerField()),
                ('observacion', models.TextField()),
                ('adicional1', models.CharField(max_length=250)),
                ('adicional2', models.CharField(max_length=250)),
                ('adicional3', models.CharField(max_length=250)),
                ('adicional4', models.CharField(max_length=250)),
                ('articulo', models.ForeignKey(to='Articulo.Articulo')),
            ],
            options={
                'verbose_name_plural': 'Provedores de Articulos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Articulo_Subclase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subclase', models.CharField(max_length=100)),
                ('adicional1', models.CharField(max_length=250, blank=True)),
                ('adicional2', models.CharField(max_length=250, blank=True)),
                ('adicional3', models.CharField(max_length=250, blank=True)),
                ('adicional4', models.CharField(max_length=250, blank=True)),
                ('activo', models.BooleanField(default=True)),
                ('clase', models.ForeignKey(to='Articulo.Articulo_Clase')),
            ],
            options={
                'verbose_name_plural': 'Subclases de Articulos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Articulo_Unidad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('principal', models.BooleanField()),
                ('articulo', models.ForeignKey(to='Articulo.Articulo')),
                ('relacion_principal', models.ForeignKey(to='Articulo.Articulo_Unidad')),
            ],
            options={
                'verbose_name_plural': 'Unidades de Articulos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Categoria_Articulo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('categoria', models.CharField(max_length=100)),
                ('adicional1', models.CharField(max_length=250, blank=True)),
                ('adicional2', models.CharField(max_length=250, blank=True)),
                ('adicional3', models.CharField(max_length=250, blank=True)),
                ('adicional4', models.CharField(max_length=250, blank=True)),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Categorias de Articulos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subcategoria_articulo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subcategoria', models.CharField(max_length=100)),
                ('adicional1', models.CharField(max_length=250, blank=True)),
                ('adicional2', models.CharField(max_length=250, blank=True)),
                ('adicional3', models.CharField(max_length=250, blank=True)),
                ('adicional4', models.CharField(max_length=250, blank=True)),
                ('activo', models.BooleanField(default=True)),
                ('categoria', models.ForeignKey(to='Articulo.Categoria_Articulo')),
            ],
            options={
                'verbose_name_plural': 'Subcategorias de Articulos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tipo_Costo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo_costo', models.CharField(max_length=100)),
                ('monto', models.DecimalField(max_digits=13, decimal_places=2)),
                ('desde', models.DateField()),
                ('hasta', models.DateField()),
                ('descripcion', models.CharField(max_length=100)),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Tipos de Costos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Unidad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('unidad', models.CharField(max_length=100)),
                ('adicional1', models.CharField(max_length=250)),
                ('adicional2', models.CharField(max_length=250)),
                ('adicional3', models.CharField(max_length=250)),
                ('adicional4', models.CharField(max_length=250)),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Unidades',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='articulo_unidad',
            name='unidad',
            field=models.ForeignKey(to='Articulo.Unidad'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='articulo_costo',
            name='tipo_costo',
            field=models.ForeignKey(to='Articulo.Tipo_Costo'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='articulo',
            name='subcategoria',
            field=models.ForeignKey(to='Articulo.Subcategoria_articulo'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='articulo',
            name='subclase',
            field=models.ForeignKey(to='Articulo.Articulo_Subclase'),
            preserve_default=True,
        ),
    ]
