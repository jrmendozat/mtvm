from django.db import models
from Vehiculo.models import Vehiculo
from Articulo.models import Articulo

# Create your models here.
class Transporte(models.Model):
    """docstring for Transporte"""
    def __init__(self, *args, **kwargs):
        super(Transporte, self).__init__(*args, **kwargs)

    transporte = models.CharField(max_length=100, unique=True)
    adicional1 = models.CharField(max_length=250, blank=True)
    adicional2 = models.CharField(max_length=250, blank=True)
    adicional3 = models.CharField(max_length=250, blank=True)
    adicional4 = models.CharField(max_length=250, blank=True)
    activo = models.BooleanField(default=True)

    def __unicode__(self):
        return self.transporte

    class Meta:
        verbose_name_plural = "Transportes"

class Equipamiento_Transporte(models.Model):
    """docstring for Equipamiento_Transporte"""
    def __init__(self, *args, **kwargs):
        super(Equipamiento_Transporte, self).__init__(*args, **kwargs)

    transporte = models.ForeignKey(Transporte)
    articulo = models.ForeignKey(Articulo)
    descripcion = models.CharField(max_length=100)
    cantidad = models.DecimalField(max_digits=13, decimal_places=2)
    costo = models.DecimalField(max_digits=13, decimal_places=2)
    adicional1 = models.CharField(max_length=250, blank=True)
    adicional2 = models.CharField(max_length=250, blank=True)
    adicional3 = models.CharField(max_length=250, blank=True)
    adicional4 = models.CharField(max_length=250, blank=True)

    def __unicode__(self):
        return self.descripcion

    class Meta:
        verbose_name_plural = "Equipamientos de Transportes"

class Transporte_Vehiculo(models.Model):
    """docstring for Transporte_Vehiculo"""
    def __init__(self, *args, **kwargs):
        super(Transporte_Vehiculo, self).__init__(*args, **kwargs)

    vehiculo = models.ForeignKey(Vehiculo)
    transporte = models.ForeignKey(Transporte)

    def __unicode__(self):
        return u'%s %s'%(self.vehiculo, self.transporte)

    class Meta:
        verbose_name_plural = "Vehiculos de Transportes"

class Transporte_rol(models.Model):
    """docstring for Transporte_rol"""
    def __init__(self, *args, **kwargs):
        super(Transporte_rol, self).__init__(*args, **kwargs)

    rol = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=250)
    adicional1 = models.CharField(max_length=250, blank=True)
    adicional2 = models.CharField(max_length=250, blank=True)
    adicional3 = models.CharField(max_length=250, blank=True)
    adicional4 = models.CharField(max_length=250, blank=True)
    activo = models.BooleanField(default=True)

    def __unicode__(self):
        return self.descripcion

    class Meta:
        verbose_name_plural = "Rol de Transportes"

class Transporte_cuadrilla(models.Model):
    """docstring for Transporte_cuadrilla"""
    def __init__(self, *args, **kwargs):
        super(Transporte_cuadrilla, self).__init__(*args, **kwargs)

    transporte = models.ForeignKey(Transporte)
    rol = models.ForeignKey(Transporte_rol)
    #trabajador = models.ForeignKey()
    observaciones = models.CharField(max_length=250)
    adicional1 = models.CharField(max_length=250, blank=True)
    adicional2 = models.CharField(max_length=250, blank=True)
    adicional3 = models.CharField(max_length=250, blank=True)
    adicional4 = models.CharField(max_length=250, blank=True)
