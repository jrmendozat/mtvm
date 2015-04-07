from django.conf.urls import patterns, url

from Telefono import views

urlpatterns = patterns('',
    url(r'^$', views.lista_telefono, name = 'lista_telefono'),
    url(r'^nuevo',views.nuevo_telefono, name = 'nuevo_telefono'),
    url(r'^editar/(?P<id_telef>\d+)/$', views.editar_telefono),
    url(r'^delete/(?P<pk>\d+)$', views.Delete_telefono, \
        name='Delete_telefono'),
    url(r'^telefono/$', views.lista_tipo, name = 'lista_tipo'),
    url(r'^telefono/editar/(?P<id_telef>\d+)/$', \
        views.editar_telefono, name='editar_telefono'),
    url(r'^telefono/delete/(?P<pk>\d+)$', views.Delete_telefono, \
        name='Delete_telefono'),
    url(r'^tipo_telefono/$', views.lista_tipotelefono, \
        name = 'lista_tipotelefono'),
     url(r'^tipo_telefono/nuevo',views.nuevo_tipotelefono, \
        name = 'nuevo_tipotelefono'),
    url(r'^tipo_telefono/editar/(?P<pk>\d+)/$', \
        views.editar_tipotelefono, name='editar_tipotelefono'),
    url(r'^tipo_telefono/delete/(?P<pk>\d+)$', \
        views.Delete_tipotelefono, name='Delete_tipotelefono'),
)
