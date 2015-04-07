from django.db import models
from Telefono.models import Telefono
from Direccion.models import Direccion

# Create your models here.
class Tratamiento(models.Model):
    tratamiento = models.CharField(max_length=10)

    def __unicode__(self):
        return self.tratamiento

class Sexo(models.Model):
    sexo = models.CharField(max_length=25, unique=True)

    def __unicode__(self):
        return self.sexo

class Persona(models.Model):
    """docstring for Persona"""
    def __init__(self, *args, **kwargs):
        super(Persona, self).__init__(*args, **kwargs)

    apellido1 = models.CharField(max_length=100)
    apellido2 = models.CharField(max_length=100, blank=True)
    nombre1 = models.CharField(max_length=100)
    nombre2 = models.CharField(max_length=100, blank=True)
    tratamiento = models.ForeignKey(Tratamiento, blank=True)
    sexo = models.ForeignKey(Sexo)
    documento_identidad = models.CharField(max_length=50, blank=True)
    documento_fiscal = models.CharField(max_length=50, blank=True)
    comentarios = models.TextField(blank=True)

    def __unicode__(self):
        return u'%s - %s'%(self.apellido1, self.nombre1)

class Persona_evento(models.Model):
    evento = models.CharField(max_length=250)
    fecha_evento = models.DateField()
    persona = models.ForeignKey(Persona)

    def __unicode__(self):
        return self.evento

class Persona_telefono(models.Model):
    persona = models.ForeignKey(Persona)
    telefono = models.OneToOneField(Telefono)

    def __unicode__(self):
        return u'%s - %s'%(self.persona, self.telefono)

class Persona_Direccion(models.Model):
    persona = models.ForeignKey(Persona)
    direccion = models.OneToOneField(Direccion)

    def __unicode__(self):
        return u'%s - %s'%(self.persona, self.direccion)

class Tipo_relacion(models.Model):
    tipo_relacion = models.CharField(max_length=250)

    def __unicode__(self):
        return self.tipo_relacion

class Persona_relacion(models.Model):
    tipo_relacion = models.ForeignKey(Tipo_relacion)
    persona = models.ForeignKey(Persona)
