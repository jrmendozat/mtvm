from django.contrib import admin
from Departamento.models import Disenio, Jerarquia, Departamento, Cargo_tipo, Cargo

# Register your models here.
admin.site.register(Disenio)
admin.site.register(Jerarquia)
admin.site.register(Departamento)
admin.site.register(Cargo_tipo)
admin.site.register(Cargo)
