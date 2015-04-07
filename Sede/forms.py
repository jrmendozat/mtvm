#encoding:utf-8
from django.forms import ModelForm
from Sede.models import Tipo_sede, Sede, Tipo_Ambiente, Ambiente
from django import forms

#class form
class TipoSedeForm(ModelForm):
    class Meta:
        model = Tipo_sede

class SedeForm(ModelForm):
    class Meta:
        model = Sede

class TipoAmbienteForm(ModelForm):
    class Meta:
        model = Tipo_Ambiente

class AmbienteForm(ModelForm):
    class Meta:
        model = Ambiente

class ClienteSedeForm(forms.Form):
    tipo_sede = forms.ModelChoiceField(queryset = Tipo_sede.objects.all())
    sede1 = forms.CharField(max_length=250)
    piso = forms.IntegerField()
    piso_por_escalera = forms.IntegerField()
    numero_ambiente = forms.IntegerField()
