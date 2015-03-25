from django.db import models
from django.contrib import admin

# Create your models here.
class Segmento(models.Model):

    segmento = models.CharField(max_length=50, unique=True)
    adicional1 = models.CharField(max_length=50, blank=True)
    adicional2 = models.CharField(max_length=50, blank=True)
    adicional3 = models.CharField(max_length=50, blank=True)
    adicional4 = models.CharField(max_length=50, blank=True)
    activo = models.BooleanField(default=True)

    def __unicode__(self):
        return self.segmento

admin.site.register(Segmento)
