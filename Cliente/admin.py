from django.contrib import admin
from Cliente.models import Cliente, Email, Cliente_Direccion, Cliente_telefono, Cliente_empresa

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Email)
admin.site.register(Cliente_Direccion)
admin.site.register(Cliente_telefono)
admin.site.register(Cliente_empresa)
