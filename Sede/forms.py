#encoding:utf-8
from django.forms import ModelForm
from Sede.models import Tipo_sede, Sede

#class form
class TipoSedeForm(ModelForm):
    class Meta:
        model = Tipo_sede

class SedeForm(ModelForm):
    class Meta:
        model = Sede
