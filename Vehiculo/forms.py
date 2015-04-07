from django.forms import ModelForm
from Vehiculo.models import Tipo_Vehiculo, Modelo_Vehiculo, Vehiculo

#class form
class TipoVehiculoForm(ModelForm):
    class Meta:
        model = Tipo_Vehiculo
        fields = '__all__'

class ModeloVehiculoForm(ModelForm):
    class Meta:
        model = Modelo_Vehiculo
        fields = '__all__'

class VehiculoForm(ModelForm):
    class Meta:
        model = Vehiculo
        fields = '__all__'

