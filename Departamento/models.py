from django.db import models

# Create your models here.
class Disenio(models.Model):
    linea_tipo = models.IntegerField()
    linea_grosor = models.IntegerField()
    linea_color = models.CharField(max_length=7, default='000000')
    relleno_color = models.CharField(max_length=7, default='FFFFFF')
    ancho = models.IntegerField(default=64)
    alto = models.IntegerField(default=40)

    class Meta:
        verbose_name = "Diseno"
        verbose_name_plural = "Disenos"

class Jerarquia(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    disenio = models.ForeignKey(Disenio)

class Departamento(models.Model):
    codigo = models.CharField(max_length=20, blank=True)
    nombre = models.CharField(max_length=100, unique=True)
    unidad_superior = models.ForeignKey('self', blank=True, related_name='unidad_superior1')
    tipo_jerarquia = models.ForeignKey(Jerarquia)
    disenio = models.ForeignKey(Disenio)
    activo = models.BooleanField(default=True)

    def __unicode__(self):
        return self.nombre

class Cargo_tipo(models.Model):
    cargo_tipo = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return self.cargo_tipo

    class Meta:
        verbose_name = "Tipo de cargo"
        verbose_name_plural = "Tipos de cargo"

class Cargo(models.Model):
    codigo = models.CharField(max_length=20, blank=True)
    nombre = models.CharField(max_length=100, unique=True)
    departamento = models.ForeignKey(Departamento)
    cargo_supervisor = models.ForeignKey('self', blank=True, related_name='cargo_supervisor1')
    cargo_tipo = models.ForeignKey(Cargo_tipo)

    def __unicode__(self):
        return self.nombre
