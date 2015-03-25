from django.conf.urls import patterns, url

from Condicion_pago import views

urlpatterns = patterns('',
    url(r'^$', views.lista_condicionpago, name = 'lista_condicionpago'),
    url(r'^nuevo',views.add_condicionpago, name = 'add_condicionpago'),
    url(r'^(?P<pk>\d+)/$', views.edit_condicionpago, name = 'edit_condicionpago'),
    url(r'^delete/(?P<pk>\d+)$', views.delete_condicionpago, name='delete_condicionpago'),
)
