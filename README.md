Blogfiction Backend – Documentación general
===========================================

Este proyecto es la base backend de **Blogfiction.cl**, un sitio centrado en noticias, catálogo de productos y recursos para el mundo de los juegos de mesa, el coleccionismo y la tecnología lúdica.  
Incluye autenticación de administración, formularios con estilo, filtros de datos y páginas coherentes a nivel visual.

---

## Arquitectura general

### Apps y responsabilidades
| App | Rol | URLs públicas | Comentarios |
|-----|-----|---------------|-------------|
| `core` | Layout principal y páginas estáticas (home, about, gallery, faqs) | `/`, `/about/`, `/gallery/`, `/faqs/` | Define el template base y maneja banners dinámicos. |
| `posteo` | Noticias y contenido editorial | `/noticias/` | Gestiona noticias, categorías, autores, etiquetas y comentarios. |
| `contact` | Formulario de contacto | `/contact/` | Usa django-crispy-forms + bootstrap5. |
| `redes` | Enlaces a redes sociales | `/redes/` | Modelo `LinkRed`; también alimenta el footer vía context processor. |
| `venta` | Blog / catálogo de productos | `/venta/`, `/venta/categoria/<id>/` | Muestra productos y categorías con el mismo estilo del sitio. |

Cada app expone su propio `urls.py`, incluido desde `catalogo1/urls.py`, lo que mantiene las responsabilidades separadas y facilita el mantenimiento.

### Flujo de datos
1. El usuario navega por las rutas del proyecto.  
2. Cada app atiende la solicitud a través de sus vistas (por ejemplo `posteo.views.noticias`) y prepara el contexto.  
3. El template base de `core` renderiza el layout común (banner, navbar, footer).  
4. Los context processors (`core.banner_context`, `redes.social_links`) inyectan datos globales como la imagen del banner y los links sociales.  
5. Los formularios (como el de contacto) se procesan en sus views, usando crispy-forms para el renderizado.  

---

## Modelos destacados

### Posteo
- `Categoria` → `Noticia` → `Comentario`: cadena de relaciones principal.  
- `Autor`: enlazado a `Noticia` via `ForeignKey`.  
- `Etiqueta`: relación `ManyToMany` con `Noticia`.  
Estos modelos permiten filtrar noticias por categoría, autor y etiqueta, y administrar comentarios desde el panel.

### Redes
- `LinkRed`: slug, nombre, URL, timestamps. Se consume en la vista pública y en el footer.

### Venta
- `Category` y `PostProduct`: catálogo/blog de productos relacionados con el hobby.  
`PostProduct` usa `ManyToMany` con categorías y `ForeignKey` a usuarios.

---

## Administración personalizada

En `posteo/admin.py` se personalizó el panel para `Categoria`, `Noticia`, `Comentario`, `Autor`, `Etiqueta` y `Replica`.  
Se configuraron `list_display`, `list_filter`, `search_fields`, `ordering`, `readonly_fields`, `fieldsets`, `autocomplete_fields` y `list_editable`. Esto permite a los administradores gestionar el contenido con eficiencia.

---

## Context processors

| Context processor | Ubicación | Propósito |
|-------------------|-----------|-----------|
| `core.banner_context` | `core/context_processors.py` | Selecciona la imagen de banner según la ruta actual. |
| `redes.social_links` | `redes/processors.py` | Entrega los enlaces a redes sociales para el footer y la vista pública. |

Ambos se registran en `TEMPLATES[0]['OPTIONS']['context_processors']` dentro de `catalogo1/settings.py`.

---

## Formularios

- La app `contact` utiliza **django-crispy-forms** + **crispy-bootstrap5**.  
- `ContactForm` define un `FormHelper` con layout responsive en `contact/forms.py`.  
- La vista `contact` (`contact/views.py`) gestiona el POST, muestra mensajes de éxito y redirige.  
- El template `contact/contacto.html` renderiza el formulario con `{{ form|crispy }}` y un CTA propio.

---

## Noticias y filtros

- La vista `posteo.views.noticias` admite filtros via query string:

  | Parámetro | Descripción |
  |-----------|-------------|
  | `categoria` | slug de `Categoria` |
  | `autor` | slug de `Autor` |
  | `etiqueta` | slug de `Etiqueta` |
  | `q` | búsqueda en título/detalle |
  | `orden` | ordenamiento (`-created`, `created`, `titulo`, `-titulo`) |

- El template `posteo/noticias.html` genera un formulario con selects y campo de búsqueda.  
- La paginación preserva los filtros agregando el querystring actual a los links de página.

---

## Estilos y assets

- `core/base.html` define el grid principal (banner, navbar, sidebars, footer).  
- `core/static/core/css/styles.css` contiene la paleta, tipografías y elementos compartidos.  
- Las apps `posteo`, `venta` y `contact` extienden ese layout y agregan clases propias (`.venta-card`, `.filtros-container`, etc.).  
- Archivos estáticos específicos de cada app se encuentran en `app/static/app/...`.

---

## Manejo de errores

- Plantilla custom: `core/templates/core/404.html`.  
- Vista: `core.views.error_404`.  
- Handler registrado en `catalogo1/urls.py` (`handler404 = 'core.views.error_404'`).  
- Al poner `DEBUG=False` o ejecutar tests con `override_settings(DEBUG=False)` se muestra el diseño personalizado.

---

## Rutas principales

- `/` → Home (`core`)  
- `/noticias/` → Listado filtrable de noticias (`posteo`)  
- `/contact/` → Formulario de contacto (`contact`)  
- `/redes/` → Listado de enlaces sociales (`redes`)  
- `/venta/` y `/venta/categoria/<id>/` → Blog/catalogo de productos (`venta`)  
- `/admin/` → Panel de administración (usuario `root` / `root123`)  

---

## Requisitos cumplidos

1. **Modelos relacionados**: `Categoria → Noticia → Comentario` + `Autor` y `Etiqueta`.  
2. **Admin personalizado**: panel extendido con múltiples configuraciones.  
3. **404 custom**: template, vista y handler configurados.  
4. **Filtros**: query params en noticias (categoría/autor/etiqueta/búsqueda/orden).  
5. **Context processors**: banners y enlaces sociales dinámicos.  
6. **Formulario con crispy**: app `contact`.  
7. **Apps coherentes**: cada app con responsabilidad clara.  
8. **URLs por app**: `core`, `posteo`, `contact`, `redes`, `venta` expuestas y enlazadas en el router principal.
