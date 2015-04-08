from django.shortcuts import render, render_to_response, get_object_or_404
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
    return render(request, 'vehiculo/tipovehiculo_lista.html', context)

def lista_modelo_vehiculo(request):
    lista_modelovehiculo = Modelo_Vehiculo.objects.all()
    context = {'lista_modelovehiculo': lista_modelovehiculo}
    return render(request, 'vehiculo/modelovehiculo_lista.html', context)

def lista_vehiculo(request):
    lista_vehiculo = Vehiculo.objects.all()
    context = {'lista_vehiculo': lista_vehiculo}
    return render(request, 'vehiculo/vehiculo_lista.html', context)

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

def add_vehiculo(request):

    if request.method == 'POST':
        form_vehiculo = VehiculoForm(request.POST)
        if form_vehiculo.is_valid():
            form_vehiculo.save()
            return HttpResponseRedirect(reverse('uvehiculo:lista_vehiculo'))
    else:
        form_vehiculo = VehiculoForm()
    return render_to_response('vehiculo/vehiculo_add.html', \
        {'form_vehiculo':form_vehiculo, 'create': True}, \
        context_instance = RequestContext(request))

# editar un registro
def editar_tipovehiculo(request, pk):

    id_tipo = Tipo_Vehiculo.objects.get(pk=pk)

    if request.method == 'POST':
        # formulario enviado
        editar_tipovehiculo = TipoVehiculoForm(request.POST, instance=id_tipo)

        if editar_tipovehiculo.is_valid():
            # formulario validado correctamente
            editar_tipovehiculo.save()

            return HttpResponseRedirect(reverse('uvehiculo:lista_tipo_vehiculo'))
    else:
        # formulario inicial
        editar_tipovehiculo = TipoVehiculoForm(instance=id_tipo)

    return render_to_response('vehiculo/tipovehiculo_edit.html', \
        {'editar_tipovehiculo':editar_tipovehiculo, \
        'id_tipo':id_tipo, 'create':False}, \
        context_instance = RequestContext(request))

def editar_modelovehiculo(request, pk):

    id_modelo = Modelo_Vehiculo.objects.get(pk=pk)

    if request.method == 'POST':
        # formulario enviado
        editar_modelovehiculo = ModeloVehiculoForm(request.POST, instance=id_modelo)

        if editar_modelovehiculo.is_valid():
            # formulario validado correctamente
            editar_modelovehiculo.save()

            return HttpResponseRedirect(reverse('uvehiculo:lista_modelo_vehiculo'))
    else:
        # formulario inicial
        editar_modelovehiculo = ModeloVehiculoForm(instance=id_modelo)

    return render_to_response('vehiculo/modelovehiculo_edit.html', \
        {'editar_modelovehiculo':editar_modelovehiculo, \
        'id_modelo':id_modelo, 'create':False}, \
        context_instance = RequestContext(request))

def editar_vehiculo(request, pk):

    id_vehiculo = Vehiculo.objects.get(pk=pk)

    if request.method == 'POST':
        # formulario enviado
        editar_vehiculo = VehiculoForm(request.POST,instance=id_vehiculo)

        if editar_vehiculo.is_valid():
            # formulario validado correctamente
            editar_vehiculo.save()

            return HttpResponseRedirect(reverse('uvehiculo:lista_vehiculo'))
    else:
        # formulario inicial
        editar_vehiculo = VehiculoForm(instance=id_vehiculo)

    return render_to_response('vehiculo/vehiculo_edit.html', \
        {'editar_vehiculo':editar_vehiculo, \
        'id_vehiculo':id_vehiculo, 'create':False}, \
        context_instance = RequestContext(request))

# eliminar un registro
def delete_tipovehiculo(request, pk, template_name='server_confirm_delete.html'):
    tipovehiculo = get_object_or_404(Tipo_Vehiculo, pk=pk)
    if request.method == 'POST':
        tipovehiculo.delete()
        return HttpResponseRedirect('../')
    return render(request, template_name, \
        {'object':tipovehiculo})

def delete_modelovehiculo(request, pk, template_name='server_confirm_delete.html'):
    modelovehiculo = get_object_or_404(Modelo_Vehiculo, pk=pk)
    if request.method == 'POST':
        modelovehiculo.delete()
        return HttpResponseRedirect('../')
    return render(request, template_name, \
        {'object':modelovehiculo})

def delete_vehiculo(request, pk, template_name='server_confirm_delete.html'):
    vehiculo = get_object_or_404(Vehiculo, pk=pk)
    if request.method == 'POST':
        vehiculo.delete()
        return HttpResponseRedirect('../')
    return render(request, template_name, \
        {'object':vehiculo})
