from django.db import models
#from Cliente.models import Cliente_Direccion

# Create your models here.
class Tipo_sede(models.Model):

    nombre = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = "Tipo de sede"
        verbose_name_plural = "Tipos de sede"

class Sede(models.Model):

    tipo = models.ForeignKey(Tipo_sede)
    piso = models.IntegerField(default=0)
    piso_por_escalera = models.IntegerField(default=0)
    numero_ambiente = models.IntegerField(default=1)
    #direccion_cliente = models.OneToOneField(Cliente_Direccion)

    def __unicode__(self):
        return u'%s'%(self.tipo)

    class Meta:
        verbose_name = "Sede"
        verbose_name_plural = "Sedes"

class Tipo_ambiente(models.Model):

    tipo_ambiente = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return self.tipo_ambiente

    class Meta:
        verbose_name = "Tipo de ambiente"
        verbose_name_plural = "Tipos de ambientes"

class Ambiente(models.Model):

    ambiente = models.ForeignKey(Tipo_ambiente)
    sede = models.ForeignKey(Sede)

    def __unicode__(self):
        return u'%s - %s'%(self.ambiente, self.sede)

    class Meta:
        verbose_name = "Ambiente"
        verbose_name_plural = "Ambientes"
