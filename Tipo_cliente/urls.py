from django.conf.urls import patterns, url

from Tipo_cliente import views

urlpatterns = patterns('',
    url(r'^$', views.lista_tipocliente, name = 'lista_tipocliente'),
    url(r'^nuevo',views.add_tipocliente, name = 'add_tipocliente'),
    url(r'^(?P<pk>\d+)/$', views.edit_tipocliente, name = 'edit_tipocliente'),
    url(r'^delete/(?P<pk>\d+)$', views.delete_tipocliente, name='delete_tipocliente'),
    url(r'^tipo_precio/$', views.lista_tipoprecio, name = 'lista_tipoprecio'),
    url(r'^tipo_precio/nuevo',views.add_tipoprecio, name = 'add_tipoprecio'),
    url(r'^tipo_precio/(?P<pk>\d+)/$', views.edit_tipoprecio, name = 'edit_tipoprecio'),
    url(r'^tipo_precio/delete/(?P<pk>\d+)$', views.delete_tipoprecio, name='delete_tipoprecio'),
)
