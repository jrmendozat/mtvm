#encoding:utf-8
from django.forms import ModelForm
from Direccion.models import Direccion, Tipo_direccion

#class form
class DireccionForm(ModelForm):
    class Meta:
        model = Direccion

class TipoDireccionForm(ModelForm):
    class Meta:
        model = Tipo_direccion
