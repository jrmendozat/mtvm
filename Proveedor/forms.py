from django.forms import ModelForm
from Proveedor.models import Tipo_Proveedor, Proveedor, Proveedor_Telefono,\
Proveedor_Direccion, Email_Proveedor

# crear form
class TipoProveedorForm(ModelForm):
    class Meta:
        model = Tipo_Proveedor
        fields = '__all__'

class ProveedorForm(ModelForm):
    class Meta:
        model = Proveedor
        fields = '__all__'

class ProveedorTelefonoForm(ModelForm):
    class Meta:
        model = Proveedor_Telefono
        fields = '__all__'

class ProveedorDireccionForm(ModelForm):
    class Meta:
        model = Proveedor_Direccion
        fields = '__all__'

class EmailProveedorForm(ModelForm):
    class Meta:
        model = Email_Proveedor
        fields = '__all__'
