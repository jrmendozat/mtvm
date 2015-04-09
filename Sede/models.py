from django.db import models
#from Cliente.models import Cliente_Direccion

# Create your models here.
class Tipo_sede(models.Model):
    """docstring for Tipo_sede"""
    def __init__(self, *args, **kwargs):
        super(Tipo_sede, self).__init__(*args, **kwargs)

    nombre = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = "Tipo de sede"
        verbose_name_plural = "Tipos de sede"

class Sede(models.Model):
    """docstring for Sede"""
    def __init__(self, *args, **kwargs):
        super(Sede, self).__init__(*args, **kwargs)

    tipo = models.ForeignKey(Tipo_sede)
    sede = models.CharField(max_length=250)
    piso = models.IntegerField(default=0)
    piso_por_escalera = models.IntegerField(default=0)
    numero_ambiente = models.IntegerField(default=1)
    #direccion_cliente = models.OneToOneField(Cliente_Direccion)

    def __unicode__(self):
        return u'%s'%(self.tipo)

    class Meta:
        verbose_name = "Sede"
        verbose_name_plural = "Sedes"

class Tipo_Ambiente(models.Model):
    """docstring for Tipo_Ambiente"""
    def __init__(self, *args, **kwargs):
        super(Tipo_Ambiente, self).__init__(*args, **kwargs)

    tipo_ambiente = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return self.tipo_ambiente

    class Meta:
        verbose_name = "Tipo de ambiente"
        verbose_name_plural = "Tipos de ambientes"

class Ambiente(models.Model):
    """docstring for Ambiente"""
    def __init__(self, *args, **kwargs):
        super(Ambiente, self).__init__(*args, **kwargs)

    ambiente = models.ForeignKey(Tipo_Ambiente)
    sede = models.ForeignKey(Sede)

    def __unicode__(self):
        return u'%s - %s'%(self.ambiente, self.sede)

    class Meta:
        verbose_name = "Ambiente"
        verbose_name_plural = "Ambientes"
