"""
Vistas de la aplicación posteo para Blogfiction.cl

Este módulo contiene las vistas que manejan la lógica de presentación
de las noticias y réplicas. Implementa paginación para mejorar la
experiencia del usuario al navegar por el contenido.

Autor: Equipo Blogfiction
Fecha: 2025
"""

from django.db.models import Q
from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Autor, Categoria, Etiqueta, Noticia


def noticias(request):
    """
    Vista que muestra la lista paginada de noticias.
    
    Esta función maneja la lógica para mostrar todas las noticias disponibles
    en el sistema, implementando paginación para mejorar el rendimiento y
    la experiencia del usuario.
    
    Proceso:
    1. Obtiene todas las noticias ordenadas por fecha de creación (más recientes primero)
    2. Configura la paginación con 5 noticias por página
    3. Obtiene el número de página desde los parámetros GET
    4. Renderiza el template con las noticias paginadas
    
    Args:
        request (HttpRequest): Objeto de petición HTTP que contiene información
                              sobre la solicitud del usuario, incluyendo parámetros GET
    
    Returns:
        HttpResponse: Respuesta HTTP que renderiza el template 'posteo/noticias.html'
                     con el contexto de noticias paginadas
    
    Context:
        noticias: Objeto Page de Django con las noticias de la página actual
                 y métodos para navegación (has_previous, has_next, etc.)
    
    Template:
        posteo/noticias.html: Template que muestra las noticias con paginación
    
    URL Pattern:
        'noticias/' -> Esta vista se accede desde la URL raíz de noticias
    """
    
    # Obtener parámetros de filtro desde query params
    categoria_slug = request.GET.get('categoria')
    autor_slug = request.GET.get('autor')
    etiqueta_slug = request.GET.get('etiqueta')
    buscar = request.GET.get('q')
    orden = request.GET.get('orden', '-created')

    # Base queryset
    noticias_list = (
        Noticia.objects.select_related('categoria', 'autor')
        .prefetch_related('etiquetas')
        .order_by(orden)
    )

    # Aplicar filtros
    if categoria_slug:
        noticias_list = noticias_list.filter(categoria__slug=categoria_slug)
    if autor_slug:
        noticias_list = noticias_list.filter(autor__slug=autor_slug)
    if etiqueta_slug:
        noticias_list = noticias_list.filter(etiquetas__slug=etiqueta_slug)
    if buscar:
        noticias_list = noticias_list.filter(
            Q(titulo__icontains=buscar) |
            Q(detalle__icontains=buscar)
        ).distinct()

    query_params = request.GET.copy()
    if 'page' in query_params:
        query_params.pop('page')
    query_string = query_params.urlencode()
    
    # Configurar paginación: 5 noticias por página
    # La paginación mejora el rendimiento al cargar solo los registros necesarios
    paginator = Paginator(noticias_list, 5)
    
    # Obtener el número de página desde los parámetros GET de la URL
    # Si no se especifica página, Django usa la página 1 por defecto
    page_number = request.GET.get('page')
    
    # Obtener la página específica solicitada
    # get_page() maneja automáticamente páginas inválidas devolviendo la última página
    noticias = paginator.get_page(page_number)
    
    filtros_contexto = {
        'categorias': Categoria.objects.all().order_by('nombre'),
        'autores': Autor.objects.all().order_by('nombre'),
        'etiquetas': Etiqueta.objects.all().order_by('nombre'),
        'filtro_categoria': categoria_slug,
        'filtro_autor': autor_slug,
        'filtro_etiqueta': etiqueta_slug,
        'filtro_buscar': buscar or '',
        'orden_actual': orden,
        'query_string': query_string,
    }

    contexto = {
        'noticias': noticias,
        **filtros_contexto
    }

    return render(request, 'posteo/noticias.html', contexto)
