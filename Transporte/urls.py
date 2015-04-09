from django.conf.urls import patterns, url
from Transporte import views

urlpatterns = patterns('',
    url(r'^$', views.lista_transporte, name = 'lista_transporte'),
    url(r'^nuevo',views.add_transporte, name = 'add_transporte'),
    url(r'^(?P<pk>\d+)/$', views.editar_transporte, \
        name = 'editar_transporte'),
    url(r'^delete/(?P<pk>\d+)$', views.delete_transporte, \
        name='delete_transporte'),

    url(r'^transporte_vehiculo/(?P<id_transp>\d+)/$', views.lista_transporte_vehiculo, \
        name = 'lista_transporte_vehiculo'),
    url(r'^transporte_vehiculo/(?P<id_transp>\d+)/nuevo',views.add_transportevehiculo, \
        name = 'add_transportevehiculo'),
    url(r'^transporte_vehiculo/(?P<id_transp>\d+)/editar/(?P<pk>\d+)/$', \
        views.edit_transportevehiculo, name = 'edit_transportevehiculo'),
    url(r'^transporte_vehiculo/(?P<id_transp>\d+)/delete/(?P<pk>\d+)$',\
     views.delete_transportevehiculo, name='delete_transportevehiculo'),

    url(r'^equipamiento/(?P<id_transp>\d+)/$', views.lista_equipamiento_transporte, \
        name = 'lista_equipamiento_transporte'),
    url(r'^equipamiento/(?P<id_transp>\d+)/nuevo$', views.add_equipamientotransporte, \
        name = 'add_equipamientotransporte'),
    url(r'^equipamiento/(?P<id_transp>\d+)/editar/(?P<pk>\d+)/$', \
        views.edit_equipamientotransporte, name = 'edit_equipamientotransporte'),
    url(r'^equipamiento/(?P<id_transp>\d+)/delete/(?P<pk>\d+)$', \
        views.delete_equipamientotransporte, name='delete_equipamientotransporte'),

    url(r'^transporte_rol/$', views.lista_transporte_rol, \
        name = 'lista_transporte_rol'),
    url(r'^transporte_rol/nuevo',views.add_transporterol, \
        name = 'add_transporterol'),
    url(r'^transporte_rol/(?P<pk>\d+)/$', views.edit_transporterol, \
        name = 'edit_transporterol'),
    url(r'^transporte_rol/delete/(?P<pk>\d+)$', views.delete_transporterol, \
        name='delete_transporterol'),

    url(r'^transporte_cuadrilla/(?P<id_transp>\d+)/$', views.lista_transporte_cuadrilla, \
        name = 'lista_transporte_cuadrilla'),
    #url(r'^transporte_cuadrilla/(?P<id_transp>\d+)/nuevo$', views.add_transporte_cuadrilla_cliente, \
    #    name = 'add_transporte_cuadrilla_cliente'),
    #url(r'^transporte_cuadrilla/(?P<id_transp>\d+)/editar/(?P<pk>\d+)/$', views.edit_transporte_cuadrilla_cliente, \
    #    name = 'edit_transporte_cuadrilla_cliente'),
    #url(r'^transporte_cuadrilla/(?P<id_transp>\d+)/delete/(?P<pk>\d+)$', views.delete_equipamiento_cliente, \
    #    name='delete_equipamiento_cliente'),

)
