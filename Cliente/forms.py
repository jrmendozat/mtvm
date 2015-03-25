#encoding:utf-8
from django.forms import ModelForm
from Cliente.models import Cliente, Cliente_telefono, Email, Cliente_Direccion
#class form

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente

class ClienteTelefonoForm(ModelForm):
    class Meta:
        model = Cliente_telefono

class EmailForm(ModelForm):
    class Meta:
        model = Email

class ClienteDireccionForm(ModelForm):
    class Meta:
        model = Cliente_Direccion
