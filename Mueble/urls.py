from django.conf.urls import patterns, url

from Mueble import views

urlpatterns = patterns('',
    url(r'^$', views.lista_mueble, name = 'lista_mueble'),
    url(r'^nuevo',views.add_mueble, name = 'add_mueble'),
    url(r'^(?P<pk>\d+)/$', views.editar_mueble, name = 'editar_mueble'),
    url(r'^delete/(?P<pk>\d+)$', views.delete_mueble, name='delete_mueble'),
    url(r'^tamanio_mueble/$', views.lista_tamanio_mueble, name = 'lista_tamanio_mueble'),
    url(r'^tamanio_mueble/nuevo',views.add_tamaniomueble, name = 'add_tamaniomueble'),
    url(r'^tamanio_mueble/(?P<pk>\d+)/$', views.editar_tamanio_mueble, name = 'editar_tamanio_mueble'),
    url(r'^tamanio_mueble/delete/(?P<pk>\d+)$', views.delete_tamanio_mueble, name='delete_tamanio_mueble'),
    url(r'^tipo_peso/$', views.lista_tipo_peso, name = 'lista_tipo_peso'),
    url(r'^tipo_peso/nuevo',views.add_tipopeso, name = 'add_tipopeso'),
    url(r'^tipo_peso/(?P<pk>\d+)/$', views.editar_tipopeso, name = 'editar_tipopeso'),
    url(r'^tipo_peso/delete/(?P<pk>\d+)$', views.delete_tipopeso, name='delete_tipopeso'),
    url(r'^tipo_fragilidad/$', views.lista_tipo_fragilidad, name = 'lista_tipo_fragilidad'),
    url(r'^tipo_fragilidad/nuevo',views.add_tipofragilidad, name = 'add_tipofragilidad'),
    url(r'^tipo_fragilidad/(?P<pk>\d+)/$', views.editar_tipofragilidad, name = 'editar_tipofragilidad'),
    url(r'^tipo_fragilidad/delete/(?P<pk>\d+)$', views.delete_tipofragilidad, name='delete_tipofragilidad'),
    url(r'^familia_mueble/$', views.lista_familia_mueble, name = 'lista_familia_mueble'),
    url(r'^familia_mueble/nuevo',views.add_familiamueble, name = 'add_familiamueble'),
    url(r'^familia_mueble/(?P<pk>\d+)/$', views.editar_familiamueble, name = 'editar_familiamueble'),
    url(r'^familia_mueble/delete/(?P<pk>\d+)$', views.delete_familiamueble, name='delete_familiamueble'),

 )
