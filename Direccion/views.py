from django.shortcuts import render, render_to_response, get_object_or_404
from Direccion.models import Tipo_direccion, Direccion, Pais, \
Provincia, Ciudad, Zona
from Direccion.forms import TipoDireccionForm, DireccionForm, \
PaisForm, ProvinciaForm, CiudadForm, ZonaForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
# Create your views here.

# lista
def lista_pais(request):
    lista_pais = Pais.objects.all()
    context = {'lista_pais':lista_pais}
    return render (request,'pais_lista.html', context)

def lista_provincia(request):
    lista_provincia = Provincia.objects.all()
    context = {'lista_provincia':lista_provincia}
    return render (request,'direccion/provincia_lista.html', context)

def lista_ciudad(request):
    lista_ciudad = Ciudad.objects.all()
    context = {'lista_ciudad':lista_ciudad}
    return render (request,'direccion/ciudad_lista.html', context)

def lista_zona(request):
    lista_zona = Zona.objects.all()
    context = {'lista_zona':lista_zona}
    return render (request,'direccion/zona_lista.html', context)


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

def add_pais(request):
    if request.method == 'POST':
        form_pais = PaisForm(request.POST, request.FILES)
        if form_pais.is_valid():
            form_pais.save()
            return HttpResponseRedirect(reverse('udireciones:lista_pais'))
    else:
        form_pais = PaisForm()
    return render_to_response('direccion/pais_add.html', \
        {'form_pais':form_pais, 'create': True}, \
        context_instance = RequestContext(request))

def add_provincia(request):
    if request.method == 'POST':
        form_provincia = ProvinciaForm(request.POST, request.FILES)
        if form_provincia.is_valid():
            form_provincia.save()
            return HttpResponseRedirect(reverse('udireciones:lista_provincia'))
    else:
        form_provincia = ProvinciaForm()
    return render_to_response('direccion/provincia_add.html', \
        {'form_provincia':form_provincia, 'create': True}, \
        context_instance = RequestContext(request))

def add_ciudad(request):
    if request.method == 'POST':
        form_ciudad = CiudadForm(request.POST, request.FILES)
        if form_ciudad.is_valid():
            form_ciudad.save()
            return HttpResponseRedirect(reverse('udireciones:lista_ciudad'))
    else:
        form_ciudad = CiudadForm()
    return render_to_response('direccion/ciudad_add.html', \
        {'form_ciudad':form_ciudad, 'create': True}, \
        context_instance = RequestContext(request))

def add_zona(request):
    if request.method == 'POST':
        form_zona = ZonaForm(request.POST, request.FILES)
        if form_zona.is_valid():
            form_zona.save()
            return HttpResponseRedirect(reverse('udireciones:lista_zona'))
    else:
        form_zona = ZonaForm()
    return render_to_response('direccion/zona_add.html', \
        {'form_zona':form_zona, 'create': True}, \
        context_instance = RequestContext(request))

# editar registro
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

def edit_pais(request, pk):

    pais = Pais.objects.get(pk = pk)

    if request.method == 'POST':
        # formulario enviado
        form_edit_pais = PaisForm(request.POST, instance=pais)

        if form_edit_pais.is_valid():
            # formulario validado correctamente
            form_edit_pais.save()

            return HttpResponseRedirect(reverse('udireciones:lista_pais'))

    else:
        # formulario inicial
        form_edit_pais = PaisForm(instance=pais)

    return render_to_response('direccion/pais_edit.html', \
        {'form_edit_pais': form_edit_pais, 'create':False}, \
        context_instance = RequestContext(request))

def edit_provincia(request, pk):

    provincia = Provincia.objects.get(pk = pk)

    if request.method == 'POST':
        # formulario enviado
        form_edit_provincia = ProvinciaForm(request.POST, instance=provincia)

        if form_edit_provincia.is_valid():
            # formulario validado correctamente
            form_edit_provincia.save()

            return HttpResponseRedirect(reverse('udireciones:lista_provincia'))

    else:
        # formulario inicial
        form_edit_provincia = ProvinciaForm(instance=provincia)

    return render_to_response('direccion/provincia_edit.html', \
        {'form_edit_provincia': form_edit_provincia, 'create':False}, \
        context_instance = RequestContext(request))

def edit_ciudad(request, pk):

    ciudad = Ciudad.objects.get(pk = pk)

    if request.method == 'POST':
        # formulario enviado
        form_edit_ciudad = CiudadForm(request.POST, instance=ciudad)

        if form_edit_ciudad.is_valid():
            # formulario validado correctamente
            form_edit_ciudad.save()

            return HttpResponseRedirect(reverse('udireciones:lista_ciudad'))

    else:
        # formulario inicial
        form_edit_ciudad = CiudadForm(instance=ciudad)

    return render_to_response('direccion/ciudad_edit.html', \
        {'form_edit_ciudad': form_edit_ciudad, 'create':False}, \
        context_instance = RequestContext(request))

def edit_zona(request, pk):

    zona = Zona.objects.get(pk = pk)

    if request.method == 'POST':
        # formulario enviado
        form_edit_zona = ZonaForm(request.POST, instance=zona)

        if form_edit_zona.is_valid():
            # formulario validado correctamente
            form_edit_zona.save()

            return HttpResponseRedirect(reverse('udireciones:lista_zona'))

    else:
        # formulario inicial
        form_edit_zona = ZonaForm(instance=zona)

    return render_to_response('direccion/zona_edit.html', \
        {'form_edit_zona': form_edit_zona, 'create':False}, \
        context_instance = RequestContext(request))

# eliminar un registro
def delete_tipo_direccion(request, pk, template_name='server_confirm_delete.html'):
    tipodireccion = get_object_or_404(Tipo_direccion, pk=pk)
    if request.method == 'POST':
        tipodireccion.delete()
        return HttpResponseRedirect(reverse('udireciones:lista_tipo_direccion'))
    return render(request, template_name, {'object':tipodireccion})

def delete_pais(request, pk, template_name='server_confirm_delete.html'):
    pais = get_object_or_404(Pais, pk=pk)
    if request.method == 'POST':
        pais.delete()
        return HttpResponseRedirect(reverse('udireciones:lista_tipo_direccion'))
    return render(request, template_name, {'object':pais})

def delete_provincia(request, pk, template_name='server_confirm_delete.html'):
    provincia = get_object_or_404(Provincia, pk=pk)
    if request.method == 'POST':
        provincia.delete()
        return HttpResponseRedirect(reverse('udireciones:lista_provincia'))
    return render(request, template_name, {'object':provincia})

def delete_ciudad(request, pk, template_name='server_confirm_delete.html'):
    ciudad = get_object_or_404(Ciudad, pk=pk)
    if request.method == 'POST':
        ciudad.delete()
        return HttpResponseRedirect(reverse('udireciones:lista_ciudad'))
    return render(request, template_name, {'object':ciudad})

def delete_zona(request, pk, template_name='server_confirm_delete.html'):
    zona = get_object_or_404(Zona, pk=pk)
    if request.method == 'POST':
        zona.delete()
        return HttpResponseRedirect(reverse('udireciones:lista_zona'))
    return render(request, template_name, {'object':zona})
