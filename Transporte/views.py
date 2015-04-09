from django.shortcuts import render, render_to_response, get_object_or_404
from Transporte.models import Transporte, Equipamiento_Transporte, Transporte_Vehiculo, \
Transporte_rol, Transporte_cuadrilla
from Transporte.forms import TransporteForm, EquipamientoTransporteForm, \
TransporteVehiculoForm, TransporterolForm
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from Vehiculo.forms import VehiculoForm

# Create your views here.
#lista
def lista_transporte(request):
    lista_transporte = Transporte.objects.all()
    context = {'lista_transporte': lista_transporte}
    return render(request, 'transporte/transporte_lista.html', context)

def lista_equipamiento_transporte(request, id_transp):

    transporte = Transporte.objects.get(id = id_transp)

    lista_equip_transp = Equipamiento_Transporte.objects.filter(transporte_id=transporte)
    context = {'lista_equip_transp': lista_equip_transp}
    return render(request, 'transporte/equipamientotransporte_lista.html', context)

def lista_transporte_vehiculo(request, id_transp):

    transporte = Transporte.objects.get(id = id_transp)

    lista_transp_vehic = Transporte_Vehiculo.objects.filter(transporte_id=transporte)
    context = {'lista_transp_vehic': lista_transp_vehic}
    return render(request, 'transporte/transportevehiculo_lista.html', context)

def lista_transporte_rol(request):
    lista_transporterol = Transporte_rol.objects.all()
    context = {'lista_transporterol': lista_transporterol}
    return render(request, 'transporte/transporterol_lista.html', context)

def lista_transporte_cuadrilla(request, id_transp):

    transporte = Transporte.objects.get(id = id_transp)

    lista_transpcuadrilla = Transporte_cuadrilla.objects.filter(transporte_id=transporte)
    context = {'lista_transpcuadrilla': lista_transpcuadrilla}
    return render(request, 'transporte/transportecuadrilla_lista.html', context)

# agregar nuevo
def add_transporte(request):

    if request.method == 'POST':
        form_transporte = TransporteForm(request.POST)
        if form_transporte.is_valid():
            form_transporte.save()
            return HttpResponseRedirect(reverse('utransporte:lista_transporte'))
    else:
        form_transporte = TransporteForm()
    return render_to_response('transporte/transporte_add.html', \
        {'form_transporte':form_transporte, 'create': True}, \
        context_instance = RequestContext(request))

def add_transporterol(request):

    if request.method == 'POST':
        form_transporterol = TransporterolForm(request.POST)
        if form_transporterol.is_valid():
            form_transporterol.save()
            return HttpResponseRedirect(reverse('utransporte:lista_transporte_rol'))
    else:
        form_transporterol = TransporterolForm()
    return render_to_response('transporte/transporterol_add.html', \
        {'form_transporterol':form_transporterol, 'create': True}, \
        context_instance = RequestContext(request))

def add_equipamientotransporte(request, id_transp):

    transporte = Transporte.objects.get(id = id_transp)

    if request.method == 'POST':

        form_equip_transp = EquipamientoTransporteForm(request.POST)
        form_equip_transp.transporte = transporte
        if form_equip_transp.is_valid():
            formu = form_equip_transp.save(commit = False)
            formu.transporte = transporte
            formu.save()

            return HttpResponseRedirect('../../')
    else:
        form_equip_transp = EquipamientoTransporteForm()
    return render_to_response('transporte/equipamientotransporte_add.html',\
     {'form_equip_transp':form_equip_transp, \
        'create': True}, context_instance = RequestContext(request))

def add_transportevehiculo(request, id_transp):

    transporte = Transporte.objects.get(id = id_transp)
    if request.method == 'POST':

        form_vehiculo = VehiculoForm(request.POST)

        if form_vehiculo.is_valid():
            obj_vehic = form_vehiculo.save()
            vehiculo = Vehiculo.objects.get(id = obj_vehic.id)

        transpvehi = TransporteVehiculoForm(request.POST)
        if transpvehi.is_valid():
            formResult2 = transpvehi.save(commit = False)
            #luego de hacer el save anterior le metodo el ID al siguiente y listo
            formResult2.transporte = transporte
            formResult2.vehiculo = vehiculo
            formResult2.save()
    else:
        form_vehiculo = VehiculoForm()
        transpvehi = TransporteVehiculoForm()

    return render_to_response('transporte/transportevehiculo_add.html', \
     {'form_vehiculo':form_vehiculo,'transpvehi':transpvehi, \
      'id_transp':id_transp, 'create': True}, \
      context_instance = RequestContext(request))

# editar un registro
def editar_transporte(request, pk):

    transporte = Transporte.objects.get(pk = pk)

    if request.method == 'POST':
        # formulario enviado
        editar_transporte = TransporteForm(request.POST, instance=transporte)

        if editar_transporte.is_valid():
            # formulario validado correctamente
            editar_transporte.save()

            return HttpResponseRedirect('../')

    else:
        # formulario inicial
        editar_transporte = TransporteForm(instance=transporte)

    return render_to_response('transporte/transporte_edit.html', \
        {'editar_transporte': editar_transporte, \
        'pk':pk, 'create':False}, \
        context_instance = RequestContext(request))

def edit_transporterol(request, pk):

    transporterol = Transporte_rol.objects.get(pk = pk)

    if request.method == 'POST':
        # formulario enviado
        form_edit_transporterol = TransporterolForm(request.POST, instance=transporterol)

        if form_edit_transporterol.is_valid():
            # formulario validado correctamente
            form_edit_transporterol.save()

            return HttpResponseRedirect(reverse('udireciones:lista_transporte_rol'))

    else:
        # formulario inicial
        form_edit_transporterol = TransporterolForm(instance=transporterol)

    return render_to_response('transporte/transporterol_edit.html', \
        {'form_edit_transporterol': form_edit_transporterol, 'create':False}, \
        context_instance = RequestContext(request))

def edit_equipamientotransporte(request,id_transp, pk):

    id_equipamientotransporte = Equipamiento_Transporte.objects.get(pk = pk)

    if request.method == 'POST':
        # formulario enviado
        form_edit_equip_transporte = EquipamientoTransporteForm(request.POST, instance=id_equipamientotransporte)

        if form_edit_equip_transporte.is_valid():
            # formulario validado correctamente
            form_edit_equip_transporte.save()

            #return HttpResponseRedirect(reverse('uclientes:lista_equipamientotransporte'))
            return HttpResponseRedirect('../../../')
    else:
        # formulario inicial
        form_edit_equip_transporte = EquipamientoTransporteForm(instance=id_equipamientotransporte)

    return render_to_response('transporte/equipamientotransporte_edit.html', \
        {'form_edit_equip_transporte': form_edit_equip_transporte, 'create':False},\
        context_instance = RequestContext(request))

def edit_transportevehiculo(request, id_transp, pk):

    id_vehi = Transporte_Vehiculo.objects.values('vehiculo').filter(pk = pk)

    id_vehiculo=Vehiculo.objects.get(pk=id_vehi)

    if request.method == 'POST':
        # formulario enviado
        form_edit_vehiculo = VehiculoForm(request.POST, instance=id_vehiculo)

        if form_edit_vehiculo.is_valid():
            # formulario validado correctamente
            form_edit_vehiculo.save()

            #return HttpResponseRedirect(reverse('uclientes:lista_email'))
            return HttpResponseRedirect('../../')
    else:
        # formulario inicial
        form_edit_vehiculo = VehiculoForm(instance=id_vehiculo)

    return render_to_response('transporte/transportevehiculo_edit.html', \
        {'form_edit_vehiculo': form_edit_vehiculo, 'create':False}, \
        context_instance = RequestContext(request))

# eliminar un registro
def delete_transporte(request, pk, template_name='server_confirm_delete.html'):
    transporte = get_object_or_404(Transporte, pk=pk)
    if request.method == 'POST':
        transporte.delete()
        return HttpResponseRedirect('../')
    return render(request, template_name, \
        {'object':transporte})

def delete_equipamientotransporte(request, pk, template_name='server_confirm_delete.html'):
    equipamientotransporte = get_object_or_404(Equipamiento_Transporte, pk=pk)
    if request.method == 'POST':
        equipamientotransporte.delete()
        return HttpResponseRedirect('../')
    return render(request, template_name, \
        {'object':equipamientotransporte})

def delete_transporterol(request, pk, template_name='server_confirm_delete.html'):
    transporterol = get_object_or_404(Transporte_rol, pk=pk)
    if request.method == 'POST':
        transporterol.delete()
        return HttpResponseRedirect('../')
    return render(request, template_name, \
        {'object':transporterol})

def delete_transportevehiculo(request, pk, template_name='server_confirm_delete.html'):
    transportevehiculo = get_object_or_404(Transporte_Vehiculo, pk=pk)
    if request.method == 'POST':
        transportevehiculo.delete()
        return HttpResponseRedirect('../')
    return render(request, template_name, \
        {'object':transportevehiculo})
