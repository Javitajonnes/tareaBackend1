# Sistema de Banners Dinámicos - Blogfiction.cl

## Descripción
Sistema que cambia automáticamente las imágenes de banner según la sección del sitio web que el usuario está visitando.

## Estructura de Archivos
```
media/
├── banner1.jpg      # Banner para página principal (/)
├── banner2.png      # Banner para noticias (/noticias/)
├── banner3.webp     # Banner para sobre nosotros (/about/)
├── banner4.jpg      # Banner para galería (/gallery/)
└── banner5.jpg      # Banner para FAQs (/faqs/)
```

## Funcionamiento

### 1. Context Processor
- **Archivo**: `core/context_processors.py`
- **Función**: `banner_context(request)`
- **Propósito**: Detecta la URL actual y proporciona la imagen de banner correspondiente

### 2. Configuración
- **Settings**: `catalogo1/settings.py`
- **Context Processor**: Registrado en `TEMPLATES['OPTIONS']['context_processors']`

### 3. Templates
- **Posteo**: `posteo/templates/posteo/base.html`
- **Core**: `core/templates/core/base.html`
- **Variable**: `{{ banner_image }}` disponible en todos los templates

## Mapeo de URLs a Banners
```python
banner_mapping = {
    '/': 'banner1.jpg',           # Página principal
    '/noticias/': 'banner2.png',  # Noticias
    '/about/': 'banner3.webp',    # Sobre nosotros
    '/gallery/': 'banner4.jpg',  # Galería
    '/faqs/': 'banner5.jpg',      # FAQs
}
```

## Personalización

### Cambiar Imágenes
1. Reemplazar archivos en `media/`
2. Mantener nombres de archivo: banner1.jpg, banner2.png, etc.
3. Dimensiones recomendadas: 1920x600px
4. Formatos soportados: JPG, PNG, WEBP

### Agregar Nueva Sección
1. Agregar nueva imagen en `media/` (ej: banner6.jpg)
2. Actualizar `banner_mapping` en `core/context_processors.py`
3. Crear nueva URL en `catalogo1/urls.py`

## Estilos CSS

### Template Core (Grid Layout)
```css
#banner {
    background-image: url({{ banner_image }});
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    /* Overlay para legibilidad */
}
```

### Template Posteo (Bootstrap Layout)
```html
<header class="masthead" style="background-image: url({{ banner_image }})">
```

## Ventajas
- ✅ **Automático**: No requiere configuración manual por página
- ✅ **Consistente**: Mismo sistema en todos los templates
- ✅ **Escalable**: Fácil agregar nuevas secciones
- ✅ **Mantenible**: Centralizado en context processor
- ✅ **Flexible**: Permite personalización por template
- ✅ **Multi-formato**: Soporta JPG, PNG, WEBP

## Autor
Equipo Blogfiction - 2025
