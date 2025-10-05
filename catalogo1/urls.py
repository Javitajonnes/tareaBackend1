"""
Configuración principal de URLs para el proyecto Blogfiction.cl

Este módulo define las rutas URL principales del proyecto, incluyendo
las rutas de las aplicaciones core y posteo, así como la configuración
para servir archivos media en modo desarrollo.

Estructura de URLs:
- / : Página principal (home)
- /gallery/ : Galería de imágenes
- /faqs/ : Preguntas frecuentes  
- /about/ : Sobre nosotros
- /noticias/ : Sección de noticias (app posteo)
- /admin/ : Panel de administración de Django

Autor: Equipo Blogfiction
Fecha: 2025
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from core import views

# Lista principal de patrones de URL del proyecto
urlpatterns = [    
    # Rutas de la aplicación core (páginas estáticas)
    path('', views.home, name='home'),                    # Página principal
    path('gallery/', views.gallery, name='gallery'),     # Galería de imágenes
    path('faqs/', views.faqs, name='faqs'),             # Preguntas frecuentes
    path('about/', views.about, name='about'),           # Sobre nosotros
    
    # Rutas de la aplicación posteo (contenido dinámico)
    # Incluye todas las URLs definidas en posteo/urls.py
    path('noticias/', include('posteo.urls')),
    
    # Panel de administración de Django
    path('admin/', admin.site.urls),
]

# Configuración para servir archivos media en modo desarrollo
# Solo se activa cuando DEBUG=True (modo desarrollo)
# En producción, los archivos media deben servirse por el servidor web
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
