from django.conf.urls import patterns, url

from Direccion import views

urlpatterns = patterns('',
    url(r'^$', views.lista_direccion, name = 'lista_direccion'),
    url(r'^nuevo',views.add_direccion, name = 'add_direccion'),
    url(r'^tipo_direccion/$', views.lista_tipo_direccion, name = 'lista_tipo_direccion'),
    url(r'^tipo_direccion/nuevo', views.add_tipo_direccion, name = 'add_tipo_direccion'),
    url(r'^tipo_direccion/(?P<pk>\d+)/$', views.edit_tipo_direccion, name = 'edit_tipo_direccion'),
    url(r'^tipo_direccion/delete/(?P<pk>\d+)$', views.delete_tipo_direccion, name='delete_tipo_direccion'),
   )
