#encoding:utf-8
from django.forms import ModelForm
from Sede.models import Tipo_sede, Sede, Tipo_ambiente, Ambiente

#class form
class TipoSedeForm(ModelForm):
    class Meta:
        model = Tipo_sede

class SedeForm(ModelForm):
    class Meta:
        model = Sede

class TipoAmbienteForm(ModelForm):
    class Meta:
        model = Tipo_ambiente

class AmbienteForm(ModelForm):
    class Meta:
        model = Ambiente
