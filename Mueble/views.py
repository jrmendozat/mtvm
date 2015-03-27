from django.shortcuts import render, render_to_response
from Mueble.models import Tamanio_Mueble, Tipo_Peso, Tipo_Fragilidad, \
Familia_Mueble, Mueble
from Mueble.forms import TamanioMuebleForm, TipoPesoForm, TipoFragilidadForm, \
FamiliaMuebleForm, MuebleForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext

# Create your views here.
#listas
def lista_tamanio_mueble(request):
    lista_tamaniomueble = Tamanio_Mueble.objects.all()
    context = {'lista_tamaniomueble': lista_tamaniomueble}
    return render(request, 'tamaniomueble_lista.html', context)

def lista_tipo_peso(request):
    lista_tipopeso = Tipo_Peso.objects.all()
    context = {'lista_tipopeso': lista_tipopeso}
    return render(request, 'cliente_lista.html', context)

def lista_tipo_fragilidad(request):
    lista_tipo_fragilidad = Tipo_Fragilidad.objects.all()
    context = {'lista_tipo_fragilidad': lista_tipo_fragilidad}
    return render(request, 'cliente_lista.html', context)

def lista_mueble(request):
    lista_mueble = Mueble.objects.all()
    context = {'lista_mueble': lista_mueble}
    return render(request, 'mueble/mueble_lista.html', context)

def lista_familia_mueble(request):
    lista_familiamueble = Familia_Mueble.objects.all()
    context = {'lista_familiamueble': lista_familiamueble}
    return render(request, 'cliente_lista.html', context)

# agregar nuevo
def add_tamaniomueble(request):
    if request.method == 'POST':
        form_tamaniomueble = TamanioMuebleForm(request.POST)
        if form_tamaniomueble.is_valid():
            form_tamaniomueble.save()
            return HttpResponseRedirect(reverse('umueble:lista_tamanio_mueble'))
    else:
        form_tamaniomueble = TamanioMuebleForm()
    return render_to_response('mueble/tamaniomueble_add.html', \
        {'form_tamaniomueble':form_tamaniomueble, 'create': True}, \
        context_instance = RequestContext(request))

def add_tipopeso(request):
    if request.method == 'POST':
        form_tipopeso = TipoPesoForm(request.POST)
        if form_tipopeso.is_valid():
            form_tipopeso.save()
            return HttpResponseRedirect(reverse('umueble:lista_tipopeso'))
    else:
        form_tipopeso = TipoPesoForm()
    return render_to_response('mueble/tipopeso_add.html', \
        {'form_tipopeso':form_tipopeso, 'create': True}, \
        context_instance = RequestContext(request))

def add_tipofragilidad(request):
    if request.method == 'POST':
        form_tipofragilidad = TipoFragilidadForm(request.POST)
        if form_tipofragilidad.is_valid():
            form_tipofragilidad.save()
            return HttpResponseRedirect(reverse('umueble:lista_tipofragilidad'))
    else:
        form_tipofragilidad = TipoFragilidadForm()
    return render_to_response('mueble/tipofragilidad_add.html', \
        {'form_tipofragilidad':form_tipofragilidad, 'create': True}, \
        context_instance = RequestContext(request))

def add_familiamueble(request):
    if request.method == 'POST':
        form_familiamueble = FamiliaMuebleForm(request.POST)
        if form_familiamueble.is_valid():
            form_familiamueble.save()
            return HttpResponseRedirect(reverse('umueble:lista_familiamueble'))
    else:
        form_familiamueble = FamiliaMuebleForm()
    return render_to_response('mueble/familiamueble_add.html', \
        {'form_familiamueble':form_familiamueble, 'create': True}, \
        context_instance = RequestContext(request))

def add_mueble(request):
    if request.method == 'POST':
        form_mueble = MuebleForm(request.POST)
        if form_mueble.is_valid():
            form_mueble.save()
            return HttpResponseRedirect(reverse('umueble:lista_mueble'))
    else:
        form_mueble = MuebleForm()
    return render_to_response('mueble/mueble_add.html', \
        {'form_mueble':form_mueble, 'create': True}, \
        context_instance = RequestContext(request))
