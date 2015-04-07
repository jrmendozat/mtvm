from django.contrib import admin
from Sede.models import Tipo_sede, Sede,Tipo_Ambiente, Ambiente
# Register your models here.
admin.site.register(Tipo_sede)
admin.site.register(Sede)
admin.site.register(Tipo_Ambiente)
admin.site.register(Ambiente)
