from django.db import models

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

