from django.contrib import admin
from Pais.models import Pais, Provincia, Ciudad, Zona

# Register your models here.
admin.site.register(Pais)
admin.site.register(Provincia)
admin.site.register(Ciudad)
admin.site.register(Zona)
