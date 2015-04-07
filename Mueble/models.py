from django.db import models
from Sede.models import Tipo_Ambiente

# Create your models here.
class Tamanio_Mueble(models.Model):
    """docstring for Tamanio_Mueble"""
    def __init__(self, *args, **kwargs):
        super(Tamanio_Mueble, self).__init__(*args, **kwargs)

    tipo_tamanio = models.CharField(max_length=100)
    adicional1 = models.CharField(max_length=250)
    adicional2 = models.CharField(max_length=250)
    adicional3 = models.CharField(max_length=250)
    adicional4 = models.CharField(max_length=250)
    activo = models.BooleanField(default=True)

    def __unicode__(self):
        return self.tipo_tamanio

    class Meta:
        verbose_name_plural = "Tamanios de Muebles"

class Tipo_Peso(models.Model):
    """docstring for Tipo_Peso"""
    def __init__(self, *args, **kwargs):
        super(Tipo_Peso, self).__init__(*args, **kwargs)

    tipo_peso = models.CharField(max_length=100)
    peso_promedio = models.DecimalField(max_digits = 13, \
        decimal_places = 2)
    adicional1 = models.CharField(max_length=250)
    adicional2 = models.CharField(max_length=250)
    adicional3 = models.CharField(max_length=250)
    adicional4 = models.CharField(max_length=250)
    activo = models.BooleanField(default=True)

    def __unicode__(self):
        return self.tipo_peso

    class Meta:
        verbose_name_plural = "Tipos de Pesos"

class Tipo_Fragilidad(models.Model):
    """docstring for Tipo_Fragilidad"""
    def __init__(self, *args, **kwargs):
        super(Tipo_Fragilidad, self).__init__(*args, **kwargs)

    tipo_fragilidad = models.CharField(max_length=100)
    adicional1 = models.CharField(max_length=250)
    adicional2 = models.CharField(max_length=250)
    adicional3 = models.CharField(max_length=250)
    adicional4 = models.CharField(max_length=250)
    activo = models.BooleanField(default=True)

    def __unicode__(self):
        return self.tipo_fragilidad

    class Meta:
        verbose_name_plural = "Tipos de Fradilidad"

class Familia_Mueble(models.Model):
    """docstring for Familia_Mueble"""
    def __init__(self, *args, **kwargs):
        super(Familia_Mueble, self).__init__(*args, **kwargs)

    familia_muebles = models.CharField(max_length=100)
    adicional1 = models.CharField(max_length=250)
    adicional2 = models.CharField(max_length=250)
    adicional3 = models.CharField(max_length=250)
    adicional4 = models.CharField(max_length=250)
    activo = models.BooleanField(default=True)

    def __unicode__(self):
        return self.familia_muebles

    class Meta:
        verbose_name_plural = "Familia de Muebles"

class Mueble(models.Model):
    """docstring for Mueble"""
    def __init__(self, *args, **kwargs):
        super(Mueble, self).__init__(*args, **kwargs)

    mueble = models.CharField(max_length=250)
    trasladable = models.BooleanField(default=True)
    ancho = models.DecimalField(max_digits=13, decimal_places=2)
    alto = models.DecimalField(max_digits=13, decimal_places=2)
    largo = models.DecimalField(max_digits=13, decimal_places=2)
    peso = models.DecimalField(max_digits=13, decimal_places=2)
    familia = models.ForeignKey(Familia_Mueble)
    tipo_fragil = models.ForeignKey(Tipo_Fragilidad)
    capacidad_interna = models.DecimalField(max_digits=13, decimal_places=2)
    capacidad_carga = models.DecimalField(max_digits=13, decimal_places=2)
    apilable = models.BooleanField(default=True)
    tipo_ambiente = models.ForeignKey(Tipo_Ambiente)
    tipo_tamanio = models.ForeignKey(Tamanio_Mueble)
    tipo_peso = models.ForeignKey(Tipo_Peso)
    adicional1 = models.CharField(max_length=250)
    adicional2 = models.CharField(max_length=250)
    adicional3 = models.CharField(max_length=250)
    adicional4 = models.CharField(max_length=250)
    observaciones = models.TextField()
    activo = models.BooleanField(default=True)

    def __unicode__(self):
        return self.mueble

    class Meta:
        verbose_name_plural = "Muebles"


