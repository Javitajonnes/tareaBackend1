"""
Configuración de Django para el proyecto Blogfiction.cl

Este archivo contiene todas las configuraciones necesarias para el funcionamiento
del proyecto Django, incluyendo aplicaciones instaladas, base de datos, archivos
estáticos y media, y configuraciones de seguridad.

Configuraciones principales:
- INSTALLED_APPS: Aplicaciones Django instaladas (core, posteo)
- DATABASES: Configuración de base de datos SQLite
- STATIC_URL/MEDIA_URL: URLs para archivos estáticos y media
- TEMPLATES: Configuración del motor de templates
- MIDDLEWARE: Middleware de Django para procesamiento de requests

Autor: Equipo Blogfiction
Fecha: 2025
Versión Django: 5.2.5
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-c#$^$*&o=lrij(a=^zx!*0wjm%qr0f0@$f)y-n69yc7dx1f4#('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['localhost', '127.0.0.1']


# =============================================================================
# CONFIGURACIÓN DE APLICACIONES
# =============================================================================

# Lista de aplicaciones Django instaladas en el proyecto
INSTALLED_APPS = [
    # Aplicaciones por defecto de Django
    'django.contrib.admin',        # Panel de administración
    'django.contrib.auth',         # Sistema de autenticación
    'django.contrib.contenttypes', # Framework de tipos de contenido
    'django.contrib.sessions',     # Framework de sesiones
    'django.contrib.messages',     # Framework de mensajes
    'django.contrib.staticfiles',  # Manejo de archivos estáticos
    
    # Aplicaciones personalizadas del proyecto
    'core',                        # App para páginas estáticas (home, about, etc.)
    'posteo',                      # App para contenido dinámico (noticias, réplicas)
    'contact',                     # App para formulario de contacto y soporte de
    'venta',                       # App para gestión de ventas y productos
    'redes',                       # App para gestión de enlaces a redes sociales
    
    # Librerías de terceros
    'crispy_forms',
    'crispy_bootstrap5',
]

# =============================================================================
# CONFIGURACIÓN DE MIDDLEWARE
# =============================================================================

# Lista de middleware que procesa las requests HTTP en orden
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',           # Seguridad HTTP
    'django.contrib.sessions.middleware.SessionMiddleware',     # Manejo de sesiones
    'django.middleware.common.CommonMiddleware',               # Funcionalidades comunes
    'django.middleware.csrf.CsrfViewMiddleware',              # Protección CSRF
    'django.contrib.auth.middleware.AuthenticationMiddleware', # Autenticación de usuarios
    'django.contrib.messages.middleware.MessageMiddleware',    # Manejo de mensajes
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Protección clickjacking
]

ROOT_URLCONF = 'catalogo1.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'core.context_processors.banner_context',  # Context processor para banners
                'redes.processors.social_links',  # Context processor para redes sociales
            ],
        },
    },
]

WSGI_APPLICATION = 'catalogo1.wsgi.application'


# =============================================================================
# CONFIGURACIÓN DE BASE DE DATOS
# =============================================================================

# Configuración de la base de datos SQLite
# SQLite es ideal para desarrollo y proyectos pequeños
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Motor de base de datos SQLite
        'NAME': BASE_DIR / 'db.sqlite3',        # Ruta al archivo de base de datos
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

# Configuración de idioma y zona horaria
LANGUAGE_CODE = 'es-cl'  # Español Chile
TIME_ZONE = 'America/Santiago'  # Zona horaria de Chile
USE_I18N = True  # Internacionalización habilitada
USE_TZ = True  # Usar zona horaria


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

# =============================================================================
# CONFIGURACIÓN DE ARCHIVOS ESTÁTICOS Y MEDIA
# =============================================================================

# URL base para archivos estáticos (CSS, JS, imágenes del sitio)
STATIC_URL = 'static/'

# Configuración para archivos media (subidas de usuarios como imágenes de noticias)
MEDIA_URL = '/media/'                    # URL base para acceder a archivos media
MEDIA_ROOT = BASE_DIR / 'media'          # Directorio físico donde se almacenan los archivos media

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# =============================================================================
# CONFIGURACIÓN DE CRISPY FORMS
# =============================================================================

CRISPY_ALLOWED_TEMPLATE_PACKS = ("bootstrap5",)
CRISPY_TEMPLATE_PACK = "bootstrap5"
