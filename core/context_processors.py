"""
Context processor para banners dinámicos

Este módulo proporciona contexto global para todas las vistas,
incluyendo las imágenes de banner según la sección actual.

Autor: Equipo Blogfiction
Fecha: 2025
"""

from django.conf import settings
import os

def banner_context(request):
    """
    Context processor que proporciona la imagen de banner según la URL actual.
    
    Args:
        request: Objeto HttpRequest de Django
        
    Returns:
        dict: Contexto con la imagen de banner apropiada
    """
    # Obtener la ruta actual
    current_path = request.path
    
    # Mapeo de rutas a imágenes de banner (usando las imágenes del usuario)
    banner_mapping = {
        '/': 'banner1.jpg',           # Página principal
        '/noticias/': 'banner2.png',  # Noticias
        '/about/': 'banner3.webp',   # Sobre nosotros
        '/gallery/': 'banner4.jpg',  # Galería
        '/faqs/': 'banner5.jpg',     # FAQs
        '/contact/': 'banner1.jpg',  # Contacto usa banner por defecto
    }
    
    # Determinar qué imagen usar
    banner_image = banner_mapping.get(current_path, 'banner1.jpg')
    
    # Verificar si la imagen existe físicamente
    banner_path = os.path.join(settings.MEDIA_ROOT, banner_image)
    
    # Si la imagen no existe, usar un gradiente CSS en lugar de una URL que cause 404
    if not os.path.exists(banner_path):
        # Usar un gradiente CSS en lugar de una imagen que no existe
        banner_url = 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)'
    else:
        # Construir la URL completa de la imagen
        banner_url = f"{settings.MEDIA_URL}{banner_image}"
    
    return {
        'banner_image': banner_url,
        'current_section': current_path,
    }
