from Telefono.models import Telefono, Tipo_telefono
from Telefono.forms import TelefonoForm, TipoTelefonoForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
# Create your views here.
# lista
def lista_telefono(request):
    obj_list = Telefono.objects.all()
    context = {'obj_list': obj_list}
    return render(request, 'telefono/telefono_lista.html', context)

def lista_tipotelefono(request):
    obj_list = Tipo_telefono.objects.all()
    context = {'obj_list': obj_list}
    return render(request, 'telefono/tipotelefono_lista.html',\
    context)

def lista_tipo(request):
    obj_list = Telefono.objects.all()
    context = {'obj_list': obj_list}
    return render(request, 'telefono.html', context)

def lista(request):
    obj_list = Telefono.objects.all()
    context = {'obj_list': obj_list}
    return render(request, 'prueba.html', context)

# agregar nuevo
def nuevo_telefono(request):
    if request.method == 'POST':
        formulario = TelefonoForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/telefono/telefono')
    else:
        formulario = TelefonoForm()
    return render_to_response('telefono/telefono_add.html', \
        {'formulario':formulario, 'create': True}, \
        context_instance = RequestContext(request))

def nuevo_tipotelefono(request):
    if request.method == 'POST':
        form_tipotelefono = TipoTelefonoForm(request.POST, request.FILES)
        if form_tipotelefono.is_valid():
            form_tipotelefono.save()
            return HttpResponseRedirect('/telefono/telefono')
    else:
        form_tipotelefono = TipoTelefonoForm()
    return render_to_response('telefono/tipotelefono_add.html', \
        {'form_tipotelefono':form_tipotelefono, 'create': True}, \
        context_instance = RequestContext(request))


# editar
def editar_telefono(request, id_telef):

    id_telefono = Telefono.objects.get(pk = id_telef)

    if request.method == 'POST':
        # formulario enviado
        editar_telef_form = TelefonoForm(request.POST, instance=id_telefono)

        if editar_telef_form.is_valid():
            # formulario validado correctamente
            editar_telef_form.save()

            return HttpResponseRedirect(reverse('utelefonos:lista_telefono'))
    else:
        # formulario inicial
        editar_telef_form = TelefonoForm(instance=id_telefono)

    return render_to_response('telefono/telefono_edit.html', \
        {'editar_telef_form': editar_telef_form, \
        'create':False}, context_instance = RequestContext(request))

def editar_tipotelefono(request, pk):

    id_tipo = Tipo_telefono.objects.get(pk = pk)

    if request.method == 'POST':
        # formulario enviado
        editar_tipotelef_form = TipoTelefonoForm(request.POST, instance=id_tipo)

        if editar_tipotelef_form.is_valid():
            # formulario validado correctamente
            editar_tipotelef_form.save()

            return HttpResponseRedirect(reverse('utelefonos:lista_tipotelefono'))
    else:
        # formulario inicial
        editar_tipotelef_form = TipoTelefonoForm(instance=id_tipo)

    return render_to_response('telefono/tipotelefono_edit.html', \
        {'editar_tipotelef_form': editar_tipotelef_form, \
        'create':False}, context_instance = RequestContext(request))

# eliminar registro
def Delete_telefono(request, pk, template_name='server_confirm_delete.html'):
    telefono = get_object_or_404(Telefono, pk=pk)
    if request.method == 'POST':
        telefono.delete()
        return redirect('lista_telefono')
    return render(request, template_name, {'object':telefono})

def Delete_tipotelefono(request, pk, template_name='server_confirm_delete.html'):
    tipotelefono = get_object_or_404(Tipo_telefono, pk=pk)
    if request.method == 'POST':
        tipotelefono.delete()
        return redirect('lista_tipotelefono')
    return render(request, template_name, {'object':tipotelefono})
