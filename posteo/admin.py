"""
Configuración del panel de administración para la aplicación posteo

Este módulo personaliza la interfaz del panel de administración de Django
para los modelos Noticia y Replica, mejorando la experiencia del usuario
administrador con filtros, búsquedas y organización de campos.

Características implementadas:
- Filtros por categoría y fechas
- Campos de búsqueda
- Organización de campos en secciones (fieldsets)
- Campos de solo lectura para fechas automáticas
- Ordenamiento personalizado

Autor: Equipo Blogfiction
Fecha: 2025
"""

from django.contrib import admin
from .models import Noticia, Replica


@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    """
    Configuración del admin para el modelo Noticia.
    
    Personaliza la interfaz de administración para facilitar la gestión
    de noticias con filtros, búsquedas y organización visual de campos.
    """
    
    # Campos que se muestran en la lista principal del admin
    list_display = ('titulo', 'categoria', 'created', 'updated')
    
    # Filtros laterales para facilitar la navegación
    list_filter = ('categoria', 'created', 'updated')
    
    # Campos por los que se puede buscar
    search_fields = ('titulo', 'detalle', 'categoria')
    
    # Ordenamiento por defecto (más recientes primero)
    ordering = ('-created',)
    
    # Campos que no se pueden editar (se llenan automáticamente)
    readonly_fields = ('created', 'updated')
    
    # Organización de campos en secciones para mejor UX
    fieldsets = (
        ('Información básica', {
            'fields': ('titulo', 'detalle', 'categoria')
        }),
        ('Imagen', {
            'fields': ('imagen',)
        }),
        ('Fechas', {
            'fields': ('created', 'updated'),
            'classes': ('collapse',)  # Sección colapsable para ahorrar espacio
        }),
    )


@admin.register(Replica)
class ReplicaAdmin(admin.ModelAdmin):
    """
    Configuración del admin para el modelo Replica.
    
    Personaliza la interfaz de administración para facilitar la gestión
    de réplicas con filtros, búsquedas y organización visual de campos.
    """
    
    # Campos que se muestran en la lista principal del admin
    list_display = ('name', 'numero', 'precio', 'created', 'updated')
    
    # Filtros laterales para facilitar la navegación
    list_filter = ('numero', 'created', 'updated')
    
    # Campos por los que se puede buscar
    search_fields = ('name', 'detalle')
    
    # Ordenamiento por defecto (por número ascendente)
    ordering = ('numero',)
    
    # Campos que no se pueden editar (se llenan automáticamente)
    readonly_fields = ('created', 'updated')
    
    # Organización de campos en secciones para mejor UX
    fieldsets = (
        ('Información básica', {
            'fields': ('name', 'detalle', 'numero', 'precio')
        }),
        ('Imagen', {
            'fields': ('imagen',)
        }),
        ('Fechas', {
            'fields': ('created', 'updated'),
            'classes': ('collapse',)  # Sección colapsable para ahorrar espacio
        }),
    )
