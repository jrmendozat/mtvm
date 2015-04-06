from django.conf.urls import patterns, url

from Proveedor import views

urlpatterns = patterns('',
    url(r'^$', views.lista_proveedor, name = 'lista_proveedor'),
    url(r'^nuevo',views.add_proveedor, name = 'add_proveedor'),
    url(r'^(?P<id_prov>\d+)/$', views.editar_proveedor, name = 'editar_proveedor'),
    url(r'^delete/(?P<pk>\d+)$', views.delete_proveedor, name='delete_proveedor'),

    url(r'^tipo_proveedor/(?P<id_prov>\d+)/$', views.lista_tipo_proveedor, \
        name = 'lista_tipo_proveedor'),
    url(r'^lista_tipo_proveedor/nuevo',views.add_tipoproveedor, name = 'add_tipoproveedor'),
    url(r'^lista_tipo_proveedor/(?P<id_prov>\d+)/$', views.editar_tipoproveedor, \
        name = 'editar_tipoproveedor'),
    url(r'^lista_tipo_proveedor/delete/(?P<pk>\d+)$', views.delete_tipoproveedor, \
        name='delete_tipoproveedor'),

    url(r'^telefono/(?P<id_prov>\d+)/$', views.buscar_proveedortelefono, \
        name = 'buscar_proveedortelefono'),
    url(r'^telefono/(?P<id_prov>\d+)/nuevo$', views.add_proveedor_telefono, \
        name = 'add_proveedor_telefono'),
    url(r'^telefono/(?P<id_prov>\d+)/editar/(?P<pk>\d+)/$', views.edit_telefono_proveedor, \
        name = 'edit_telefono_proveedor'),
    url(r'^telefono/(?P<id_prov>\d+)/delete/(?P<pk>\d+)$', views.delete_telefono_proveedor, \
        name='delete_telefono_proveedor'),

    url(r'^email/(?P<id_prov>\d+)/$', views.lista_email_proveedor, \
        name = 'lista_email_proveedor'),
    url(r'^email/(?P<id_prov>\d+)/nuevo',views.add_email_proveedor, \
        name = 'add_email_proveedor'),
    url(r'^email/(?P<id_prov>\d+)/editar/(?P<pk>\d+)/$', views.edit_email_proveedor, \
        name = 'edit_email_proveedor'),
    url(r'^email/(?P<id_prov>\d+)/delete/(?P<pk>\d+)$', views.delete_email_proveedor, \
        name='delete_email_proveedor'),

    url(r'^direccion/(?P<id_prov>\d+)/nuevo$', views.add_proveedor_direccion, \
        name = 'add_proveedor_direccion'),
    url(r'^direccion/(?P<id_prov>\d+)/$', views.buscar_proveedordireccion,\
     name = 'buscar_proveedordireccion'),
    url(r'^direccion/(?P<id_prov>\d+)/editar/(?P<pk>\d+)/$', views.edit_direccion_proveedor, \
        name = 'edit_direccion_proveedor'),
    url(r'^direccion/(?P<id_prov>\d+)/delete/(?P<pk>\d+)$', views.delete_direccion_proveedor,\
     name='delete_direccion_proveedor'),
)
