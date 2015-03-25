from django.contrib import admin
from Tipo_cliente.models import Tipo_cliente, Tipo_precio

# Register your models here.
admin.site.register(Tipo_precio)
admin.site.register(Tipo_cliente)
