#encoding:utf-8
from django.forms import ModelForm
from Cliente.models import Cliente, Cliente_telefono, Email, Cliente_Direccion
from django import forms
from Direccion.models import Zona, Tipo_direccion

#class form

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre_principal', 'tipo_cliente', 'condicion_pago', \
        'monto_credito', 'segmento', 'sitio_web', 'comentarios', \
        'adicional1', 'adicional2', 'adicional3', 'adicional4', 'activo']

class ClienteTelefonoForm(ModelForm):
    class Meta:
        model = Cliente_telefono
        fields = '__all__' #para indicarle que todo los campos del modelo se deben utilizar

class EmailForm(ModelForm):
    class Meta:
        model = Email
        fields = ['email', 'cliente']

class ClienteDireccionForm(ModelForm):
    class Meta:
        model = Cliente_Direccion
        fields = '__all__'

class ClienteDireccForm(forms.Form):
    direccion = forms.CharField(widget = forms.Textarea )
    punto_referencia = forms.CharField(max_length=250)
    zip1 = forms.CharField(max_length=10)
    tipo_direccion = forms.ModelChoiceField(queryset=Tipo_direccion.objects.all())
    zona = forms.ModelChoiceField(queryset=Zona.objects.all())


