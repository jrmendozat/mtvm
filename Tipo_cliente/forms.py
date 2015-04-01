#encoding:utf-8
from django.forms import ModelForm
from Tipo_cliente.models import Tipo_cliente, Tipo_precio

#class form
class TipoClienteForm(ModelForm):
    class Meta:
        model = Tipo_cliente
        fields = '__all__'

class TipoPrecioForm(ModelForm):
    class Meta:
        model = Tipo_precio
        fields = '__all__'
