from django.db import models
from Segmento.models import Segmento
from Condicion_pago.models import Condicion_pago
from Telefono.models import Telefono
from Direccion.models import Direccion

# Create your models here.
class Tipo_Proveedor(models.Model):
    """docstring for Tipo_Proveedor"""
    def __init__(self, *args, **kwargs):
        super(Tipo_Proveedor, self).__init__(*args, **kwargs)

    tipo_proveedor = models.CharField(max_length=100, unique=True)
    adicional1 = models.CharField(max_length=250, blank=True)
    adicional2 = models.CharField(max_length=250, blank=True)
    adicional3 = models.CharField(max_length=250, blank=True)
    adicional4 = models.CharField(max_length=250, blank=True)
    activo = models.BooleanField(default=True)

    def __unicode__(self):
        return self.tipo_proveedor

    class Meta:
        verbose_name_plural = "Tipos proveedores"

class Proveedor(models.Model):
    """docstring for Proveedor"""
    def __init__(self, *args, **kwargs):
        super(Proveedor, self).__init__(*args, **kwargs)

    proveedor = models.CharField(max_length=250)
    tipo_proveedor = models.ForeignKey(Tipo_Proveedor)
    segmento = models.ForeignKey(Segmento)
    condicion_pago = models.ForeignKey(Condicion_pago)
    monto_credito = models.DecimalField(max_digits=13, decimal_places=2)
    sitio_web = models.URLField()
    comentarios = models.TextField()
    adicional1 = models.CharField(max_length=250, blank=True)
    adicional2 = models.CharField(max_length=250, blank=True)
    adicional3 = models.CharField(max_length=250, blank=True)
    adicional3 = models.CharField(max_length=250, blank=True)
    activo = models.BooleanField(default=True)

    def __unicode__(self):
        return self.proveedor

    class Meta:
        verbose_name_plural = "Proveedores"

class Proveedor_Telefono(models.Model):
    """docstring for Proveedor_Telefono"""
    def __init__(self, *args, **kwargs):
        super(Proveedor_Telefono, self).__init__(*args, **kwargs)

    proveedor = models.ForeignKey(Proveedor)
    telefono = models.ForeignKey(Telefono)

    def __unicode__(self):
        return u'%s %s'%(self.proveedor, self.telefono)

    class Meta:
        verbose_name_plural = "Telefonos de proveedores"

class Proveedor_Direccion(models.Model):
    """docstring for Proveedor_Direccion"""
    def __init__(self, *args, **kwargs):
        super(Proveedor_Direccion, self).__init__(*args, **kwargs)

    proveedor = models.ForeignKey(Proveedor)
    direccion = models.OneToOneField(Direccion)

    def __unicode__(self):
        return u'%s %s'%(self.proveedor, self.direccion)

    class Meta:
        verbose_name_plural = "Direcciones de proveedores"

class Email_Proveedor(models.Model):
    """docstring for Email_Proveedor"""
    def __init__(self, *args, **kwargs):
        super(Email_Proveedor, self).__init__(*args, **kwargs)

    proveedor = models.ForeignKey(Proveedor)
    email = models.EmailField()

    def __unicode__(self):
        return self.email

    class Meta:
        verbose_name_plural = "Email de proveedores"
