from django.shortcuts import render_to_response, render, get_object_or_404
from Cliente.forms import ClienteForm, ClienteTelefonoForm, EmailForm,\
 ClienteDireccionForm
from Cliente.models import Cliente, Email, Cliente_telefono, Cliente_Direccion
from Telefono.forms import TelefonoForm
from Telefono.models import Telefono
from Direccion.forms import DireccionForm
from Direccion.models import Direccion
from Sede.forms import SedeForm
from Sede.models import Sede
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.forms.formsets import formset_factory


# Create your views here.
# listas
def list_cliente(request):
    list_clie = Cliente.objects.all()
    context = {'list_clie': list_clie}
    return render(request, 'cliente_lista.html', context)

def lista_email(request, id_cli):

    cliente = Cliente.objects.get(id = id_cli)

    lista_email = Email.objects.filter(cliente_id=cliente)
    context = {'lista_email': lista_email}
    return render(request, 'emailcliente_lista.html', context)

def lista_telefono_cliente(request, id_cli):

    cliente = Cliente.objects.get(id = id_cli)

    lista_telefono_cliente=Cliente_telefono.objects.select_related().filter(cliente = cliente)

    context = {'lista_telefono_cliente': lista_telefono_cliente}
    return render(request, 'telefonocliente_lista.html', context)

def direccioncliente_lista(request, id_cli):

    cliente = Cliente.objects.get(id = id_cli)

    direccioncliente_lista=Cliente_Direccion.objects.filter(cliente=cliente)

    context = {'direccioncliente_lista': direccioncliente_lista}
    return render(request, 'direccioncliente_lista.html', context)

# agregar nuevo
def add_cliente(request):

    if request.method == 'POST':
        cliente_form = ClienteForm(request.POST)

        if cliente_form.is_valid():

            obj_cli = cliente_form.save()
            cliente = Cliente.objects.get(id = obj_cli.id)

            return HttpResponseRedirect('cliente/'+ cliente.id + '/')
    else:
        # formulario inicial
        cliente_form = ClienteForm()

    return render_to_response('cliente_add.html',\
     {'cliente_form': cliente_form, 'create':True},\
      context_instance = RequestContext(request))

def add_telefono_cliente(request, id_cli):

    cliente = Cliente.objects.get(id = id_cli)
    if request.method == 'POST':
        telefono_form = TelefonoForm(request.POST)

        if telefono_form.is_valid():
            obj_tel = telefono_form.save()
            telefono = Telefono.objects.get(id = obj_tel.id)

        clitel_form = ClienteTelefonoForm(request.POST)
        if clitel_form.is_valid():
            formResult2 = clitel_form.save(commit = False)
            #luego de hacer el save anterior le metodo el ID al siguiente y listo
            formResult2.cliente = cliente
            formResult2.telefono = telefono
            formResult2.save()
    else:
        telefono_form = TelefonoForm()
        clitel_form = ClienteTelefonoForm()

    return render_to_response('telefonocliente_add.html', \
     {'telefono_form':telefono_form,'clitel_form':clitel_form,\
     'id_cli':id_cli, 'create': True}, context_instance = RequestContext(request))

def add_email(request, id_cli):

    cliente = Cliente.objects.get(id = id_cli)

    if request.method == 'POST':

        emailform = EmailForm(request.POST)
        emailform.cliente = cliente
        if emailform.is_valid():
            formu = emailform.save(commit = False)
            formu.cliente = cliente
            formu.save()

            return HttpResponseRedirect('../')
    else:
        emailform = EmailForm()
    return render_to_response('Emailcliente_add.html', {'emailform':emailform, \
        'create': True}, context_instance = RequestContext(request))

def add_direccion_cliente(request, id_cli):

    cliente = Cliente.objects.get(id = id_cli)
    if request.method == 'POST':

        direccion_form = DireccionForm(request.POST)
        sede_form = SedeForm(request.POST)

        if direccion_form.is_valid():
            obj_dir = direccion_form.save()
            direc = Direccion.objects.get(id = obj_dir.id)

        if sede_form.is_valid():
            obj_sede = sede_form.save()
            sede = Sede.objects.get(id = obj_sede.id)

        clidir_form = ClienteDireccionForm(request.POST)
        if clidir_form.is_valid():
            formResult2 = clidir_form.save(commit = False)
            #luego de hacer el save anterior le metodo el ID al siguiente y listo
            formResult2.cliente = cliente
            formResult2.direc = direc
            formResult2.sede = sede
            formResult2.save()
    else:
        direccion_form = DireccionForm()
        sede_form = SedeForm()
        clidir_form = ClienteDireccionForm()

    return render_to_response('direccioncliente_add.html', \
     {'direccion_form':direccion_form,'clidir_form':clidir_form, \
     'sede_form':sede_form, 'id_cli':id_cli, 'create': True}, \
      context_instance = RequestContext(request))

# editar un registro
def editar_cliente(request, id_cli):

    id_clie = Cliente.objects.get(pk = id_cli)

    if request.method == 'POST':
        # formulario enviado
        editar_clie = ClienteForm(request.POST, instance=id_clie)

        if editar_clie.is_valid():
            # formulario validado correctamente
            editar_clie.save()

            return HttpResponseRedirect(reverse('uclientes:list_cliente'))

    else:
        # formulario inicial
        editar_clie = ClienteForm(instance=id_clie)

    return render_to_response('cliente_edit.html', {'editar_clie': editar_clie, 'id_cli':id_cli, 'create':False}, context_instance = RequestContext(request))

def edit_email(request,id_cli, pk):

    id_email = Email.objects.get(pk = pk)

    if request.method == 'POST':
        # formulario enviado
        form_edit_email = EmailForm(request.POST, instance=id_email)

        if form_edit_email.is_valid():
            # formulario validado correctamente
            form_edit_email.save()

            #return HttpResponseRedirect(reverse('uclientes:lista_email'))
            return HttpResponseRedirect('../../')
    else:
        # formulario inicial
        form_edit_email = EmailForm(instance=id_email)

    return render_to_response('emailcliente_edit.html', {'form_edit_email': form_edit_email, 'create':False}, context_instance = RequestContext(request))

def edit_telefono_cliente(request, id_cli, pk):

    id_tele = Cliente_telefono.objects.values('telefono').filter(pk = pk)

    id_telefono=Telefono.objects.get(pk=id_tele)

    if request.method == 'POST':
        # formulario enviado
        form_edit_telefono = TelefonoForm(request.POST, instance=id_telefono)

        if form_edit_telefono.is_valid():
            # formulario validado correctamente
            form_edit_telefono.save()

            #return HttpResponseRedirect(reverse('uclientes:lista_email'))
            return HttpResponseRedirect('../../')
    else:
        # formulario inicial
        form_edit_telefono = TelefonoForm(instance=id_telefono)

    return render_to_response('telefonocliente_edit.html', \
        {'form_edit_telefono': form_edit_telefono, 'create':False}, \
        context_instance = RequestContext(request))

def direccion_cliente_edit(request, id_cli, pk):

    id_dir = Cliente_Direccion.objects.values('direc').filter(pk = pk)

    id_direcc=Direccion.objects.get(pk=id_dir)

    if request.method == 'POST':
        # formulario enviado
        form_edit_direccion = DireccionForm(request.POST, instance=id_direcc)

        if form_edit_direccion.is_valid():
            # formulario validado correctamente
            form_edit_direccion.save()

            #return HttpResponseRedirect(reverse('uclientes:lista_email'))
            return HttpResponseRedirect('../../')
    else:
        # formulario inicial
        form_edit_direccion = DireccionForm(instance=id_direcc)

    return render_to_response('direccioncliente_edit.html', \
        {'form_edit_direccion': form_edit_direccion, 'create':False}, \
        context_instance = RequestContext(request))

# eliminar un registro
def delete_email(request, id_cli, pk, template_name='server_confirm_delete.html'):
    email = get_object_or_404(Email, pk=pk)
    if request.method == 'POST':
        email.delete()
        return HttpResponseRedirect('../')
    return render(request, template_name, {'object':email})

def delete_telefono_cliente(request, id_cli, pk, template_name='server_confirm_delete.html'):
    telefono = get_object_or_404(Telefono, pk=pk)
    if request.method == 'POST':
        telefono.delete()
        return HttpResponseRedirect('../')
    return render(request, template_name, {'object':telefono})

def add_telefono_cliente2(request, id_cli):

    cliente = Cliente.objects.get(id = id_cli)

    telefonoformset = formset_factory(TelefonoForm, extra = 2)
    clitelformset = formset_factory(ClienteTelefonoForm, extra = 2)

    if request.method == 'POST':

        telefono_formset = telefonoformset(request.POST)
        clitel_formset = clitelformset(request.POST)

        if telefono_formset.is_valid() and clitel_formset.is_valid():
            for form in telefono_formset:
                print form
                obj_tel = form.save()
                telefono = Telefono.objects.get(id = obj_tel.id)

                for form in clitel_formset:
                    print form
                    formResult2 = form.save(commit = False)
                    #luego de hacer el save anterior le metodo el ID al siguiente y listo
                    formResult2.cliente = cliente
                    formResult2.telefono = telefono
                    formResult2.save()
    else:
        telefono_formset = telefonoformset()
        clitel_formset = clitelformset()

    return render_to_response('telefonocliente_add.html', {'telefono_formset':telefono_formset,'clitel_formset':clitel_formset,'id_cli':id_cli, 'create': True}, context_instance = RequestContext(request))


#add_cliente con telefono
def add_cliente_tele(request):

    if request.method == 'POST':
        cliente_form = ClienteForm(request.POST)
        telefono_form = TelefonoForm(request.POST)
        clitel_form = ClienteTelefonoForm(request.POST)

        if cliente_form.is_valid() and telefono_form.is_valid():
            obj_cli = cliente_form.save()
            obj_tel = telefono_form.save()

            cliente = Cliente.objects.get(id = obj_cli.id)
            telefono = Telefono.objects.get(id = obj_tel.id)

            if clitel_form.is_valid():
                formResult2 = clitel_form.save(commit = False)
                #luego de hacer el save anterior le metodo el ID al siguiente y listo
                formResult2.cliente = cliente
                formResult2.telefono = telefono
                formResult2.save()


            return HttpResponseRedirect('/telefono/telefono')
    else:
        # formulario inicial
        cliente_form = ClienteForm()
        telefono_form = TelefonoForm()
        clitel_form = ClienteTelefonoForm()

    return render_to_response('prueba.html', {'cliente_form': cliente_form, 'telefono_form': telefono_form, 'clitel_form': clitel_form, 'create': True }, context_instance = RequestContext(request))

def ver_ficha_cliente(request, id_cli):

    cliente_individual = Cliente.objects.filter(pk = id_cli)
    lista_email = yus(id_cli)

    lista_telefono_cliente = Cliente_telefono.objects.select_related().filter(cliente = id_cli)

    direccioncliente_lista=Cliente_Direccion.objects.filter(cliente=id_cli)

    context = {'cliente_individual': cliente_individual, 'lista_email': lista_email, \
    'lista_telefono_cliente': lista_telefono_cliente, 'direccioncliente_lista': direccioncliente_lista}
    return render(request, 'cliente_ficha.html', context)

def yus(id_cli):

     lista_email = Email.objects.filter(cliente_id=id_cli)
     return lista_email
