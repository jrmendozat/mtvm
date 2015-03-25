from django.db import models

# Create your models here.
class Tipo_precio(models.Model):
    """docstring for Tipo_precio"""
    def __init__(self, *args, **kwargs):
        super(Tipo_precio, self).__init__(*args, **kwargs)

    nombre = models.CharField(max_length=50, unique=True)
    activo = models.BooleanField(default=True)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Tipos de precios"

class Tipo_cliente(models.Model):
    """docstring for Tipo_cliente"""
    def __init__(self, *args, **kwargs):
        super(Tipo_cliente, self).__init__(*args, **kwargs)

    descripcion = models.CharField(max_length=50, unique=True)
    precio = models.ForeignKey(Tipo_precio)
    adicional1 = models.CharField(max_length=50, blank=True)
    adicional2 = models.CharField(max_length=50, blank=True)
    adicional3 = models.CharField(max_length=50, blank=True)
    adicional4 = models.CharField(max_length=50, blank=True)
    activo = models.BooleanField(default=True)

    def __unicode__(self):
        return self.descripcion

    class Meta:
        verbose_name_plural = "Tipos de clientes"
