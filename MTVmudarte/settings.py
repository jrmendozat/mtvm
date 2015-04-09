"""
Django settings for MTVmudarte project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'hvw!k_u$w7e*fni&c(&l5vb&u=)q+j1v$rj1t%u47y88=xpi(7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# TEMPLATES Configuraciones para el comportamiento de los Templates
TEMPLATE_DEBUG = DEBUG

TEMPLATE_DIRS = (
    #os.path.join(BASE_DIR, 'MTVmudarte/templates'),
)
ADMINS = (
    ('Yohandi', 'yoha3001@gmail.com'),
)
#  JR 18/03/215 Cuando las variables no capturan el valor asignado
#  en un template se sustituye por el siguiente texto

TEMPLATE_STRING_IF_INVALID = 'Error en la captura del valor de la variable'

ALLOWED_HOSTS = [
        '*'
]   # Allow all host headers

SITE_ID = 1

# Definicion de las aplicaciones instaladas

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    #'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admindocs',
    'haystack',
    #'Llamadas',
    'Cliente',
    'Segmento',
    'Condicion_pago',
    'Tipo_cliente',
    'Sede',
    'Direccion',
    'Telefono',
    'Empresa',
    'Persona',
    'Departamento',
    'Trabajador',
    'Mueble',
    'Articulo',
    'Proveedor',
    'Vehiculo',
)

HAYSTACK_CONNECTIONS = {
    'default': {
    'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
    'URL': 'http://127.0.0.1:9200/',
    'INDEX_NAME': 'haystack',
    },
}

HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'MTVmudarte.urls'



WSGI_APPLICATION = 'MTVmudarte.wsgi.application'

TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), 'templates').replace('\\', '/'), )

# Configuracion de la base de datos local

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_Mudarte',
        'USER':'root',
        'PASSWORD': 'md123',
        'HOST': '',
        'PORT': '',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

#JR 19/03/2015 El lenguaje por defecto del sistema es "en-us"
#referido a ingles de los estados unidos
#
LANGUAGE_CODE = 'es-AR'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DEFAULT_CHARSET = 'utf-8'

FILE_CHARSET = 'utf-8'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
# ############### modificado por Yohandri ###########################<---------

#STATIC_ROOT = '/static/'
STATIC_URL = '/static/'
STATIC_ROOT = ''

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    )
# ############### fin modificacion por Yohandri ######################<--------

TEMPLATE_CONTEXT_PROCESSORS = ("django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages")
