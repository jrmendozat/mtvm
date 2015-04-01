from django.shortcuts import render, render_to_response, \
get_object_or_404
from Mueble.models import Tamanio_Mueble, Tipo_Peso, \
Tipo_Fragilidad, Familia_Mueble, Mueble
from Mueble.forms import TamanioMuebleForm, TipoPesoForm, \
TipoFragilidadForm, FamiliaMuebleForm, MuebleForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext

# Create your views here.
#listas
def lista_tamanio_mueble(request):
    lista_tamaniomueble = Tamanio_Mueble.objects.all()
    context = {'lista_tamaniomueble': lista_tamaniomueble}
    return render(request, 'mueble/tamaniomueble_lista.html', context)

def lista_tipo_peso(request):
    lista_tipopeso = Tipo_Peso.objects.all()
    context = {'lista_tipopeso': lista_tipopeso}
    return render(request, 'mueble/tipopeso_lista.html', context)

def lista_tipo_fragilidad(request):
    lista_tipo_fragilidad = Tipo_Fragilidad.objects.all()
    context = {'lista_tipo_fragilidad': lista_tipo_fragilidad}
    return render(request, 'mueble/tipofragilidad_lista.html', context)

def lista_mueble(request):
    lista_mueble = Mueble.objects.all()
    context = {'lista_mueble': lista_mueble}
    return render(request, 'mueble/mueble_lista.html', context)

def lista_familia_mueble(request):
    lista_familiamueble = Familia_Mueble.objects.all()
    context = {'lista_familiamueble': lista_familiamueble}
    return render(request, 'mueble/familiamueble_lista.html', context)

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
            return HttpResponseRedirect(reverse('umueble:lista_tipo_fragilidad'))
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
            return HttpResponseRedirect(reverse('umueble:lista_familia_mueble'))
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

# editar un registro
def editar_tipopeso(request, pk):

    id_peso = Tipo_Peso.objects.get(pk=pk)

    if request.method == 'POST':
        # formulario enviado
        editar_tipopeso = TipoPesoForm(request.POST, instance=id_peso)

        if editar_tipopeso.is_valid():
            # formulario validado correctamente
            editar_tipopeso.save()

            return HttpResponseRedirect(reverse('umueble:lista_tipopeso'))
    else:
        # formulario inicial
        editar_tipopeso = TipoPesoForm(instance=id_peso)

    return render_to_response('mueble/mueble_edit.html', \
        {'editar_tipopeso':editar_tipopeso, \
        'id_peso':id_peso, 'create':False}, \
        context_instance = RequestContext(request))

def editar_tamanio_mueble(request, pk):

    id_ta = Tamanio_Mueble.objects.get(pk=pk)

    if request.method == 'POST':
        # formulario enviado
        editar_tamanio_m = TamanioMuebleForm(request.POST, instance=id_ta)

        if editar_tamanio_m.is_valid():
            # formulario validado correctamente
            editar_tamanio_m.save()

            return HttpResponseRedirect(reverse('umueble:tamaniomueble_lista'))

    else:
        # formulario inicial
        editar_tamanio_m = TamanioMuebleForm(instance=id_ta)

    return render_to_response('mueble/mueble_edit.html', \
        {'editar_tamanio_m':editar_tamanio_m, \
        'id_ta':id_ta, 'create':False}, \
        context_instance = RequestContext(request))

def editar_tipofragilidad(request, pk):

    id_fra = Tipo_Fragilidad.objects.get(pk=pk)

    if request.method == 'POST':
        # formulario enviado
        editar_tipofragilidad = TipoFragilidadForm(request.POST, instance=id_fra)

        if editar_tipofragilidad.is_valid():
            # formulario validado correctamente
            editar_tipofragilidad.save()

            return HttpResponseRedirect(reverse('umueble:lista_tipo_fragilidad'))

    else:
        # formulario inicial
        editar_tipofragilidad = Tipo_Fragilidad(instance=id_fra)

    return render_to_response('mueble/tipofragilidad_edit.html', \
        {'editar_tipofragilidad':editar_tipofragilidad, \
        'id_fra':id_fra, 'create':False}, \
        context_instance = RequestContext(request))

def editar_familiamueble(request, pk):

    id_fa = Familia_Mueble.objects.get(pk=pk)

    if request.method == 'POST':
        # formulario enviado
        editar_familiamueble = FamiliaMuebleForm(request.POST, instance=id_fa)

        if editar_familiamueble.is_valid():
            # formulario validado correctamente
            editar_familiamueble.save()

            return HttpResponseRedirect(reverse('umueble:lista_familia_mueble'))
    else:
        # formulario inicial
        editar_familiamueble = Familia_Mueble(instance=id_fa)

    return render_to_response('mueble/familiamueble_edit.html', \
        {'editar_familiamueble':editar_familiamueble, \
        'id_fa':id_fa, 'create':False}, \
        context_instance = RequestContext(request))

def editar_mueble(request, pk):

    id_mu = Mueble.objects.get(pk=pk)

    if request.method == 'POST':
        # formulario enviado
        editar_mueble = MuebleForm(request.POST, instance=id_mu)

        if editar_mueble.is_valid():
            # formulario validado correctamente
            editar_mueble.save()

            return HttpResponseRedirect(reverse('umueble:lista__mueble'))
    else:
        # formulario inicial
        editar_mueble = Mueble(instance=id_mu)

    return render_to_response('mueble/mueble_edit.html', \
        {'editar_mueble':editar_mueble, \
        'id_mu':id_mu, 'create':False}, \
        context_instance = RequestContext(request))

# eliminar un registro
def delete_tamanio_mueble(request, pk, template_name='server_confirm_delete.html'):
    tamanio_mueble = get_object_or_404(Tamanio_Mueble, pk=pk)
    if request.method == 'POST':
        tamanio_mueble.delete()
        return HttpResponseRedirect('../')
    return render(request, template_name, \
        {'object':tamanio_mueble})

def delete_tipopeso(request, pk, template_name='server_confirm_delete.html'):
    tipo_peso = get_object_or_404(Tipo_Peso, pk=pk)
    if request.method == 'POST':
        tipo_peso.delete()
        return HttpResponseRedirect('../')
    return render(request, template_name, \
        {'object':tipo_peso})

def delete_tipofragilidad(request, pk, template_name='server_confirm_delete.html'):
    tipofragilidad = get_object_or_404(Tipo_Fragilidad, pk=pk)
    if request.method == 'POST':
        tipofragilidad.delete()
        return HttpResponseRedirect('../')
    return render(request, template_name, \
        {'object':tipofragilidad})

def delete_familiamueble(request, pk, template_name='server_confirm_delete.html'):
    familiamueble = get_object_or_404(Familia_Mueble, pk=pk)
    if request.method == 'POST':
        familiamueble.delete()
        return HttpResponseRedirect('../')
    return render(request, template_name, \
        {'object':familiamueble})

def delete_mueble(request, pk, template_name='server_confirm_delete.html'):
    mueble = get_object_or_404(Mueble, pk=pk)
    if request.method == 'POST':
        mueble.delete()
        return HttpResponseRedirect('../')
    return render(request, template_name, \
        {'object':mueble})
