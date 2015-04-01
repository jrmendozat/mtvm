#encoding:utf-8
from django.forms import ModelForm
from Sede.models import Tipo_sede, Sede, Tipo_Ambiente, Ambiente
from django import forms

#class form
class TipoSedeForm(ModelForm):
    class Meta:
        model = Tipo_sede
        fields = '__all__'

class SedeForm(ModelForm):
    class Meta:
        model = Sede
        fields = '__all__'

class TipoAmbienteForm(ModelForm):
    class Meta:
        model = Tipo_Ambiente
        fields = '__all__'

class AmbienteForm(ModelForm):
    class Meta:
        model = Ambiente
        fields = '__all__'

class ClienteSedeForm(forms.Form):
    tipo_sede = forms.ModelChoiceField(queryset = Tipo_sede.objects.all())
    sede1 = forms.CharField(max_length=250)
    piso = forms.IntegerField()
    piso_por_escalera = forms.IntegerField()
    numero_ambiente = forms.IntegerField()
