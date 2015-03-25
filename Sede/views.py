from django.shortcuts import render, render_to_response, get_object_or_404
from Sede.models import Tipo_sede, Sede
from Sede.forms import TipoSedeForm, SedeForm
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse

# Create your views here.
# lista
def lista_tiposede(request):
    lista_tiposede = Tipo_sede.objects.all()
    context = {'lista_tiposede': lista_tiposede}
    return render(request, 'tiposede_lista.html', context)

def lista_sede(request):
    lista_sede = Sede.objects.all()
    context = {'lista_sede': lista_sede}
    return render(request, 'sede_lista.html', context)

# agregar nuevo
def add_tiposede(request):
    if request.method == 'POST':
        form_tiposede = TipoSedeForm(request.POST, request.FILES)
        if form_tiposede.is_valid():
            form_tiposede.save()
            return HttpResponseRedirect(reverse('utipocliente:lista_tiposede'))
    else:
        form_tiposede = TipoSedeForm()
    return render_to_response('tiposede_add.html', {'form_tiposede':form_tiposede, 'create': True}, context_instance = RequestContext(request))
