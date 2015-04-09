#encoding:utf-8
from django.forms import ModelForm
from Transporte.models import Transporte, Equipamiento_Transporte, Transporte_Vehiculo, \
Transporte_rol, Transporte_cuadrilla

#class form
class TransporteForm(ModelForm):
    class Meta:
        model = Transporte
        fields = '__all__'

class EquipamientoTransporteForm(ModelForm):
    class Meta:
        model = Equipamiento_Transporte
        fields = '__all__'

class TransporteVehiculoForm(ModelForm):
    class Meta:
        model = Transporte_Vehiculo
        fields = '__all__'

class TransporterolForm(ModelForm):
    class Meta:
        model = Transporte_rol
        fields = '__all__'

class TransportecuadrillaForm(ModelForm):
    class Meta:
        model = Transporte_cuadrilla
        fields = '__all__'
