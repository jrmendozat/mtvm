from django.forms import ModelForm
from Condicion_pago.models import Condicion_pago

class CondicionPagoForm(ModelForm):
    class Meta:
        model = Condicion_pago
