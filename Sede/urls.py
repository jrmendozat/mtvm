from django.conf.urls import patterns, url

from Sede import views

urlpatterns = patterns('',
    url(r'^$', views.lista_sede, name = 'lista_sede'),
    url(r'^nuevo',views.add_sede, name = 'add_sede'),
    url(r'^(?P<pk>\d+)/$', views.edit_sede, name = 'edit_sede'),
    url(r'^delete/(?P<pk>\d+)$', views.delete_sede, name='delete_sede'),
    url(r'^tipo_sede/$', views.lista_tiposede, name = 'lista_tiposede'),
    url(r'^tipo_sede/nuevo',views.add_tiposede, name = 'add_tiposede'),
    url(r'^tipo_sede/(?P<pk>\d+)/$', views.edit_tiposede, name = 'edit_tiposede'),
    url(r'^tipo_sede/delete/(?P<pk>\d+)$', views.delete_tiposede, name='delete_tiposede'),
    url(r'^ambiente/$', views.lista_ambiente, name = 'lista_ambiente'),
    url(r'^ambiente/nuevo',views.add_ambiente, name = 'add_ambiente'),
    url(r'^ambiente/(?P<pk>\d+)/$', views.edit_ambiente, name = 'edit_ambiente'),
    url(r'^ambiente/delete/(?P<pk>\d+)$', views.delete_ambiente, name='delete_ambiente'),
    url(r'^ambiente/tipo/$', views.lista_tipoambiente, name = 'lista_tipoambiente'),
    url(r'^ambiente/tipo/nuevo',views.add_tipoambiente, name = 'add_tipoambiente'),
    url(r'^ambiente/tipo/(?P<pk>\d+)/$', views.edit_tipoambiente, name = 'edit_tipoambiente'),
    url(r'^ambiente/tipo/delete/(?P<pk>\d+)$', views.delete_tipoambiente, name='delete_tipoambiente'),
)
