from django.db import models

# Create your models here.
class Pais(models.Model):
    """docstring for Pais"""
    def __init__(self, *args, **kwargs):
        super(Pais, self).__init__(*args, **kwargs)

    pais = models.CharField(max_length=250, unique=True)

    def __unicode__(self):
        return self.pais

    class Meta:
        verbose_name = "Pais"
        verbose_name_plural = "Paises"

class Provincia(models.Model):
    """docstring for Provincia"""
    def __init__(self, *args, **kwargs):
        super(Provincia, self).__init__(*args, **kwargs)

    provincia = models.CharField(max_length=100, unique=True)
    pais = models.ForeignKey(Pais)

    def __unicode__(self):
        return self.provincia

class Ciudad(models.Model):
    """docstring for Ciudad"""
    def __init__(self, *args, **kwargs):
        super(Ciudad, self).__init__(*args, **kwargs)

    ciudad = models.CharField(max_length=100, unique=True)
    provincia = models.ForeignKey(Provincia)

    def __unicode__(self):
        return self.ciudad

    class Meta:
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"

class Zona(models.Model):
    """docstring for Zona"""
    def __init__(self, *args, **kwargs):
        super(Zona, self).__init__(*args, **kwargs)

    zona = models.CharField(max_length=100, unique=True)
    cuidad = models.ForeignKey(Ciudad)

    def __unicode__(self):
        return self.zona

class Tipo_direccion(models.Model):
    """docstring for Tipo_direccion"""
    def __init__(self, *args, **kwargs):
        super(Tipo_direccion, self).__init__(*args, **kwargs)

    tipo_direccion = models.CharField(max_length=10)
    activo = models.BooleanField(default=True)

    def __unicode__(self):
        return self.tipo_direccion

    class Meta:
        verbose_name = "Tipo de direccion"
        verbose_name_plural = "Tipos de direccion"

class Direccion(models.Model):
    """docstring for Direccion"""
    def __init__(self, *args, **kwargs):
        super(Direccion, self).__init__(*args, **kwargs)

    direccion = models.CharField(max_length=500)
    punto_referencia = models.CharField(max_length=250)
    zip1 = models.CharField(max_length=10, blank=True)
    tipo_direccion = models.ForeignKey(Tipo_direccion)
    zona = models.ForeignKey(Zona)

    def __unicode__(self):
        return self.direccion

    class Meta:
        verbose_name = "Direccion"
        verbose_name_plural = "Direcciones"
