from django.shortcuts import render, render_to_response, get_object_or_404
from Sede.models import Tipo_sede, Sede, Tipo_Ambiente, Ambiente
from Sede.forms import TipoSedeForm, SedeForm, TipoAmbienteForm, AmbienteForm
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse

# Create your views here.
# lista
def lista_tiposede(request):
    lista_tiposede = Tipo_sede.objects.all()
    context = {'lista_tiposede': lista_tiposede}
    return render(request, 'sede/tiposede_lista.html', context)

def lista_sede(request):
    lista_sede = Sede.objects.all()
    context = {'lista_sede': lista_sede}
    return render(request, 'sede/sede_lista.html', context)

def lista_tipoambiente(request):
    lista_tipoambiente = Tipo_Ambiente.objects.all()
    context = {'lista_tipoambiente': lista_tipoambiente}
    return render(request, 'sede/tipoambiente_lista.html', context)

def lista_ambiente(request):
    lista_ambiente = Ambiente.objects.all()
    context = {'lista_ambiente': lista_ambiente}
    return render(request, 'sede/ambiente_lista.html', context)

# agregar nuevo
def add_tiposede(request):
    if request.method == 'POST':
        form_tiposede = TipoSedeForm(request.POST, request.FILES)
        if form_tiposede.is_valid():
            form_tiposede.save()
            return HttpResponseRedirect(reverse('usede:lista_tiposede'))
    else:
        form_tiposede = TipoSedeForm()
    return render_to_response('sede/tiposede_add.html', \
        {'form_tiposede':form_tiposede, 'create': True}, \
        context_instance = RequestContext(request))

def add_sede(request):
    if request.method == 'POST':
        form_sede = SedeForm(request.POST, request.FILES)
        if form_sede.is_valid():
            form_sede.save()
            return HttpResponseRedirect(reverse('usede:lista_sede'))
    else:
        form_sede = SedeForm()
    return render_to_response('sede/sede_add.html', {'form_sede':form_sede, \
        'create': True}, context_instance = RequestContext(request))

def add_tipoambiente(request):
    if request.method == 'POST':
        form_tipoambiente = TipoAmbienteForm(request.POST, request.FILES)
        if form_tipoambiente.is_valid():
            form_tipoambiente.save()
            return HttpResponseRedirect(reverse('usede:lista_tipoambiente'))
    else:
        form_tipoambiente = TipoAmbienteForm()
    return render_to_response('sede/tipoambiente_add.html', \
        {'form_tipoambiente':form_tipoambiente, 'create': True}, \
        context_instance = RequestContext(request))

def add_ambiente(request):
    if request.method == 'POST':
        form_ambiente = AmbienteForm(request.POST, request.FILES)
        if form_ambiente.is_valid():
            form_ambiente.save()
            return HttpResponseRedirect(reverse('usede:lista_ambiente'))
    else:
        form_ambiente = AmbienteForm()
    return render_to_response('sede/ambiente_add.html', \
        {'form_ambiente':form_ambiente, \
        'create': True}, context_instance = RequestContext(request))

# editar un registro
def edit_sede(request, pk):

    sede = Sede.objects.get(pk = pk)

    if request.method == 'POST':
        # formulario enviado
        form_edit_sede = SedeForm(request.POST, instance=sede)

        if form_edit_sede.is_valid():
            # formulario validado correctamente
            form_edit_sede.save()

            return HttpResponseRedirect(reverse('usede:lista_tiposede'))
    else:
        # formulario inicial
        form_edit_sede = SedeForm(instance=sede)

    return render_to_response('sede/sede_edit.html', {'form_edit_sede': form_edit_sede, 'create':False}, context_instance = RequestContext(request))

def edit_tiposede(request, pk):

    tiposede = Tipo_sede.objects.get(pk = pk)

    if request.method == 'POST':
        # formform_tiposedeulario enviado
        form_edit_tiposede = TipoSedeForm(request.POST, instance=tiposede)

        if form_edit_tiposede.is_valid():
            # formulario validado correctamente
            form_edit_tiposede.save()

            return HttpResponseRedirect(reverse('usede:lista_tiposede'))

    else:
        # formulario inicial
        form_edit_tiposede = TipoSedeForm(instance=tiposede)

    return render_to_response('sede/tiposede_edit.html', {'form_edit_tiposede': form_edit_tiposede, 'create':False}, context_instance = RequestContext(request))

def edit_ambiente(request, pk):

    ambiente = Ambiente.objects.get(pk = pk)

    if request.method == 'POST':
        # formulario enviado
        form_edit_ambiente = AmbienteForm(request.POST, \
            instance=ambiente)

        if form_edit_ambiente.is_valid():
            # formulario validado correctamente
            form_edit_ambiente.save()

            return HttpResponseRedirect(reverse('usede:lista_ambiente'))

    else:
        # formulario inicial
        form_edit_ambiente = AmbienteForm(instance=ambiente)

    return render_to_response('sede/ambiente_edit.html', \
        {'form_edit_ambiente': form_edit_ambiente, 'create':False}, \
        context_instance = RequestContext(request))

def edit_tipoambiente(request, pk):

    tipoambiente = Tipo_Ambiente.objects.get(pk = pk)

    if request.method == 'POST':
        # formulario enviado
        form_edit_tipoambiente = TipoAmbienteForm(request.POST, \
            instance=tipoambiente)

        if form_edit_tipoambiente.is_valid():
            # formulario validado correctamente
            form_edit_tipoambiente.save()

            return HttpResponseRedirect(reverse('usede:lista_tipoambiente'))

    else:
        # formulario inicial
        form_edit_tipoambiente = TipoAmbienteForm(instance=tipoambiente)

    return render_to_response('sede/tipoambiente_edit.html', \
        {'form_edit_tipoambiente': form_edit_tipoambiente, 'create':False}, \
        context_instance = RequestContext(request))

# eliminar un registro
def delete_sede(request, pk, template_name='server_confirm_delete.html'):
    sede = get_object_or_404(Sede, pk=pk)
    if request.method == 'POST':
        sede.delete()
        return HttpResponseRedirect(reverse('usede:lista_sede'))
    return render(request, template_name, {'object':sede})

def delete_tiposede(request, pk, template_name='server_confirm_delete.html'):
    tiposede = get_object_or_404(Tipo_sede, pk=pk)
    if request.method == 'POST':
        tiposede.delete()
        return HttpResponseRedirect(reverse('usede:lista_tiposede'))
    return render(request, template_name, {'object':tiposede})

def delete_ambiente(request, pk, template_name='server_confirm_delete.html'):
    ambiente = get_object_or_404(Ambiente, pk=pk)
    if request.method == 'POST':
        ambiente.delete()
        return HttpResponseRedirect(reverse('usede:lista_ambiente'))
    return render(request, template_name, {'object':ambiente})

def delete_tipoambiente(request, pk, template_name='server_confirm_delete.html'):
    tipoambiente = get_object_or_404(Tipo_Ambiente, pk=pk)
    if request.method == 'POST':
        tipoambiente.delete()
        return HttpResponseRedirect(reverse('usede:lista_tipoambiente'))
    return render(request, template_name, {'object':tipoambiente})
