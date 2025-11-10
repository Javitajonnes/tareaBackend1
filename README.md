Plantilla proyecto para evaluaciones Backend
============================================

- Ev1: listo  
- Ev2: en proceso  
- Ev3: pendiente  
- Ev4: pendiente  

## Formularios y contacto

- La app `contact` implementa el formulario de contacto utilizando **django-crispy-forms** y **crispy-bootstrap5**.
- Para que el estilo se renderice correctamente se agregaron los paquetes a `INSTALLED_APPS` y se configuraron las constantes `CRISPY_ALLOWED_TEMPLATE_PACKS` y `CRISPY_TEMPLATE_PACK` (ver `catalogo1/settings.py`).
- El formulario (`ContactForm`) define su `FormHelper` en `contact/forms.py`, lo que permite utilizar `{{ form|crispy }}` dentro del template `contact/contacto.html`.
- La vista `contact` muestra mensajes de éxito mediante el framework de mensajes de Django y redirige a la misma URL tras un POST válido.

## Enlaces a redes sociales

- La app `redes` expone el modelo `LinkRed`, donde se almacenan los enlaces a redes sociales.
- Se creó un context processor (`redes.processors.social_links`) que consulta estos enlaces y los pone a disposición de los templates a través de la variable `footer_social_links`.
- El contexto se registra en `catalogo1/settings.py` dentro del arreglo `TEMPLATES[0]['OPTIONS']['context_processors']`.
- El template base `core/templates/core/base.html` consume la variable `footer_social_links` para renderizar los enlaces dinámicamente en el footer.

## Filtros en noticias

- La vista `posteo.views.noticias` acepta parámetros por query string para filtrar los resultados:

  | Parámetro   | Descripción                                |
  |-------------|--------------------------------------------|
  | `categoria` | Slug de `Categoria` (ForeignKey)           |
  | `autor`     | Slug de `Autor` (ForeignKey)               |
  | `etiqueta`  | Slug de `Etiqueta` (ManyToMany)            |
  | `q`         | Búsqueda en título y detalle de la noticia |
  | `orden`     | Campo de ordenamiento (`-created`, etc.)   |

- El template `posteo/templates/posteo/noticias.html` renderiza un formulario que permite aplicar estos filtros.
- Se preservan los filtros al paginar gracias al parámetro `query_string` pasado desde la vista.

## Estructura de URLs por app

- `core/urls.py`: páginas estáticas (`/`, `/about/`, `/gallery/`, `/faqs/`).
- `posteo/urls.py`: noticias paginadas y filtradas (`/noticias/`).
- `contact/urls.py`: formulario de contacto con crispy (`/contact/`).
- `redes/urls.py`: listado público de enlaces sociales (`/redes/`).
- `venta/urls.py`: blog/catalogo de productos (`/venta/`, `/venta/categoria/<id>/`).

Cada archivo de rutas se incluye en `catalogo1/urls.py`, manteniendo la responsabilidad de cada app separada.

## Página 404 personalizada

- Se creó el template `core/templates/core/404.html` que extiende el layout principal y ofrece opciones para volver al inicio, noticias o contacto.
- El handler se registra en `catalogo1/urls.py` mediante `handler404 = 'core.views.error_404'`.
- La vista `error_404` vive en `core/views.py` y devuelve la respuesta con `status=404`.

## Estilos coherentes

- Las apps `posteo`, `venta` y `contact` comparten la base visual (`core/base.html`) para mantener tipografías, colores y layout consistentes.
- Se añadieron estilos específicos en `core/static/core/css/styles.css` para armonizar tarjetas, filtros y formularios.
