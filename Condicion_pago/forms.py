from django.forms import ModelForm
from Condicion_pago.models import Condicion_pago

class CondicionPagoForm(ModelForm):
    class Meta:
        model = Condicion_pago
        fields = ['condicion', 'dias', 'adicional1',\
          'adicional2', 'adicional3', 'adicional4', 'activo']
