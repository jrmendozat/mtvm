from django.shortcuts import render, render_to_response, get_object_or_404
from Direccion.models import Tipo_direccion, Direccion, Pais
from Direccion.forms import TipoDireccionForm, DireccionForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
# Create your views here.

# lista
def lista_pais(request):
    lista_pais = Pais.objects.all()
    context = {'lista_pais':lista_pais}
    return render (request,'direccion/pais_lista.html', context)

def lista_tipo_direccion(request):
    lista_tipodireccion = Tipo_direccion.objects.all()
    context = {'lista_tipodireccion': lista_tipodireccion}
    return render(request, 'tipodireccion_lista.html', context)

def lista_direccion(request):
    lista_direccion = Direccion.objects.all()
    context = {'lista_direccion': lista_direccion}
    return render(request, 'tipodireccion_lista.html', context)

# agregar nuevo
def add_direccion(request):
    if request.method == 'POST':
        form_direccion = DireccionForm(request.POST, request.FILES)
        if form_direccion.is_valid():
            form_direccion.save()
            return HttpResponseRedirect(reverse('udireciones:lista_direccion'))
    else:
        form_direccion = DireccionForm()
    return render_to_response('direccion_add.html', \
        {'form_direccion':form_direccion, 'create': True}, \
        context_instance = RequestContext(request))

def add_tipo_direccion(request):
    if request.method == 'POST':
        form_tipodireccion = TipoDireccionForm(request.POST, request.FILES)
        if form_tipodireccion.is_valid():
            form_tipodireccion.save()
            return HttpResponseRedirect(reverse('udireciones:lista_direccion'))
    else:
        form_tipodireccion = TipoDireccionForm()
    return render_to_response('tipodireccion_add.html', \
        {'form_tipodireccion':form_tipodireccion, 'create': True}, \
        context_instance = RequestContext(request))

def edit_tipo_direccion(request, pk):

    tipodireccion = Tipo_direccion.objects.get(pk = pk)

    if request.method == 'POST':
        # formform_tipodireccionulario enviado
        form_edit_tipodireccion = TipoDireccionForm(request.POST, instance=tipodireccion)

        if form_edit_tipodireccion.is_valid():
            # formulario validado correctamente
            form_edit_tipodireccion.save()

            return HttpResponseRedirect(reverse('udireciones:lista_tipo_direccion'))

    else:
        # formulario inicial
        form_edit_tipodireccion = TipoDireccionForm(instance=tipodireccion)

    return render_to_response('tipodireccion_edit.html', {'form_edit_tipodireccion': form_edit_tipodireccion, 'create':False}, context_instance = RequestContext(request))

# eliminar un registro
def delete_tipo_direccion(request, pk, template_name='server_confirm_delete.html'):
    tipodireccion = get_object_or_404(Tipo_direccion, pk=pk)
    if request.method == 'POST':
        tipodireccion.delete()
        return HttpResponseRedirect(reverse('udireciones:lista_tipo_direccion'))
    return render(request, template_name, {'object':tipodireccion})
