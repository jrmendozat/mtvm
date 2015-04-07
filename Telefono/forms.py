#encoding:utf-8
from django.forms import ModelForm
from django import forms
from Telefono.models import Telefono, Tipo_telefono

#class form
class PruebaForm(forms.Form):

    tipo_telefono = forms.CharField(label='tipo')
    numero = forms.CharField(label='Numero de telefono')

class TelefonoForm(ModelForm):
    class Meta:
        model = Telefono
        fields = '__all__'

class TipoTelefonoForm(ModelForm):
    class Meta:
        model = Tipo_telefono
        fields = '__all__'
