"""
    # Ayuda del docstring para la documentacion
    # pendiente por elaborar
"""

from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'inicio.views.pantalla_inicial', name = 'pantalla_inicial' ),
    # url(r'^blog/', include('blog.urls')),
    url(r'^telefono/', include('Telefono.urls', namespace="utelefonos")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^telefono/nuevo','Telefono.views.nuevo_telefono'),
    url(r'^telefono/cliente','Cliente.views.add_cliente_tele'),
    url(r'^cliente/', include('Cliente.urls', namespace="uclientes")),
    url(r'^segmento/', include('Segmento.urls', namespace="usegmentos")),
    url(r'^condicion_pago/', include('Condicion_pago.urls', namespace="ucondicionpago")),
    url(r'^tipo_cliente/', include('Tipo_cliente.urls', namespace="utipocliente")),
    url(r'^index/', 'inicio.views.pantalla_inicial', name = 'pantalla_inicial' ),
    url(r'^registro/', 'inicio.views.registro', name = 'registro'),
    url(r'^direccion/', include('Direccion.urls', namespace="udireciones")),
    url(r'^search/', include('haystack.urls')),

)
