from django.shortcuts import render, render_to_response, \
get_object_or_404
from Articulo.models import Articulo_Clase, \
Articulo_Subclase, Categoria_Articulo, \
Subcategoria_articulo, Articulo, Tipo_Costo, \
Articulo_Costo, Unidad, Articulo_Unidad, \
Articulo_Precio
from Articulo.forms import ArticuloClaseForm, \
ArticuloSubclaseForm, CategoriaArticuloForm, \
SubcategoriaArticuloForm, ArticuloForm, TipoCostoForm, \
ArticuloCostoForm, ArticulopruebaForm, UnidadForm, \
ArticuloUnidadForm, ArticuloPrecioForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.template import RequestContext

# Create your views here.
#listas
def lista_articulo_clase(request):
    lista_articuloclase = Articulo_Clase.objects.all()
    context = {'lista_articuloclase': lista_articuloclase}
    return render(request, 'articulo/articuloclase_lista.html', context)

def lista_articulo_subclase(request):
    lista_articulosubclase = Articulo_Subclase.objects.all()
    context = {'lista_articulosubclase': lista_articulosubclase}
    return render(request, 'articulo/articulosubclase_lista.html', context)

def lista_categoria_articulo(request):
    lista_categoriaarticulo = Categoria_Articulo.objects.all()
    context = {'lista_categoriaarticulo': lista_categoriaarticulo}
    return render(request, 'articulo/categoriaarticulo_lista.html', context)

def lista_subcategoria_articulo(request):
    lista_subcategoriaarticulo = Subcategoria_articulo.objects.all()
    context = {'lista_subcategoriaarticulo': lista_subcategoriaarticulo}
    return render(request, 'articulo/subcategoriaarticulo_lista.html', context)

def lista_articulo(request):
    lista_articulo = Articulo.objects.all()
    context = {'lista_articulo': lista_articulo}
    return render(request, 'articulo/articulo_lista.html', context)

def lista_tipo_costo(request):
    lista_tipocosto = Tipo_Costo.objects.all()
    context = {'lista_tipocosto': lista_tipocosto}
    return render(request, 'articulo/tipocosto_lista.html', context)

def lista_unidad(request):
    unidad = Unidad.objects.all()
    context = {'lista_unidad': unidad}
    return render(request, 'articulo/unidad_lista.html', context)

#busqueda con filtros
def buscar_articulo_costo(request, id_art):

    articulo = Articulo.objects.get(id = id_art)

    articulocosto = Articulo_Costo.objects.filter(articulo=articulo)

    context = {'articulocosto': articulocosto}
    return render(request, 'articulocosto_buscar.html', context)

def buscar_articulo_unidad(request, id_art):

    articulo = Articulo.objects.get(id = id_art)

    articulounidad = Articulo_Unidad.objects.filter(articulo=articulo)

    context = {'articulounidad': articulounidad}
    return render(request, 'articulounidad_buscar.html', context)

def buscar_articulo_precio(request, id_art):

    articulo = Articulo.objects.get(id = id_art)

    articuloprecio = Articulo_Precio.objects.filter(articulo=articulo)

    context = {'articuloprecio': articuloprecio}
    return render(request, 'articuloprecio_buscar.html', context)

# agregar nuevo
def add_articuloclase(request):
    if request.method == 'POST':
        form_articuloclase = ArticuloClaseForm(request.POST)
        if form_articuloclase.is_valid():
            form_articuloclase.save()
            return HttpResponseRedirect(reverse('uarticulo:lista_articulo_clase'))
    else:
        form_articuloclase = ArticuloClaseForm()
    return render_to_response('articulo/articuloclase_add.html', \
        {'form_articuloclase':form_articuloclase, 'create': True}, \
        context_instance = RequestContext(request))

def add_articulosubclase(request):
    if request.method == 'POST':
        form_articulosubclase = ArticuloSubclaseForm(request.POST)
        if form_articulosubclase.is_valid():
            form_articulosubclase.save()
            return HttpResponseRedirect(reverse('uarticulo:lista_articulo_subclase'))
    else:
        form_articulosubclase = ArticuloSubclaseForm()
    return render_to_response('articulo/articulosubclase_add.html', \
        {'form_articulosubclase':form_articulosubclase, 'create': True}, \
        context_instance = RequestContext(request))

def add_categoriaarticulo(request):
    if request.method == 'POST':
        form_categoriaarticulo = CategoriaArticuloForm(request.POST)
        if form_categoriaarticulo.is_valid():
            form_categoriaarticulo.save()
            return HttpResponseRedirect(reverse('uarticulo:lista_categoria_articulo'))
    else:
        form_categoriaarticulo = CategoriaArticuloForm()
    return render_to_response('articulo/categoriaarticulo_add.html', \
        {'form_categoriaarticulo':form_categoriaarticulo, 'create': True}, \
        context_instance = RequestContext(request))

def add_subcategoriaarticulo(request):
    if request.method == 'POST':
        form_subcategoriaarticulo = SubcategoriaArticuloForm(request.POST)
        if form_subcategoriaarticulo.is_valid():
            form_subcategoriaarticulo.save()
            return HttpResponseRedirect(reverse('uarticulo:lista_subcategoria_articulo'))
    else:
        form_subcategoriaarticulo = SubcategoriaArticuloForm()
    return render_to_response('articulo/subcategoriaarticulo_add.html', \
        {'form_subcategoriaarticulo':form_subcategoriaarticulo, 'create': True}, \
        context_instance = RequestContext(request))

def add_articulo(request):
    if request.method == 'POST':
        form_articulo = ArticuloForm(request.POST)
        if form_articulo.is_valid():
            form_articulo.save()
            return HttpResponseRedirect(reverse('uarticulo:lista_articulo'))
    else:
        form_articulo = ArticuloForm()
    return render_to_response('articulo/articulo_add.html', \
        {'form_articulo':form_articulo, 'create': True}, \
        context_instance = RequestContext(request))

def add_tipocosto(request):
    if request.method == 'POST':
        form_tipocosto = TipoCostoForm(request.POST)
        if form_tipocosto.is_valid():
            form_tipocosto.save()
            return HttpResponseRedirect(reverse('uarticulo:lista_tipo_costo'))
    else:
        form_tipocosto = TipoCostoForm()
    return render_to_response('articulo/tipocosto_add.html', \
        {'form_tipocosto':form_tipocosto, 'create': True}, \
        context_instance = RequestContext(request))

def add_articulocosto(request):
    if request.method == 'POST':
        form_articulocosto = ArticuloCostoForm(request.POST)
        if form_articulocosto.is_valid():
            form_articulocosto.save()
            return HttpResponseRedirect(reverse('uarticulo:lista_articulo'))
    else:
        form_articulocosto = ArticuloCostoForm()
    return render_to_response('articulo/articulocosto_add.html', \
        {'form_articulocosto':form_articulocosto, 'create': True}, \
        context_instance = RequestContext(request))

def add_unidad(request):
    if request.method == 'POST':
        form_unidad = UnidadForm(request.POST)
        if form_unidad.is_valid():
            form_unidad.save()
            return HttpResponseRedirect(reverse('uarticulo:lista_unidad'))
    else:
        form_unidad = UnidadForm()
    return render_to_response('articulo/unidad_add.html', \
        {'form_unidad':form_unidad, 'create': True}, \
        context_instance = RequestContext(request))

def add_articulounidad(request):
    if request.method == 'POST':
        form_articulounidad = ArticuloUnidadForm(request.POST)
        if form_articulounidad.is_valid():
            form_articulounidad.save()
            return HttpResponseRedirect(reverse('uarticulo:lista_articulo'))
    else:
        form_articulounidad = ArticuloUnidadForm()
    return render_to_response('articulo/articulounidad_add.html', \
        {'form_articulounidad':form_articulounidad, 'create': True}, \
        context_instance = RequestContext(request))

def add_articuloprecio(request):
    if request.method == 'POST':
        form_articuloprecio = ArticuloPrecioForm(request.POST)
        if form_articuloprecio.is_valid():
            form_articuloprecio.save()
            return HttpResponseRedirect(reverse('uarticulo:lista_articulo'))
    else:
        form_articuloprecio = ArticuloPrecioForm()
    return render_to_response('articulo/articuloprecio_add.html', \
        {'form_articuloprecio':form_articuloprecio, 'create': True}, \
        context_instance = RequestContext(request))

# editar un registro
def editar_articuloclase(request, pk):

    id_clase = Articulo_Clase.objects.get(pk=pk)

    if request.method == 'POST':
        # formulario enviado
        editar_articuloclase = ArticuloClaseForm(request.POST, instance=id_clase)

        if editar_articuloclase.is_valid():
            # formulario validado correctamente
            editar_articuloclase.save()

            return HttpResponseRedirect(reverse('uarticulo:lista_articulo_clase'))
    else:
        # formulario inicial
        editar_articuloclase = ArticuloClaseForm(instance=id_clase)

    return render_to_response('articulo/articuloclase_edit.html', \
        {'editar_articuloclase':editar_articuloclase, \
        'id_clase':id_clase, 'create':False}, \
        context_instance = RequestContext(request))

def editar_articulosubclase(request, pk):

    id_subclase = Articulo_Subclase.objects.get(pk=pk)

    if request.method == 'POST':
        # formulario enviado
        editar_articulosubclase = ArticuloSubclaseForm(request.POST, instance=id_subclase)

        if editar_articulosubclase.is_valid():
            # formulario validado correctamente
            editar_articulosubclase.save()

            return HttpResponseRedirect(reverse('uarticulo:lista_articulo_subclase'))
    else:
        # formulario inicial
        editar_articulosubclase = ArticuloSubclaseForm(instance=id_subclase)

    return render_to_response('articulo/articulosubclase_edit.html', \
        {'editar_articulosubclase':editar_articulosubclase, \
        'id_subclase':id_subclase, 'create':False}, \
        context_instance = RequestContext(request))

def editar_categoriaarticulo(request, pk):

    id_categoria = Categoria_Articulo.objects.get(pk=pk)

    if request.method == 'POST':
        # formulario enviado
        editar_categoriaarticulo = CategoriaArticuloForm(request.POST, instance=id_categoria)

        if editar_categoriaarticulo.is_valid():
            # formulario validado correctamente
            editar_categoriaarticulo.save()

            return HttpResponseRedirect(reverse('uarticulo:lista_categoria_articulo'))
    else:
        # formulario inicial
        editar_categoriaarticulo = CategoriaArticuloForm(instance=id_categoria)

    return render_to_response('articulo/categoriaarticulo_edit.html', \
        {'editar_categoriaarticulo':editar_categoriaarticulo, \
        'id_categoria':id_categoria, 'create':False}, \
        context_instance = RequestContext(request))

def editar_subcategoriaarticulo(request, pk):

    id_subcategoria = Subcategoria_articulo.objects.get(pk=pk)

    if request.method == 'POST':
        # formulario enviado
        editar_subcategoriaarticulo = SubcategoriaArticuloForm(request.POST,instance=id_subcategoria)

        if editar_subcategoriaarticulo.is_valid():
            # formulario validado correctamente
            editar_subcategoriaarticulo.save()

            return HttpResponseRedirect(reverse('uarticulo:lista_subcategoria_articulo'))
    else:
        # formulario inicial
        editar_subcategoriaarticulo = SubcategoriaArticuloForm(instance=id_subcategoria)

    return render_to_response('articulo/subcategoriaarticulo_edit.html', \
        {'editar_subcategoriaarticulo':editar_subcategoriaarticulo, \
        'id_subcategoria':id_subcategoria, 'create':False}, \
        context_instance = RequestContext(request))

def editar_articulo(request, pk):

    id_articulo = Articulo.objects.get(pk=pk)

    if request.method == 'POST':
        # formulario enviado
        editar_articulo = ArticuloForm(request.POST,instance=id_articulo)

        if editar_articulo.is_valid():
            # formulario validado correctamente
            editar_articulo.save()

            return HttpResponseRedirect(reverse('uarticulo:lista_articulo'))
    else:
        # formulario inicial
        editar_articulo = ArticuloForm(instance=id_articulo)

    return render_to_response('articulo/articulo_edit.html', \
        {'editar_articulo':editar_articulo, \
        'id_articulo':id_articulo, 'create':False}, \
        context_instance = RequestContext(request))

def editar_tipocosto(request, pk):

    id_tipocosto = Tipo_Costo.objects.get(pk=pk)

    if request.method == 'POST':
        # formulario enviado
        editar_tipocosto = TipoCostoForm(request.POST,instance=id_tipocosto)

        if editar_tipocosto.is_valid():
            # formulario validado correctamente
            editar_tipocosto.save()

            return HttpResponseRedirect(reverse('uarticulo:lista_tipo_costo'))
    else:
        # formulario inicial
        editar_tipocosto = TipoCostoForm(instance=id_tipocosto)

    return render_to_response('articulo/tipocosto_edit.html', \
        {'editar_tipocosto':editar_tipocosto, \
        'id_tipocosto':id_tipocosto, 'create':False}, \
        context_instance = RequestContext(request))

def editar_articulocosto(request, pk):

    id_articulocosto = Articulo_Costo.objects.get(pk=pk)

    if request.method == 'POST':
        # formulario enviado
        editar_articulocosto = ArticuloCostoForm(request.POST,instance=id_articulocosto)

        if editar_articulocosto.is_valid():
            # formulario validado correctamente
            editar_articulocosto.save()

            return HttpResponseRedirect(reverse('uarticulo:lista_articulo'))
    else:
        # formulario inicial
        editar_articulocosto = ArticuloCostoForm(instance=id_articulocosto)

    return render_to_response('articulo/articulocosto_edit.html', \
        {'editar_articulocosto':editar_articulocosto, \
        'id_articulocosto':id_articulocosto, 'create':False}, \
        context_instance = RequestContext(request))

def editar_unidad(request, pk):

    id_unidad = Unidad.objects.get(pk=pk)

    if request.method == 'POST':
        # formulario enviado
        editar_unidad = UnidadForm(request.POST,instance=id_unidad)

        if editar_unidad.is_valid():
            # formulario validado correctamente
            editar_unidad.save()

            return HttpResponseRedirect(reverse('uarticulo:lista_unidad'))
    else:
        # formulario inicial
        editar_unidad = UnidadForm(instance=id_unidad)

    return render_to_response('articulo/unidad_edit.html', \
        {'editar_unidad':editar_unidad, \
        'id_unidad':id_unidad, 'create':False}, \
        context_instance = RequestContext(request))

def editar_articulounidad(request, pk):

    id_articulounidad = Articulo_Costo.objects.get(pk=pk)

    if request.method == 'POST':
        # formulario enviado
        editar_articulounidad = ArticuloUnidadForm(request.POST,instance=id_articulounidad)

        if editar_articulounidad.is_valid():
            # formulario validado correctamente
            editar_articulounidad.save()

            return HttpResponseRedirect(reverse('uarticulo:lista_articulo'))
    else:
        # formulario inicial
        editar_articulounidad = ArticuloUnidadForm(instance=id_articulounidad)

    return render_to_response('articulo/articulounidad_edit.html', \
        {'editar_articulounidad':editar_articulounidad, \
        'id_articulounidad':id_articulounidad, 'create':False}, \
        context_instance = RequestContext(request))

def editar_articuloprecio(request, pk):

    id_articuloprecio = Articulo_Costo.objects.get(pk=pk)

    if request.method == 'POST':
        # formulario enviado
        editar_articuloprecio = ArticuloPrecioForm(request.POST,instance=id_articuloprecio)

        if editar_articuloprecio.is_valid():
            # formulario validado correctamente
            editar_articuloprecio.save()

            return HttpResponseRedirect(reverse('uarticulo:lista_articulo'))
    else:
        # formulario inicial
        editar_articuloprecio = ArticuloPrecioForm(instance=id_articuloprecio)

    return render_to_response('articulo/articuloprecio_edit.html', \
        {'editar_articuloprecio':editar_articuloprecio, \
        'id_articuloprecio':id_articuloprecio, 'create':False}, \
        context_instance = RequestContext(request))

# eliminar un registro
def delete_articuloclase(request, pk, template_name='server_confirm_delete.html'):
    articuloclase = get_object_or_404(Articulo_Clase, pk=pk)
    if request.method == 'POST':
        articuloclase.delete()
        return HttpResponseRedirect('../')
    return render(request, template_name, \
        {'object':articuloclase})

def delete_articulosubclase(request, pk, template_name='server_confirm_delete.html'):
    articulosubclase = get_object_or_404(Articulo_Subclase, pk=pk)
    if request.method == 'POST':
        articulosubclase.delete()
        return HttpResponseRedirect('../')
    return render(request, template_name, \
        {'object':articulosubclase})

def delete_categoriaarticulo(request, pk, template_name='server_confirm_delete.html'):
    categoriaarticulo = get_object_or_404(Categoria_Articulo, pk=pk)
    if request.method == 'POST':
        categoriaarticulo.delete()
        return HttpResponseRedirect('../')
    return render(request, template_name, \
        {'object':categoriaarticulo})

def delete_subcategoriaarticulo(request, pk, template_name='server_confirm_delete.html'):
    subcategoriaarticulo = get_object_or_404(Subcategoria_articulo, pk=pk)
    if request.method == 'POST':
        subcategoriaarticulo.delete()
        return HttpResponseRedirect('../')
    return render(request, template_name, \
        {'object':subcategoriaarticulo})

def delete_articulo(request, pk, template_name='server_confirm_delete.html'):
    articulo = get_object_or_404(Articulo, pk=pk)
    if request.method == 'POST':
        articulo.delete()
        return HttpResponseRedirect('../')
    return render(request, template_name, \
        {'object':articulo})

def delete_tipocosto(request, pk, template_name='server_confirm_delete.html'):
    tipocosto = get_object_or_404(Tipo_Costo, pk=pk)
    if request.method == 'POST':
        tipocosto.delete()
        return HttpResponseRedirect('../')
    return render(request, template_name, \
        {'object':tipocosto})

def delete_articulocosto(request, pk, template_name='server_confirm_delete.html'):
    articulocosto = get_object_or_404(Articulo_Costo, pk=pk)
    if request.method == 'POST':
        articulocosto.delete()
        return HttpResponseRedirect('../')
    return render(request, template_name, \
        {'object':articulocosto})

def delete_unidad(request, pk, template_name='server_confirm_delete.html'):
    unidad = get_object_or_404(Unidad, pk=pk)
    if request.method == 'POST':
        unidad.delete()
        return HttpResponseRedirect('../')
    return render(request, template_name, \
        {'object':unidad})

def delete_articulounidad(request, pk, template_name='server_confirm_delete.html'):
    articulounidad = get_object_or_404(Articulo_Unidad, pk=pk)
    if request.method == 'POST':
        articulounidad.delete()
        return HttpResponseRedirect('../')
    return render(request, template_name, \
        {'object':articulounidad})

def delete_articuloprecio(request, pk, template_name='server_confirm_delete.html'):
    articuloprecio = get_object_or_404(Articulo_Precio, pk=pk)
    if request.method == 'POST':
        articuloprecio.delete()
        return HttpResponseRedirect('../')
    return render(request, template_name, \
        {'object':articuloprecio})


# prueba

def add_articuloprueba(request):
    if request.method == 'POST':
        form_articulo = ArticulopruebaForm(request.POST)
        form_unidad = UnidadForm(request.POST)
        art_unid = ArticuloUnidadForm(request.POST)
        if form_articulo.is_valid() and form_unidad.is_valid():
            obj_art = form_articulo.save()
            obj_uni = form_unidad.save()

            articulo = Articulo.objects.get(id = obj_art.id)
            unidad = Unidad.objects.get(id = obj_uni.id)

            if art_unid.is_valid():
                formResult2 = art_unid.save(commit = False)
                #luego de hacer el save anterior le metodo el ID al siguiente y listo
                formResult2.articulo = articulo
                formResult2.unidad = unidad
                formResult2.save()

            return HttpResponseRedirect('../')
    else:
        # formulario inicial
        form_articulo = ArticulopruebaForm()
        form_unidad = UnidadForm()
        art_unid = ArticuloUnidadForm()

    return render_to_response('articulo/articuloprueba_add.html', \
        {'form_articulo': form_articulo, \
        'form_unidad': form_unidad, \
        'art_unid': art_unid, 'create': True }, \
        context_instance = RequestContext(request))


