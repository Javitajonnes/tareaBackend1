"""
Configuración de URLs para la aplicación posteo

Este módulo define las rutas URL específicas de la aplicación posteo,
incluyendo la ruta principal para mostrar las noticias.

Autor: Equipo Blogfiction
Fecha: 2025
"""

from django.urls import path
from . import views

# Lista de patrones de URL para la aplicación posteo
urlpatterns = [
    # Ruta principal para mostrar noticias
    # URL: /noticias/ -> Vista: views.noticias
    # Nombre: 'noticias' (para usar en templates con {% url 'noticias' %})
    path('', views.noticias, name='noticias'),
]

