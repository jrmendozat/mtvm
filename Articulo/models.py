from django.db import models
from Tipo_cliente.models import Tipo_precio
from Proveedor.models import Proveedor

# Create your models here.
class Articulo_Clase(models.Model):
    """docstring for Articulo_Clase"""
    def __init__(self, *args, **kwargs):
        super(Articulo_Clase, self).__init__(*args, **kwargs)

    clase = models.CharField(max_length=100)
    adicional1 = models.CharField(max_length=250, blank=True)
    adicional2 = models.CharField(max_length=250, blank=True)
    adicional3 = models.CharField(max_length=250, blank=True)
    adicional4 = models.CharField(max_length=250, blank=True)
    activo = models.BooleanField(default=True)

    def __unicode__(self):
        return self.clase

    class Meta:
        verbose_name_plural = "Clases de Articulos"

class Articulo_Subclase(models.Model):
    """docstring for Articulo_Subclase"""
    def __init__(self, *args, **kwargs):
        super(Articulo_Subclase, self).__init__(*args, **kwargs)

    clase = models.ForeignKey(Articulo_Clase)
    subclase = models.CharField(max_length=100)
    adicional1 = models.CharField(max_length=250, blank=True)
    adicional2 = models.CharField(max_length=250, blank=True)
    adicional3 = models.CharField(max_length=250, blank=True)
    adicional4 = models.CharField(max_length=250, blank=True)
    activo = models.BooleanField(default=True)

    def __unicode__(self):
        return self.subclase

    class Meta:
        verbose_name_plural = "Subclases de Articulos"

class Categoria_Articulo(models.Model):
    """docstring for Categoria_Articulo"""
    def __init__(self, *args, **kwargs):
        super(Categoria_Articulo, self).__init__(*args, **kwargs)

    categoria = models.CharField(max_length=100)
    adicional1 = models.CharField(max_length=250, blank=True)
    adicional2 = models.CharField(max_length=250, blank=True)
    adicional3 = models.CharField(max_length=250, blank=True)
    adicional4 = models.CharField(max_length=250, blank=True)
    activo = models.BooleanField(default=True)

    def __unicode__(self):
        return self.categoria

    class Meta:
        verbose_name_plural = "Categorias de Articulos"

class Subcategoria_articulo(models.Model):
    """docstring for Subcategoria_articulo"""
    def __init__(self, *args, **kwargs):
        super(Subcategoria_articulo, self).__init__(*args, **kwargs)

    categoria = models.ForeignKey(Categoria_Articulo)
    subcategoria = models.CharField(max_length=100)
    adicional1 = models.CharField(max_length=250, blank=True)
    adicional2 = models.CharField(max_length=250, blank=True)
    adicional3 = models.CharField(max_length=250, blank=True)
    adicional4 = models.CharField(max_length=250, blank=True)
    activo = models.BooleanField(default=True)

    def __unicode__(self):
        return self.subcategoria

    class Meta:
        verbose_name_plural = "Subcategorias de Articulos"

class Articulo(models.Model):
    """docstring for Articulo"""
    def __init__(self, *args, **kwargs):
        super(Articulo, self).__init__(*args, **kwargs)

    articulo = models.CharField(max_length=100)
    subcategoria = models.ForeignKey(Subcategoria_articulo)
    subclase = models.ForeignKey(Articulo_Subclase)
    adicional1 = models.CharField(max_length=250, blank=True)
    adicional2 = models.CharField(max_length=250, blank=True)
    adicional3 = models.CharField(max_length=250, blank=True)
    adicional4 = models.CharField(max_length=250, blank=True)
    activo = models.BooleanField(default=True)

    def __unicode__(self):
        return self.articulo

    class Meta:
        verbose_name_plural = "Articulos"

class Tipo_Costo(models.Model):
    """docstring for Tipo_Costo"""
    def __init__(self, *args, **kwargs):
        super(Tipo_Costo, self).__init__(*args, **kwargs)

    tipo_costo = models.CharField(max_length=100)
    monto = models.DecimalField(max_digits=13, decimal_places=2)
    desde = models.DateField()
    hasta = models.DateField()
    descripcion = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)

    def __unicode__(self):
        return self.tipo_costo

    class Meta:
        verbose_name_plural = "Tipos de Costos"

class Articulo_Costo(models.Model):
    """docstring for Articulo_Costo"""
    def __init__(self, *args, **kwargs):
        super(Articulo_Costo, self).__init__(*args, **kwargs)

    articulo = models.ForeignKey(Articulo)
    tipo_costo = models.ForeignKey(Tipo_Costo)
    monto = models.DecimalField(max_digits=13, decimal_places=2)
    desde = models.DateField()
    hasta = models.DateField()
    descripcion = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)

    def __unicode__(self):
        return u'%s %s'%(self.articulo, self.tipo_costo)

    class Meta:
        verbose_name_plural = "Costos de Articulos"

class Unidad(models.Model):
    """docstring for Unidad"""
    def __init__(self, *args, **kwargs):
        super(Unidad, self).__init__(*args, **kwargs)

    unidad = models.CharField(max_length=100)
    adicional1 = models.CharField(max_length=250, blank=True)
    adicional2 = models.CharField(max_length=250, blank=True)
    adicional3 = models.CharField(max_length=250, blank=True)
    adicional4 = models.CharField(max_length=250, blank=True)
    activo = models.BooleanField(default=True)

    def __unicode__(self):
        return self.unidad

    class Meta:
        verbose_name_plural = "Unidades"

class Articulo_Unidad(models.Model):
    """docstring for Articulo_Unidad"""
    def __init__(self, *args, **kwargs):
        super(Articulo_Unidad, self).__init__(*args, **kwargs)

    unidad = models.ForeignKey(Unidad)
    articulo = models.ForeignKey(Articulo)
    principal = models.BooleanField(default=False)
    relacion_principal = models.ForeignKey('self')

    def __unicode__(self):
        return u'%s %s'%(self.unidad, self.articulo)

    class Meta:
        verbose_name_plural = "Unidades de Articulos"

class Articulo_Precio(models.Model):
    """docstring for Articulo_Precio"""
    def __init__(self, *args, **kwargs):
        super(Articulo_Precio, self).__init__(*args, **kwargs)

    articulo = models.ForeignKey(Articulo)
    tipo_precio = models.ForeignKey(Tipo_precio)
    monto = models.DecimalField(max_digits=13, decimal_places=2)
    desde = models.DateField()
    hasta = models.DateField()
    descripcion = models.CharField(max_length=250)
    activo = models.BooleanField(default=True)

    def __unicode__(self):
        return u'%s %s'%(self.articulo, self.tipo_precio)

    class Meta:
        verbose_name_plural = "Precios de Articulos "

class Articulo_Proveedor(models.Model):
    """docstring for Articulo_Proveedor"""
    def __init__(self, *args, **kwargs):
        super(Articulo_Proveedor, self).__init__(*args, **kwargs)

    articulo = models.ForeignKey(Articulo)
    proveedor = models.ForeignKey(Proveedor)
    observacion = models.TextField()
    adicional1 = models.CharField(max_length=250, blank=True)
    adicional2 = models.CharField(max_length=250, blank=True)
    adicional3 = models.CharField(max_length=250, blank=True)
    adicional4 = models.CharField(max_length=250, blank=True)

    def __unicode__(self):
        return u'%s %s'%(self.activo, self.proveedor)

    class Meta:
        verbose_name_plural = "Proveedores de Articulos"
