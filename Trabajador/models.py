from django.db import models
from Departamento.models import Cargo
from Persona.models import Persona
# Create your models here.
class Tipo_status(models.Model):
    tipo_status = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return self.tipo_status

    class Meta:
        verbose_name_plural = "Tipos de status de trabajadores"

class Trabajador(models.Model):
    cargo = models.ForeignKey(Cargo)
    persona = models.ForeignKey(Persona)
    codigo_trabajador = models.CharField(max_length=50, blank=True)
    fecha_ingreso = models.DateField()
    fecha_retiro = models.DateField(blank=True)

    def __unicode__(self):
        return self.persona

    class Meta:
        verbose_name_plural = "Trabajadores"

class Trabajador_status(models.Model):
    tipo_status = models.ForeignKey(Tipo_status)
    trabajador = models.ForeignKey(Trabajador)
    fecha_inicio_status = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return u'%s - %s'%(str(self.tipo_status), str(self.trabajador))

    class Meta:
        verbose_name_plural = "Status de trabajadores"
