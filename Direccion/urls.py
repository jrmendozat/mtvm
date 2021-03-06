from django.conf.urls import patterns, url

from Direccion import views

urlpatterns = patterns('',
    url(r'^$', views.lista_direccion, name = 'lista_direccion'),
    url(r'^nuevo',views.add_direccion, name = 'add_direccion'),
    url(r'^tipo_direccion/$', views.lista_tipo_direccion, \
        name = 'lista_tipo_direccion'),
    url(r'^tipo_direccion/nuevo', views.add_tipo_direccion, \
        name = 'add_tipo_direccion'),
    url(r'^tipo_direccion/(?P<pk>\d+)/$', \
        views.edit_tipo_direccion, name = 'edit_tipo_direccion'),
    url(r'^tipo_direccion/delete/(?P<pk>\d+)$', \
        views.delete_tipo_direccion, name='delete_tipo_direccion'),
    url(r'^pais/$', views.lista_pais, name = 'lista_pais'),
    url(r'^pais/nuevo', views.add_pais, name = 'add_pais'),
    url(r'^pais/(?P<pk>\d+)/$', views.edit_pais, \
        name = 'edit_pais'),
    url(r'^pais/delete/(?P<pk>\d+)$', views.delete_pais, \
        name='delete_pais'),
    url(r'^provincia/$', views.lista_provincia, \
        name = 'lista_provincia'),
    url(r'^provincia/nuevo', views.add_provincia, \
        name = 'add_provincia'),
    url(r'^provincia/(?P<pk>\d+)/$', views.edit_provincia, \
        name = 'edit_provincia'),
    url(r'^provincia/delete/(?P<pk>\d+)$', views.delete_provincia, \
        name='delete_provincia'),
    url(r'^ciudad/$', views.lista_ciudad, \
        name = 'lista_ciudad'),
    url(r'^ciudad/nuevo', views.add_ciudad, \
        name = 'add_ciudad'),
    url(r'^ciudad/(?P<pk>\d+)/$', views.edit_ciudad, \
        name = 'edit_ciudad'),
    url(r'^ciudad/delete/(?P<pk>\d+)$', views.delete_ciudad, \
        name='delete_ciudad'),
    url(r'^zona/$', views.lista_zona, \
        name = 'lista_zona'),
    url(r'^zona/nuevo', views.add_zona, \
        name = 'add_zona'),
    url(r'^zona/(?P<pk>\d+)/$', views.edit_zona, \
        name = 'edit_zona'),
    url(r'^zona/delete/(?P<pk>\d+)$', views.delete_zona, \
        name='delete_zona'),

   )
