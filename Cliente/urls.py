from django.conf.urls import patterns, url

from Cliente import views

urlpatterns = patterns('',
    url(r'^$', views.list_cliente, name = 'list_cliente'),
    url(r'^nuevo',views.add_cliente, name = 'add_cliente'),
    url(r'^(?P<id_cli>\d+)/$', views.editar_cliente, name = 'editar_cliente'),
    url(r'^telefono/(?P<id_cli>\d+)/$', views.lista_telefono_cliente, \
        name = 'lista_telefono_cliente'),
    url(r'^telefono/(?P<id_cli>\d+)/nuevo$', views.add_telefono_cliente, \
        name = 'add_telefono_cliente'),
    url(r'^telefono/(?P<id_cli>\d+)/editar/(?P<pk>\d+)/$', views.edit_telefono_cliente, \
        name = 'edit_telefono_cliente'),
    url(r'^telefono/(?P<id_cli>\d+)/delete/(?P<pk>\d+)$', views.delete_telefono_cliente, \
        name='delete_telefono_cliente'),
    url(r'^email/(?P<id_cli>\d+)/$', views.lista_email, name = 'lista_email'),
    url(r'^email/(?P<id_cli>\d+)/nuevo',views.add_email, name = 'add_email'),
    url(r'^email/(?P<id_cli>\d+)/editar/(?P<pk>\d+)/$', views.edit_email, \
        name = 'edit_email'),
    url(r'^email/(?P<id_cli>\d+)/delete/(?P<pk>\d+)$', views.delete_email, \
        name='delete_email'),
    url(r'^direccion/(?P<id_cli>\d+)/nuevo$', views.add_direccion_sede_cliente, \
        name = 'add_direccion_sede_cliente'),
    url(r'^direccion/(?P<id_cli>\d+)/$', views.direccioncliente_lista,\
     name = 'direccioncliente_lista'),
    url(r'^direccion/(?P<id_cli>\d+)/editar/(?P<pk>\d+)/$', views.direccion_cliente_edit, \
        name = 'direccion_cliente_edit'),
    url(r'^cliente_ficha/(?P<id_cli>\d+)/$', views.ver_ficha_cliente, \
        name = 'ver_ficha_cliente'),
    url(r'^cliente_ficha/(?P<id_cli>\d+)/email/nuevo',views.add_email, name = 'add_email'),
    url(r'^cliente_ficha/(?P<id_cli>\d+)/email/delete/(?P<pk>\d+)$', views.eliminarEmail, \
        name='delete_email'),
    url(r'^cliente_ficha/(?P<id_cli>\d+)/email/editar/(?P<pk>\d+)/$', views.edit_email, \
        name = 'edit_email'),
    url(r'^cliente_ficha/(?P<id_cli>\d+)/direccion/editar/(?P<pk>\d+)/$', views.direccion_cliente_edit, \
        name = 'direccion_cliente_edit'),
    url(r'^cliente_ficha/(?P<id_cli>\d+)/direccion/nuevo', views.add_direccion_sede_cliente, \
        name = 'add_direccion_sede_cliente'),
    url(r'^cliente_ficha/(?P<id_cli>\d+)/telefono/nuevo', views.add_telefono_cliente, \
        name = 'add_telefono_cliente'),
    url(r'^cliente_ficha/(?P<id_cli>\d+)/telefono/editar/(?P<pk>\d+)/$', views.edit_telefono_cliente, \
        name = 'edit_telefono_cliente'),
    url(r'^cliente_ficha/(?P<id_cli>\d+)/telefono/delete/(?P<pk>\d+)/$', views.delete_telefono_cliente, \
        name='delete_telefono_cliente'),
)
