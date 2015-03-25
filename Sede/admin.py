from django.contrib import admin
from Sede.models import Tipo_sede, Sede,Tipo_ambiente, Ambiente
# Register your models here.
admin.site.register(Tipo_sede)
admin.site.register(Sede)
admin.site.register(Tipo_ambiente)
admin.site.register(Ambiente)
