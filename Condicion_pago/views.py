from django.shortcuts import render, render_to_response, get_object_or_404
from Condicion_pago.models import Condicion_pago, CondicionPagoForm
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.core.urlresolvers import reverse

# Create your views here.
# listas
def lista_condicionpago(request):
    lista_condicionpago = Condicion_pago.objects.all()
    context = {'lista_condicionpago': lista_condicionpago}
    return render(request, 'condicionpago_lista.html', context)

# agregar nuevo
def add_condicionpago(request):
    if request.method == 'POST':
        form_condicionpago = CondicionPagoForm(request.POST, request.FILES)
        if form_condicionpago.is_valid():
            form_condicionpago.save()
            return HttpResponseRedirect(reverse('ucondicionpago:lista_condicionpago'))
    else:
        form_condicionpago = CondicionPagoForm()
    return render_to_response('condicionpago_add.html', {'form_condicionpago':form_condicionpago, 'create': True}, context_instance = RequestContext(request))

# editar un registro

def edit_condicionpago(request, pk):

    condicionpago = Condicion_pago.objects.get(pk = pk)

    if request.method == 'POST':
        # formform_condicionpagoulario enviado
        form_edit_condicionpago = CondicionPagoForm(request.POST, instance=condicionpago)

        if form_edit_condicionpago.is_valid():
            # formulario validado correctamente
            form_edit_condicionpago.save()

            return HttpResponseRedirect(reverse('ucondicionpago:lista_condicionpago'))

    else:
        # formulario inicial
        form_edit_condicionpago = CondicionPagoForm(instance=condicionpago)

    return render_to_response('condicionpago_edit.html', {'form_edit_condicionpago': form_edit_condicionpago, 'create':False}, context_instance = RequestContext(request))

# eliminar un registro
def delete_condicionpago(request, pk,):
        condicionpago = get_object_or_404(Condicion_pago, pk=pk)
        condicionpago.delete()

        return HttpResponseRedirect(reverse('ucondicionpago:lista_condicionpago'))
        html = "<script>alert('Registro eliminado');</script>"
        return HttpResponse(html)
