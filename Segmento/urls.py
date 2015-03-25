from django.conf.urls import patterns, url

from Segmento import views

urlpatterns = patterns('',
    url(r'^$', views.lista_segmento, name = 'lista_segmento'),
    url(r'^nuevo', views.add_segmento, name = 'add_segmento'),
    url(r'^(?P<pk>\d+)/$', views.edit_segmento, name = 'edit_segmento'),
    url(r'^delete/(?P<pk>\d+)$', views.mensaje_eliminar, name='mensaje_eliminar'),
    url(r'^buscar/', views.segmentos, name='segmentos'),

)
