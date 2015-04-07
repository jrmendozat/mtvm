from django.shortcuts import render, render_to_response
from Vehiculo.models import Tipo_Vehiculo, Modelo_Vehiculo, Vehiculo
from Vehiculo.forms import TipoVehiculoForm, ModeloVehiculoForm, VehiculoForm
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
# Create your views here.
#lista
def lista_tipo_vehiculo(request):
    lista_tipovehiculo = Tipo_Vehiculo.objects.all()
    context = {'lista_tipovehiculo': lista_tipovehiculo}
    return render(request, 'tipovehiculo_lista.html', context)

def lista_modelo_vehiculo(request):
    lista_modelovehiculo = Modelo_Vehiculo.objects.all()
    context = {'lista_modelovehiculo': lista_modelovehiculo}
    return render(request, 'modelovehiculo_lista.html', context)

def lista_vehiculo(request):
    lista_vehiculo = Vehiculo.objects.all()
    context = {'lista_vehiculo': lista_vehiculo}
    return render(request, 'vehiculo_lista.html', context)

# agregar nuevo
def add_tipovehiculo(request):

    if request.method == 'POST':
        form_tipovehiculo = TipoVehiculoForm(request.POST)
        if form_tipovehiculo.is_valid():
            form_tipovehiculo.save()
            return HttpResponseRedirect(reverse('uvehiculo:lista_tipo_vehiculo'))
    else:
        form_tipovehiculo = TipoVehiculoForm()
    return render_to_response('vehiculo/tipovehiculo_add.html', \
        {'form_tipovehiculo':form_tipovehiculo, 'create': True}, \
        context_instance = RequestContext(request))

def add_modelovehiculo(request):

    if request.method == 'POST':
        form_modelovehiculo = ModeloVehiculoForm(request.POST)
        if form_modelovehiculo.is_valid():
            form_modelovehiculo.save()
            return HttpResponseRedirect(reverse('uvehiculo:lista_modelo_vehiculo'))
    else:
        form_modelovehiculo = ModeloVehiculoForm()
    return render_to_response('vehiculo/modelovehiculo_add.html', \
        {'form_modelovehiculo':form_modelovehiculo, 'create': True}, \
        context_instance = RequestContext(request))
