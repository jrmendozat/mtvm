from django.conf.urls import patterns, url

from Mueble import views

urlpatterns = patterns('',
    url(r'^$', views.lista_mueble, name = 'lista_mueble'),
    url(r'^nuevo',views.add_mueble, name = 'add_mueble'),
    #url(r'^(?P<pk>\d+)/$', views.edit_sede, name = 'edit_sede'),
    #url(r'^delete/(?P<pk>\d+)$', views.delete_sede, name='delete_sede'),
    url(r'^tamanio_mueble/$', views.lista_tamanio_mueble, name = 'lista_tamanio_mueble'),
    url(r'^tamanio_mueble/nuevo',views.add_tamaniomueble, name = 'add_tamaniomueble'),
    #url(r'^tamanio_mueble/(?P<pk>\d+)/$', views.edit_tiposede, name = 'edit_tiposede'),
    #url(r'^tamanio_mueble/delete/(?P<pk>\d+)$', views.delete_tiposede, name='delete_tiposede'),
 )
