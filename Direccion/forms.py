#encoding:utf-8
from django.forms import ModelForm
<<<<<<< HEAD
from Direccion.models import Direccion, Tipo_direccion
=======
from Direccion.models import Direccion, Tipo_direccion, \
Pais, Provincia, Ciudad, Zona

>>>>>>> yusnel
#class form

class DireccionForm(ModelForm):
    class Meta:
        model = Direccion
        fields = '__all__'

class TipoDireccionForm(ModelForm):
    class Meta:
        model = Tipo_direccion
        fields = '__all__'

class PaisForm(ModelForm):
    class Meta:
        model = Pais
        fields = '__all__'

class ProvinciaForm(ModelForm):
    class Meta:
        model = Provincia
        fields = '__all__'

class CiudadForm(ModelForm):
    class Meta:
        model = Ciudad
        fields = '__all__'

class ZonaForm(ModelForm):
    class Meta:
        model = Zona
        fields = '__all__'
