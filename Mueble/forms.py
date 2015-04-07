from django.forms import ModelForm
from Mueble.models import Mueble, Tamanio_Mueble, \
Tipo_Peso, Tipo_Fragilidad, Familia_Mueble

# crear form
class MuebleForm(ModelForm):
    class Meta:
        model = Mueble
        fields = '__all__'

class TamanioMuebleForm(ModelForm):
    class Meta:
        model = Tamanio_Mueble
        fields = '__all__'

class TipoPesoForm(ModelForm):
    class Meta:
        model = Tipo_Peso
        fields = '__all__'

class TipoFragilidadForm(ModelForm):
    class Meta:
        model = Tipo_Fragilidad
        fields = '__all__'

class FamiliaMuebleForm(ModelForm):
    class Meta:
        model = Familia_Mueble
        fields = '__all__'

