from Telefono.models import Telefono
from Telefono.forms import TelefonoForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
# Create your views here.

def lista_tipo(request):
    obj_list = Telefono.objects.all()
    context = {'obj_list': obj_list}
    return render(request, 'telefono.html', context)

def lista(request):
    obj_list = Telefono.objects.all()
    context = {'obj_list': obj_list}
    return render(request, 'prueba.html', context)

def nuevo_telefono(request):
    if request.method == 'POST':
        formulario = TelefonoForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/telefono/telefono')
    else:
        formulario = TelefonoForm()
    return render_to_response('telefonoform.html', {'formulario':formulario, 'create': True}, context_instance = RequestContext(request))

def editar_telefono(request, id_telef):

    id_telefono = Telefono.objects.get(pk = id_telef)

    if request.method == 'POST':
        # formulario enviado
        editar_telef_form = TelefonoForm(request.POST, instance=id_telefono)

        if editar_telef_form.is_valid():
            # formulario validado correctamente
            editar_telef_form.save()

            return HttpResponseRedirect(reverse('utelefonos:lista_tipo'))

    else:
        # formulario inicial
        editar_telef_form = TelefonoForm(instance=id_telefono)

    return render_to_response('telefonoform.html', {'editar_telef_form': editar_telef_form, 'create':False}, context_instance = RequestContext(request))

def Delete_telefono(request, pk, template_name='server_confirm_delete.html'):
    telefono = get_object_or_404(Telefono, pk=pk)
    if request.method == 'POST':
        telefono.delete()
        return redirect('lista_tipo')
    return render(request, template_name, {'object':telefono})
