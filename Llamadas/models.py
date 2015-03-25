#encoding: utf-8
from django.db import models
from django.contrib import admin
from Direccion.models import Zona

#declaración de variables
ENTRADA = '1'
SALIENTE = '2'
TIPO_LLAMADA = (
    (ENTRADA, 'Entrante'),
    (SALIENTE, 'Saliente'),)

SEGUIMIENTO = (
    ('Cotizacion Mudanza', 'Cotización Mudanza'),
    ('Confirmacion Mudanza', 'Confirmación Mudanza'),
    ('Cambio de Fecha Mudanza', 'Cambio de Fecha Mudanza'),
    ('Cambio Visita Cotizador', 'Cambio Visita Cotizador'),
    ('Cancela Visita Cotizador', 'Cancela Visita Cotizador'),
    ('Cancelacion Mudanza', 'Cancelación Mudanza'),
    ('Seguimiento de Ventas', 'Seguimiento de Ventas'),
    ('Consulta', 'Consulta'),
    ('Gestion de Canastos', 'Gestión de Canastos'),
    ('Llamada Perdida', 'Llamada Perdida'),
    ('Interno', 'Interno'),
    ('Empresas', 'Empresas'),
    ('Control de Calidad', 'Control de Calidad'),
    ('N/S', 'N/S'),
    ('Otros', 'Otros'),
    ('Reclamo Mudanza', 'Reclamo Mudanza'),)

class llamada(models.Model):
    fecha = models.DateField(auto_now_add=True)
    horaini = models.TimeField(auto_now_add=True)
    horafin = models.TimeField()
    tipollamada = models.CharField(max_length=1, choices=TIPO_LLAMADA, default=ENTRADA)
    status = models.CharField(max_length=10)
    nrocotizacion = models.CharField(max_length=20)
    nombrecli = models.CharField(max_length=250)
    telefono = models.CharField(max_length=15)
    celular = models.CharField(max_length=15)
    motivo = models.CharField(max_length=50, choices=SEGUIMIENTO)
    observacion = models.CharField(max_length=250)
    direccorigen = models.CharField(max_length=250)
    barrioorigen = models.CharField(max_length=100)
    zonaorigen = models.ForeignKey(Zona, related_name='zona1')
    tipoorigen = models.CharField(max_length=100)
    ambptos = models.PositiveIntegerField()
    direccdestino = models.CharField(max_length=250)
    barriodestino = models.CharField(max_length=100)
    zonadestino = models.ForeignKey(Zona, related_name='zona2')
    fuentereclutamiento = models.CharField(max_length=200)
    barriopublicidad = models.CharField(max_length=100)
    email = models.EmailField()
    fechacotiz = models.DateField()
    horacotiz = models.TimeField()
    nombrecotiz = models.CharField(max_length=250)
    nombrequieningreso = models.CharField(max_length=250)
    duracionllamada = models.TimeField() #horafin-horaini

    def __unicode__(self):
        return u'%s %s'%(self.nrocotizacion, self.nombrecli)

admin.site.register(llamada)
