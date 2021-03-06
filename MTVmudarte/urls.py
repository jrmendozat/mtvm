"""
    # Ayuda del docstring para la documentacion
    # pendiente por elaborar
"""

from django.conf.urls import patterns, include, url
from django.contrib import admin
from MTVmudarte import views
from django.conf import settings

handler404 = views.custom_404
admin.autodiscover()

urlpatterns = patterns('',
    #(r'^static/(?P<path>.*)$',
    #    'django.views.static.serve',
    #    {'document_root': 'static'}),
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
    url(r'^sede/', include('Sede.urls', namespace="usede")),
    url(r'^mueble/', include('Mueble.urls', namespace="umueble")),
    url(r'^articulo/', include('Articulo.urls', namespace="uarticulo")),
    url(r'^proveedor/', include('Proveedor.urls', namespace="uproveedor")),
    url(r'^vehiculo/', include('Vehiculo.urls', namespace="uvehiculo")),
    url(r'^transporte/', include('Transporte.urls', namespace="utransporte")),
)

# se agrego para probar los estilo
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^static/(?P<path>.*)$',
            'django.views.static.serve',
            {'document_root' : settings.STATICFILES_DIRS}),
    )
