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
from .models import Autor, Categoria, Comentario, Etiqueta, Noticia, Replica


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    """Configuración del admin para el modelo Categoría."""

    list_display = ('nombre', 'slug', 'created', 'updated')
    search_fields = ('nombre', 'descripcion')
    prepopulated_fields = {'slug': ('nombre',)}
    readonly_fields = ('created', 'updated')
    ordering = ('nombre',)
    list_filter = ('created', 'updated')


@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    """
    Configuración del admin para el modelo Noticia.
    
    Personaliza la interfaz de administración para facilitar la gestión
    de noticias con filtros, búsquedas y organización visual de campos.
    """
    
    # Campos que se muestran en la lista principal del admin
    list_display = ('titulo', 'categoria', 'autor', 'created', 'updated')
    
    # Filtros laterales para facilitar la navegación
    list_filter = ('categoria', 'autor', 'created', 'updated')
    
    # Campos por los que se puede buscar
    search_fields = ('titulo', 'detalle', 'categoria__nombre', 'autor__nombre', 'etiquetas__nombre')
    
    # Ordenamiento por defecto (más recientes primero)
    ordering = ('-created',)
    
    # Campos que no se pueden editar (se llenan automáticamente)
    readonly_fields = ('created', 'updated')
    
    # Organización de campos en secciones para mejor UX
    fieldsets = (
        ('Información básica', {
            'fields': ('titulo', 'detalle', 'categoria', 'autor', 'etiquetas')
        }),
        ('Imagen', {
            'fields': ('imagen',)
        }),
        ('Fechas', {
            'fields': ('created', 'updated'),
            'classes': ('collapse',)  # Sección colapsable para ahorrar espacio
        }),
    )


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    """Configuración del admin para el modelo Comentario."""

    list_display = ('nombre', 'noticia', 'aprobado', 'created')
    list_filter = ('aprobado', 'created', 'updated')
    search_fields = ('nombre', 'email', 'contenido', 'noticia__titulo')
    ordering = ('-created',)
    readonly_fields = ('created', 'updated')
    autocomplete_fields = ('noticia',)
    list_editable = ('aprobado',)


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    """Configuración del admin para el modelo Autor."""

    list_display = ('nombre', 'email', 'created', 'updated')
    search_fields = ('nombre', 'email', 'bio')
    readonly_fields = ('created', 'updated')
    prepopulated_fields = {'slug': ('nombre',)}
    ordering = ('nombre',)
    list_filter = ('created', 'updated')


@admin.register(Etiqueta)
class EtiquetaAdmin(admin.ModelAdmin):
    """Configuración del admin para el modelo Etiqueta."""

    list_display = ('nombre', 'slug', 'created', 'updated')
    search_fields = ('nombre', 'descripcion')
    readonly_fields = ('created', 'updated')
    prepopulated_fields = {'slug': ('nombre',)}
    ordering = ('nombre',)
    list_filter = ('created', 'updated')


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
