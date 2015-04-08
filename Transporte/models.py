from django.db import models
from Vehiculo.models import Vehiculo

# Create your models here.
class Transporte(models.Model):
    """docstring for Transporte"""
    def __init__(self, *args, **kwargs):
        super(Transporte, self).__init__(*args, **kwargs)

    transporte = models.CharField(max_length=100)
    adicional1 = models.CharField(max_length=250, blank=True)
    adicional2 = models.CharField(max_length=250, blank=True)
    adicional3 = models.CharField(max_length=250, blank=True)
    adicional4 = models.CharField(max_length=250, blank=True)
    activo = models.BooleanField(default=True)

    def __unicode__(self):
        return self.transporte

    class Meta:
        verbose_name_plural = "Transportes"

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
