from django.shortcuts import render, render_to_response, get_object_or_404
from Segmento.models import Segmento
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.core.urlresolvers import reverse
from .forms import SegmentoSearchForm, SegmentoForm


# Create your views here.
# listas
def lista_segmento(request):
    sl = Segmento.objects.all().order_by('segmento')
    context = {'lista_segmento': sl}
    return render(request, 'segmento_lista.html', context)

# agregar nuevo
def add_segmento(request):
    if request.method == 'POST':
        form_segmento = SegmentoForm(request.POST, request.FILES)
        if form_segmento.is_valid():
            form_segmento.save()
            return HttpResponseRedirect(reverse('usegmentos:segmento_lista'))
    else:
        form_segmento = SegmentoForm()
    return render_to_response('add_segmento.html', \
        {'form_segmento':form_segmento, 'create': True}, context_instance = RequestContext(request))

# editar un registro

def edit_segmento(request, pk):

    segmento = Segmento.objects.get(pk = pk)

    if request.method == 'POST':
        # formform_segmentoulario enviado
        form_edit_segmento = SegmentoForm(request.POST, instance=segmento)

        if form_edit_segmento.is_valid():
            # formulario validado correctamente
            form_edit_segmento.save()

            return HttpResponseRedirect(reverse('usegmentos:lista_segmento'))

    else:
        # formulario inicial
        form_edit_segmento = SegmentoForm(instance=segmento)

    return render_to_response('segmento_edit.html', {'form_edit_segmento': form_edit_segmento, 'create':False}, context_instance = RequestContext(request))

# eliminar un registro
def delete_segmento(request, pk, template_name='server_confirm_delete.html'):
    segmento = get_object_or_404(Segmento, pk=pk)
    if request.method == 'POST':
        segmento.delete()
        return HttpResponseRedirect(reverse('usegmentos:lista_segmento'))
    return render(request, template_name, {'object':segmento})

def mensaje_eliminar(request, pk):

     segmento = get_object_or_404(Segmento, pk=pk)
     if request.method == 'POST':
        segmento.delete()


def eliminar(request,pk):

    html = "<script>alert('alerta');</script>"
    return HttpResponse(html)


#vista para la busqueda
def segmentos(request):
    formseg = SegmentoSearchForm(request.GET)
    segmentos = formseg.search()
    return render_to_response('search/indexes/Segmento/segmento.html', {'segmentos': segmentos})
