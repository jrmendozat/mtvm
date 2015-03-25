from django.contrib import admin
from Telefono.models import Telefono, Tipo_telefono
# Register your models here.

admin.site.register(Tipo_telefono)
admin.site.register(Telefono)
