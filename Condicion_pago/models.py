#encoding:utf-8
from django.db import models
from django.contrib import admin

# Create your models here.
class Condicion_pago(models.Model):
    """docstring for Condicion_pago"""
    def __init__(self, *args, **kwargs):
        super(Condicion_pago, self).__init__(*args, **kwargs)

    condicion = models.CharField(max_length=50, unique=True)
    dias = models.PositiveIntegerField()
    adicional1 = models.CharField(max_length=50, blank=True)
    adicional2 = models.CharField(max_length=50, blank=True)
    adicional3 = models.CharField(max_length=50, blank=True)
    adicional4 = models.CharField(max_length=50, blank=True)
    activo = models.BooleanField(default=True)

    def __unicode__(self):
        return self.condicion

    class Meta:
        verbose_name = "Condicion de pago"
        verbose_name_plural = "Condiciones de pago"

admin.site.register(Condicion_pago)
