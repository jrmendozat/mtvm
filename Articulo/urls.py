from django.conf.urls import patterns, url
from Articulo import views

urlpatterns = patterns('',
    url(r'^$', views.lista_articulo, name='lista_articulo'),
    url(r'^nuevo',views.add_articulo, name='add_articulo'),
    url(r'^(?P<pk>\d+)/$', views.editar_articulo, \
        name = 'editar_articulo'),
    url(r'^delete/(?P<pk>\d+)$', views.delete_articulo, \
        name='delete_articulo'),
    url(r'^clase/$', views.lista_articulo_clase, \
        name = 'lista_articulo_clase'),
    url(r'^clase/nuevo',views.add_articuloclase, \
        name = 'add_articuloclase'),
    url(r'^clase/(?P<pk>\d+)/$', views.editar_articuloclase, \
        name = 'editar_articuloclase'),
    url(r'^clase/delete/(?P<pk>\d+)$', views.delete_articuloclase, \
        name='delete_articuloclase'),
    url(r'^subclase/$', views.lista_articulo_subclase, \
        name = 'lista_articulo_subclase'),
    url(r'^subclase/nuevo',views.add_articulosubclase, \
        name = 'add_articulosubclase'),
    url(r'^subclase/(?P<pk>\d+)/$', views.editar_articulosubclase, \
        name = 'editar_articulosubclase'),
    url(r'^subclase/delete/(?P<pk>\d+)$', \
        views.delete_articulosubclase, \
        name='delete_articulosubclase'),
    url(r'^categoria/$', views.lista_categoria_articulo, \
        name = 'lista_categoria_articulo'),
    url(r'^categoria/nuevo',views.add_categoriaarticulo, \
        name = 'add_categoriaarticulo'),
    url(r'^categoria/(?P<pk>\d+)/$', views.editar_categoriaarticulo, \
        name = 'editar_categoriaarticulo'),
    url(r'^categoria/delete/(?P<pk>\d+)$', \
        views.delete_categoriaarticulo, \
        name='delete_categoriaarticulo'),
    url(r'^subcategoria/$', views.lista_subcategoria_articulo, \
        name = 'lista_subcategoria_articulo'),
    url(r'^subcategoria/nuevo',views.add_subcategoriaarticulo, \
        name = 'add_subcategoriaarticulo'),
    url(r'^subcategoria/editar/(?P<pk>\d+)/$', \
        views.editar_subcategoriaarticulo, \
        name = 'editar_subcategoriaarticulo'),
    url(r'^subcategoria/delete/(?P<pk>\d+)$', \
        views.delete_subcategoriaarticulo, \
        name='delete_subcategoriaarticulo'),
    url(r'^tipo_costo/$', views.lista_tipo_costo, \
        name = 'lista_tipo_costo'),
    url(r'^tipo_costo/nuevo',views.add_tipocosto, \
        name = 'add_tipocosto'),
    url(r'^tipo_costo/(?P<pk>\d+)/$', \
        views.editar_tipocosto, \
        name = 'editar_tipocosto'),
    url(r'^tipo_costo/delete/(?P<pk>\d+)$', \
        views.delete_tipocosto, \
        name='delete_tipocosto'),
    url(r'^articulo_costo/(?P<id_art>\d+)/$', views.buscar_articulo_costo, \
        name = 'buscar_articulo_costo'),
    url(r'^articulo_costo/nuevo$', views.add_articulocosto, \
        name = 'add_articulocosto'),
    url(r'^articulo_costo/(?P<pk>\d+)/$', views.editar_articulocosto, \
        name = 'editar_articulocosto'),
    url(r'^articulo_costo/delete/(?P<pk>\d+)$', views.delete_articulocosto, \
        name='delete_articulocosto'),
    url(r'^unidad/$', views.lista_unidad, \
        name = 'lista_unidad'),
    url(r'^unidad/nuevo',views.add_unidad, \
        name = 'add_unidad'),
    url(r'^unidad/(?P<pk>\d+)/$', \
        views.editar_unidad, \
        name = 'editar_unidad'),
    url(r'^unidad/delete/(?P<pk>\d+)$', \
        views.delete_unidad, \
        name='delete_unidad'),
    url(r'^articulo_unidad/(?P<id_art>\d+)/$', views.buscar_articulo_costo, \
        name = 'buscar_articulo_costo'),
    url(r'^articulo_unidad/nuevo$', views.add_articulounidad, \
        name = 'add_articulounidad'),
    url(r'^articulo_unidad/(?P<pk>\d+)/$', views.editar_articulounidad, \
        name = 'editar_articulounidad'),
    url(r'^articulo_unidad/delete/(?P<pk>\d+)$', views.delete_articulounidad, \
        name='delete_articulounidad'),
    url(r'^articulo_precio/(?P<id_art>\d+)/$', views.buscar_articulo_precio, \
        name = 'buscar_articulo_precio'),
    url(r'^articulo_precio/nuevo$', views.add_articuloprecio, \
        name = 'add_articuloprecio'),
    url(r'^articulo_precio/(?P<pk>\d+)/$', views.editar_articuloprecio, \
        name = 'editar_articuloprecio'),
    url(r'^articulo_precio/delete/(?P<pk>\d+)$', views.delete_articuloprecio, \
        name='delete_articuloprecio'),
    url(r'^articulo_prueba/nuevo$', views.add_articuloprueba, \
        name = 'add_articuloprueba'),

)
