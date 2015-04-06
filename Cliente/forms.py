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
        fields = ['email', 'cliente']

class ClienteDireccionForm(ModelForm):
    class Meta:
        model = Cliente_Direccion
<<<<<<< HEAD
=======
        fields = '__all__'

class ClienteDireccForm(forms.Form):
    direccion = forms.CharField(widget = forms.Textarea )
    punto_referencia = forms.CharField(max_length=250)
    zip1 = forms.CharField(max_length=10)
    tipo_direccion = forms.ModelChoiceField(queryset=Tipo_direccion.objects.all())
    zona = forms.ModelChoiceField(queryset=Zona.objects.all())


>>>>>>> yusnel
