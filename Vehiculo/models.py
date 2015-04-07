from django.db import models

# Create your models here.
class Tipo_Vehiculo(models.Model):
    """docstring for Tipo_Vehiculo"""
    def __init__(self, *args, **kwargs):
        super(Tipo_Vehiculo, self).__init__(*args, **kwargs)

    tipo_vehiculo = models.CharField(max_length=100, unique=True)
    adicional1 = models.CharField(max_length=250, blank=True)
    adicional2 = models.CharField(max_length=250, blank=True)
    adicional3 = models.CharField(max_length=250, blank=True)
    adicional4 = models.CharField(max_length=250, blank=True)
    activo = models.BooleanField(default=True)

    def __unicode__(self):
        return self.tipo_vehiculo

    class Meta:
        verbose_name_plural = "Tipos de Vehiculos"

class Modelo_Vehiculo(models.Model):
    """docstring for Modelo_Vehiculo"""
    def __init__(self, *args, **kwargs):
        super(Modelo_Vehiculo, self).__init__(*args, **kwargs)

    modelo_vehiculo = models.CharField(max_length=100)
    capacidad_peso = models.IntegerField()
    capacidad_x = models.DecimalField(max_digits=6, decimal_places=2)
    capacidad_y = models.DecimalField(max_digits=6, decimal_places=2)
    capacidad_z = models.DecimalField(max_digits=6, decimal_places=2)
    capacidad_m3 = models.DecimalField(max_digits=6, decimal_places=2)
    adicional1 = models.CharField(max_length=250, blank=True)
    adicional2 = models.CharField(max_length=250, blank=True)
    adicional3 = models.CharField(max_length=250, blank=True)
    adicional4 = models.CharField(max_length=250, blank=True)
    activo = models.BooleanField(default=True)

    def __unicode__(self):
        return self.modelo_vehiculo

    class Meta:
        verbose_name_plural = "Modelos de Vehiculos"

class Vehiculo(models.Model):
    """docstring for Vehiculo"""
    def __init__(self, *args, **kwargs):
        super(Vehiculo, self).__init__(*args, **kwargs)

    numero_vehiculo = models.CharField(max_length=10)
    #mantenimiento_vehiculo = models.ForeignKey()
    vehiculo = models.CharField(max_length=100)
    patente = models.CharField(max_length=100)
    tipo_vehiculo = models.ForeignKey(Tipo_Vehiculo)
    modelo_vehiculo = models.ForeignKey(Modelo_Vehiculo)
    adicional1 = models.CharField(max_length=250, blank=True)
    adicional2 = models.CharField(max_length=250, blank=True)
    adicional3 = models.CharField(max_length=250, blank=True)
    adicional4 = models.CharField(max_length=250, blank=True)
    activo = models.BooleanField(default=True)

    def __unicode__(self):
        return self.vehiculo

    class Meta:
        verbose_name_plural = "Vehiculos"
