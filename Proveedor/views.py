from django.shortcuts import render, render_to_response, get_object_or_404
from Proveedor.models import Tipo_Proveedor, Proveedor, Proveedor_Telefono, \
Proveedor_Direccion, Email_Proveedor
from Proveedor.forms import TipoProveedorForm, ProveedorForm, \
ProveedorTelefonoForm, ProveedorDireccionForm, EmailProveedorForm
from Telefono.models import Telefono
from Telefono.forms import TelefonoForm
from Direccion.forms import DireccionForm
from Direccion.models import Direccion
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.template import RequestContext

# Create your views here.
#listas
def lista_tipo_proveedor(request):
    lista_tipoproveedor = Tipo_Proveedor.objects.all()
    context = {'lista_tipoproveedor': lista_tipoproveedor}
    return render(request, 'proveedor/tipoproveedor_lista.html', context)

def lista_proveedor(request):
    lista_proveedor = Proveedor.objects.all()
    context = {'lista_proveedor': lista_proveedor}
    return render(request, 'proveedor/proveedor_lista.html', context)

def lista_email_proveedor(request, id_prov):

    proveedor = Proveedor.objects.get(id = id_prov)

    lista_email = Email_Proveedor.objects.filter(proveedor_id=proveedor)
    context = {'lista_email': lista_email}
    return render(request, 'emailproveedor_lista.html', context)

#busqueda con filtros
def buscar_proveedortelefono(request, id_prov):

    proveedor = Proveedor.objects.get(id=id_prov)

    proveedortelefono = Proveedor_Telefono.objects.filter(proveedor=proveedor)

    context = {'proveedortelefono': proveedortelefono}
    return render(request, 'proveedortelefono_buscar.html', context)

def buscar_proveedordireccion(request, id_prov):

    proveedor = Proveedor.objects.get(id=id_prov)

    proveedordireccion = Proveedor_Direccion.objects.filter(proveedor=proveedor)

    context = {'proveedordireccion': proveedordireccion}
    return render(request, 'proveedordireccion_buscar.html', context)

# agregar nuevo
def add_tipoproveedor(request):
    if request.method == 'POST':
        form_tipoproveedor = TipoProveedorForm(request.POST)
        if form_tipoproveedor.is_valid():
            form_tipoproveedor.save()
            return HttpResponseRedirect(reverse('uproveedor:lista_tipo_proveedor'))
    else:
        form_tipoproveedor = TipoProveedorForm()
    return render_to_response('proveedor/tipoproveedor_add.html', \
        {'form_tipoproveedor':form_tipoproveedor, 'create': True}, \
        context_instance = RequestContext(request))

def add_proveedor(request):
    if request.method == 'POST':
        form_proveedor = ProveedorForm(request.POST)
        if form_proveedor.is_valid():
            form_proveedor.save()
            return HttpResponseRedirect(reverse('uproveedor:lista_proveedor'))
    else:
        form_proveedor = ProveedorForm()
    return render_to_response('proveedor/proveedor_add.html', \
        {'form_proveedor':form_proveedor, 'create': True}, \
        context_instance = RequestContext(request))

def add_proveedor_telefono(request, id_prov):

    proveedor = Proveedor.objects.get(id = id_prov)
    if request.method == 'POST':
        telefono_form = TelefonoForm(request.POST)

        if telefono_form.is_valid():
            obj_tel = telefono_form.save()
            telefono = Telefono.objects.get(id = obj_tel.id)

        provtel_form = ProveedorTelefonoForm(request.POST)
        if provtel_form.is_valid():
            formResult2 = provtel_form.save(commit = False)
            #luego de hacer el save anterior le metodo el ID al siguiente y listo
            formResult2.proveedor = proveedor
            formResult2.telefono = telefono
            formResult2.save()
    else:
        telefono_form = TelefonoForm()
        provtel_form = ProveedorTelefonoForm()

    return render_to_response('proveedor/telefonoproveedor_add.html', \
      {'telefono_form':telefono_form,'provtel_form':provtel_form,\
      'id_prov':id_prov, 'create': True}, context_instance = RequestContext(request))

def add_proveedor_direccion(request, id_prov):

    proveedor = Proveedor.objects.get(id = id_prov)
    if request.method == 'POST':

        direccion_form = DireccionForm(request.POST)

        if direccion_form.is_valid():
            obj_dir = direccion_form.save()
            direc = Direccion.objects.get(id=obj_dir.id)

        provdir_form = ProveedorDireccionForm(request.POST)
        if provdir_form.is_valid():
            formResult2 = provdir_form.save(commit = False)
            #luego de hacer el save anterior le metodo el ID al siguiente y listo
            formResult2.proveedor = proveedor
            formResult2.direc = direc
            formResult2.save()
    else:
        direccion_form = DireccionForm()
        provdir_form = ProveedorDireccionForm()

    return render_to_response('proveedor/direccionproveedor_add.html', \
      {'direccion_form':direccion_form,'provdir_form':provdir_form, \
       'id_prov':id_prov, 'create': True}, \
       context_instance = RequestContext(request))

def add_email_proveedor(request, id_prov):

    proveedor = Proveedor.objects.get(id = id_prov)

    if request.method == 'POST':

        emailform = EmailProveedorForm(request.POST)
        emailform.proveedor = proveedor
        if emailform.is_valid():
            formu = emailform.save(commit = False)
            formu.proveedor = proveedor
            formu.save()

            return HttpResponseRedirect('../')
    else:
        emailform = EmailProveedorForm()
    return render_to_response('proveedor/emailproveedor_add.html', {'emailform':emailform, \
         'create': True}, context_instance = RequestContext(request))

# editar un registro
def editar_tipoproveedor(request, pk):

    id_tipoprov = Tipo_Proveedor.objects.get(pk=pk)

    if request.method == 'POST':
        # formulario enviado
        editar_tipoproveedor = TipoProveedorForm(request.POST, instance=id_tipoprov)

        if editar_tipoproveedor.is_valid():
            # formulario validado correctamente
            editar_tipoproveedor.save()

            return HttpResponseRedirect(reverse('uproveedor:lista_tipo_proveedor'))
    else:
        # formulario inicial
        editar_tipoproveedor = TipoProveedorForm(instance=id_tipoprov)

    return render_to_response('proveedor/tipoproveedor_edit.html', \
        {'editar_tipoproveedor':editar_tipoproveedor, \
        'id_tipoprov':id_tipoprov, 'create':False}, \
        context_instance = RequestContext(request))

def editar_proveedor(request, pk):

    id_prov = Proveedor.objects.get(pk=pk)

    if request.method == 'POST':
        # formulario enviado
        editar_proveedor = ProveedorForm(request.POST, instance=id_prov)

        if editar_proveedor.is_valid():
            # formulario validado correctamente
            editar_proveedor.save()

            return HttpResponseRedirect(reverse('uproveedor:lista_proveedor'))
    else:
        # formulario inicial
        editar_proveedor = ProveedorForm(instance=id_prov)

    return render_to_response('proveedor/proveedor_edit.html', \
        {'editar_proveedor':editar_proveedor, \
        'id_prov':id_prov, 'create':False}, \
        context_instance = RequestContext(request))

def edit_telefono_proveedor(request, id_prov, pk):

    id_tele = Proveedor_Telefono.objects.values('telefono').filter(pk = pk)

    id_telefono=Telefono.objects.get(pk=id_tele)

    if request.method == 'POST':
        # formulario enviado
        form_edit_telefono = TelefonoForm(request.POST, instance=id_telefono)

        if form_edit_telefono.is_valid():
            # formulario validado correctamente
            form_edit_telefono.save()

            #return HttpResponseRedirect(reverse('uproveedors:lista_email'))
            return HttpResponseRedirect('../../')
    else:
        # formulario inicial
        form_edit_telefono = TelefonoForm(instance=id_telefono)

    return render_to_response('proveedor/telefonoproveedor_edit.html', \
         {'form_edit_telefono': form_edit_telefono, 'create':False}, \
         context_instance = RequestContext(request))

def edit_direccion_proveedor(request, id_prov, pk):

    id_dir = Proveedor_Direccion.objects.values('direc').filter(pk = pk)

    id_direcc=Direccion.objects.get(pk=id_dir)

    if request.method == 'POST':
        # formulario enviado
        form_edit_direccion = DireccionForm(request.POST, instance=id_direcc)

        if form_edit_direccion.is_valid():
            # formulario validado correctamente
            form_edit_direccion.save()

            #return HttpResponseRedirect(reverse('uproveedor(:lista_email'))
            return HttpResponseRedirect('../../')
    else:
        # formulario inicial
        form_edit_direccion = DireccionForm(instance=id_direcc)

    return render_to_response('proveedor/direccionproveedor_edit.html', \
         {'form_edit_direccion': form_edit_direccion, 'create':False}, \
         context_instance = RequestContext(request))

def edit_email_proveedor(request,id_prov, pk):

    id_email = Email_Proveedor.objects.get(pk = pk)

    if request.method == 'POST':
        # formulario enviado
        form_edit_email = EmailProveedorForm(request.POST, instance=id_email)

        if form_edit_email.is_valid():
            # formulario validado correctamente
            form_edit_email.save()

            #return HttpResponseRedirect(reverse('uclientes:lista_email'))
            return HttpResponseRedirect('../../')
    else:
        # formulario inicial
        form_edit_email = EmailProveedorForm(instance=id_email)

    return render_to_response('proveedor/emailproveedor_edit.html', \
         {'form_edit_email': form_edit_email, 'create':False}, \
         context_instance = RequestContext(request))

# eliminar un registro
def delete_tipoproveedor(request, pk, template_name='server_confirm_delete.html'):
    tipoproveedor = get_object_or_404(Tipo_Proveedor, pk=pk)
    if request.method == 'POST':
        tipoproveedor.delete()
        return HttpResponseRedirect('../')
    return render(request, template_name, \
        {'object':tipoproveedor})

def delete_proveedor(request, pk, template_name='server_confirm_delete.html'):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        proveedor.delete()
        return HttpResponseRedirect('../')
    return render(request, template_name, \
        {'object':proveedor})

def delete_email_proveedor(request, id_prov, pk, template_name='server_confirm_delete.html'):
    email = get_object_or_404(Email_Proveedor, pk=pk)
    if request.method == 'POST':
        email.delete()
        return HttpResponseRedirect('../')
    return render(request, template_name, {'object':email})

# probar estos eliminar si borran la relacion en la tablas intermedias
def delete_telefono_proveedor(request, id_prov, pk, template_name='server_confirm_delete.html'):
    telefono = get_object_or_404(Telefono, pk=pk)
    if request.method == 'POST':
        telefono.delete()
        return HttpResponseRedirect('../')
    return render(request, template_name, {'object':telefono})

def delete_direccion_proveedor(request, id_prov, pk, template_name='server_confirm_delete.html'):
    direccion = get_object_or_404(Direccion, pk=pk)
    if request.method == 'POST':
        direccion.delete()
        return HttpResponseRedirect('../')
    return render(request, template_name, {'object':direccion})
