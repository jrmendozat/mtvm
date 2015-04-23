#encoding:utf-8
from django.db import models
#from django.contrib.auth.models import User
from Tipo_cliente.models import Tipo_cliente
from Condicion_pago.models import Condicion_pago
from Segmento.models import Segmento
from Direccion.models import Direccion
from Telefono.models import Telefono
from Empresa.models import Empresa
from Persona.models import Persona
from Sede.models import Sede

# Create your models here.


class Cliente(models.Model):
    """docstring for Cliente"""
    def __init__(self, *args, **kwargs):
        super(Cliente, self).__init__(*args, **kwargs)

    nombre_principal = models.CharField(max_length=250)
    tipo_cliente = models.ForeignKey(Tipo_cliente, blank=True)
    condicion_pago = models.ForeignKey(Condicion_pago, blank=True)
    monto_credito = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    segmento = models.ForeignKey(Segmento, blank=True)
    #login = models.ForeignKey(User)
    sitio_web = models.URLField(blank=True)
    comentarios = models.TextField(blank=True)
    adicional1 = models.CharField(max_length=50, blank=True)
    adicional2 = models.CharField(max_length=50, blank=True)
    adicional3 = models.CharField(max_length=50, blank=True)
    adicional4 = models.CharField(max_length=50, blank=True)
    activo = models.BooleanField(default=True)

    def __unicode__(self):
        return self.nombre_principal

    class Meta:
        verbose_name_plural = "Clientes"


class Email(models.Model):

    email = models.EmailField()
    cliente = models.ForeignKey(Cliente, default=1)

    def __unicode__(self):
        return self.email


class Cliente_Direccion(models.Model):
    cliente = models.ForeignKey(Cliente, default=1)
    direc = models.OneToOneField(Direccion, default=1, blank=True)
    sede1 = models.OneToOneField(Sede, null=True, blank=True)

    def __unicode__(self):
        return u' %s - %s' % (self.cliente, self.direc)

    class Meta:
        verbose_name = "Direccion del cliente"
        verbose_name_plural = "Direcciones del cliente"


class Cliente_telefono(models.Model):
    cliente = models.ForeignKey(Cliente, default=1)
    telefono = models.OneToOneField(Telefono, default=1, blank=True)

    def __unicode__(self):
        return u' %s - %s' % (self.cliente, self.telefono)

    class Meta:
        verbose_name = "Telefono del cliente"
        verbose_name_plural = "Telefonos del cliente"


class Cliente_empresa(models.Model):
    cliente = models.ForeignKey(Cliente)
    empresa = models.ForeignKey(Empresa)
    principal = models.BooleanField(default=True)

    def __unicode__(self):
        return u' %s - %s' % (self.cliente, self.empresa)

    class Meta:
        verbose_name = "Empresa del cliente"
        verbose_name_plural = "Empresas del cliente"


class Cliente_persona(models.Model):
    cliente = models.ForeignKey(Cliente)
    persona = models.ForeignKey(Persona)
    principal = models.BooleanField(default=True)

    def __unicode__(self):
        return u' %s - %s' % (self.cliente, self.persona)

    class Meta:
        verbose_name = "Persona del cliente"
        verbose_name_plural = "Personas del cliente"
