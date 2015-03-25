from django.contrib import admin
from Trabajador.models import Trabajador, Trabajador_status, Tipo_status

# Register your models here.
admin.site.register(Trabajador)
admin.site.register(Trabajador_status)
admin.site.register(Tipo_status)
