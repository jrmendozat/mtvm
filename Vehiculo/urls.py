from django.conf.urls import patterns, url
from Vehiculo import views

urlpatterns = patterns('',
    url(r'^$', views.lista_vehiculo, name = 'lista_vehiculo'),
    url(r'^nuevo',views.add_vehiculo, name = 'add_vehiculo'),
    url(r'^(?P<pk>\d+)/$', views.editar_vehiculo, \
        name = 'editar_vehiculo'),
    url(r'^delete/(?P<pk>\d+)$', views.delete_vehiculo, \
        name='delete_vehiculo'),

    url(r'^tipo_vehiculo/$', views.lista_tipo_vehiculo, \
        name = 'lista_tipo_vehiculo'),
    url(r'^tipo_vehiculo/nuevo',views.add_tipovehiculo, \
        name = 'add_tipovehiculo'),
    url(r'^tipo_vehiculo/(?P<pk>\d+)/$', views.editar_tipovehiculo, \
        name = 'editar_tipovehiculo'),
    url(r'^tipo_vehiculo/delete/(?P<pk>\d+)$', views.delete_tipovehiculo, \
        name='delete_tipovehiculo'),

    url(r'^modelo_vehiculo/$', views.lista_modelo_vehiculo, \
        name = 'lista_modelo_vehiculo'),
    url(r'^modelo_vehiculo/nuevo',views.add_modelovehiculo, \
        name = 'add_modelovehiculo'),
    url(r'^modelo_vehiculo/(?P<pk>\d+)/$', views.editar_modelovehiculo, \
        name = 'editar_modelovehiculo'),
    url(r'^modelo_vehiculo/delete/(?P<pk>\d+)$', views.delete_modelovehiculo, \
        name='delete_modelovehiculo'),
)
