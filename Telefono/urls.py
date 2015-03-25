from django.conf.urls import patterns, url

from Telefono import views

urlpatterns = patterns('',
    url(r'^telefono/$', views.lista_tipo, name = 'lista_tipo'),
    url(r'^$', views.lista, name = 'lista'),
    url(r'^nuevo',views.nuevo_telefono, name = 'nuevo_telefono'),
    url(r'^editar/(?P<id_telef>\d+)/$', views.editar_telefono),
    url(r'^telefono/editar/(?P<id_telef>\d+)/$', views.editar_telefono, name='editar_telefono'),
    url(r'^telefono/delete/(?P<pk>\d+)$', views.Delete_telefono, name='Delete_telefono'),
)
