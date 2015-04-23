from django.db import models


# Create your models here.
class Segmento(models.Model):

    """docstring for Segmento"""
    def __init__(self, *args, **kwargs):
        super(Segmento, self).__init__(*args, **kwargs)

    segmento = models.CharField(max_length=50, unique=True)
    adicional1 = models.CharField(max_length=50, blank=True)
    adicional2 = models.CharField(max_length=50, blank=True)
    adicional3 = models.CharField(max_length=50, blank=True)
    adicional4 = models.CharField(max_length=50, blank=True)
    activo = models.BooleanField(default=True)

    def __unicode__(self):
        return self.segmento

    class Meta:
        verbose_name_plural = "Segmentos"
