from django.shortcuts import render, render_to_response, get_object_or_404
from Tipo_cliente.models import Tipo_cliente, Tipo_precio
from Tipo_cliente.forms import TipoClienteForm, TipoPrecioForm
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
# Create your views here.

# listas
def lista_tipocliente(request):
    lista_cliente = Tipo_cliente.objects.all().order_by('descripcion')
    context = {'lista_cliente': lista_cliente}
    return render(request, 'tipocliente_lista.html', context)

def lista_tipoprecio(request):
    Lista_precio = Tipo_precio.objects.all().order_by('nombre')
    context = {'Lista_precio': Lista_precio}
    return render(request, 'tipoprecio_lista.html', context)

# agregar nuevo
def add_tipocliente(request):
    if request.method == 'POST':
        form_tipocliente = TipoClienteForm(request.POST, request.FILES)
        if form_tipocliente.is_valid():
            form_tipocliente.save()
            return HttpResponseRedirect(reverse('utipocliente:lista_tipocliente'))
    else:
        form_tipocliente = TipoClienteForm()
    return render_to_response('tipocliente_add.html', {'form_tipocliente':form_tipocliente, 'create': True}, context_instance = RequestContext(request))

def add_tipoprecio(request):
    if request.method == 'POST':
        form_tipoprecio = TipoPrecioForm(request.POST, request.FILES)
        if form_tipoprecio.is_valid():
            form_tipoprecio.save()
            return HttpResponseRedirect(reverse('utipocliente:lista_tipoprecio'))
    else:
        form_tipoprecio = TipoPrecioForm()
    return render_to_response('tipoprecio_add.html', {'form_tipoprecio':form_tipoprecio, 'create': True}, context_instance = RequestContext(request))


# editar un registro

def edit_tipocliente(request, pk):

    tipocliente = Tipo_cliente.objects.get(pk = pk)

    if request.method == 'POST':
        # formform_tipoclienteulario enviado
        form_edit_tipocliente = TipoClienteForm(request.POST, instance=tipocliente)

        if form_edit_tipocliente.is_valid():
            # formulario validado correctamente
            form_edit_tipocliente.save()

            return HttpResponseRedirect(reverse('utipocliente:lista_tipocliente'))

    else:
        # formulario inicial
        form_edit_tipocliente = TipoClienteForm(instance=tipocliente)

    return render_to_response('tipocliente_edit.html', {'form_edit_tipocliente': form_edit_tipocliente, 'create':False}, context_instance = RequestContext(request))

def edit_tipoprecio(request, pk):

    tipoprecio = Tipo_precio.objects.get(pk = pk)

    if request.method == 'POST':
        # formform_tipoprecioulario enviado
        form_edit_tipoprecio = TipoPrecioForm(request.POST, instance=tipoprecio)

        if form_edit_tipoprecio.is_valid():
            # formulario validado correctamente
            form_edit_tipoprecio.save()

            return HttpResponseRedirect(reverse('utipocliente:lista_tipoprecio'))

    else:
        # formulario inicial
        form_edit_tipoprecio = TipoPrecioForm(instance=tipoprecio)

    return render_to_response('tipoprecio_edit.html', {'form_edit_tipoprecio': form_edit_tipoprecio, 'create':False}, context_instance = RequestContext(request))

# eliminar un registro
def delete_tipocliente(request, pk, template_name='server_confirm_delete.html'):
    tipocliente = get_object_or_404(Tipo_cliente, pk=pk)
    if request.method == 'POST':
        tipocliente.delete()
        return HttpResponseRedirect(reverse('utipocliente:lista_tipocliente'))
    return render(request, template_name, {'object':tipocliente})

def delete_tipoprecio(request, pk, template_name='server_confirm_delete.html'):
    tipoprecio = get_object_or_404(Tipo_precio, pk=pk)
    if request.method == 'POST':
        tipoprecio.delete()
        return HttpResponseRedirect(reverse('utipocliente:lista_tipoprecio'))
    return render(request, template_name, {'object':tipoprecio})
