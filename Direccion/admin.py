from django.contrib import admin
from Direccion.models import Tipo_direccion, Direccion,Pais, Provincia, Ciudad, Zona
# Register your models here.

admin.site.register(Tipo_direccion)
admin.site.register(Direccion)
admin.site.register(Pais)
admin.site.register(Provincia)
admin.site.register(Ciudad)
admin.site.register(Zona)

