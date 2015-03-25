from django.db import models
from Direccion.models import Direccion
from Telefono.models import Telefono

# Create your models here.
class Empresa(models.Model):
    nombre = models.CharField(max_length=250, unique=True)
    documento_fiscal = models.CharField(max_length=50, blank=True)
    Comentarios = models.TextField(blank=True)
    adicional1 = models.CharField(max_length=50, blank=True)
    adicional2 = models.CharField(max_length=50, blank=True)
    adicional3 = models.CharField(max_length=50, blank=True)
    adicional4 = models.CharField(max_length=50, blank=True)
    activo = models.BooleanField(default=True)
    sitio_web = models.CharField(max_length=250, blank=True)

    def __unicode__(self):
        return self.nombre

class Email_empresa(models.Model):
    email = models.EmailField()
    empresa = models.ForeignKey(Empresa)

    def __unicode__(self):
        return u'%s - %s'%(self.email, self.empresa)

class Empresa_direccion(models.Model):
    empresa = models.ForeignKey(Empresa)
    direccion = models.ForeignKey(Direccion)

    def __unicode__(self):
        return u'%s - %s'%(self.empresa, self.direccion)

class Empresa_telefono(models.Model):
    empresa = models.ForeignKey(Empresa)
    telefono = models.ForeignKey(Telefono)

    def __unicode__(self):
        return u'%s - %s'%(self.empresa, self.telefono)
