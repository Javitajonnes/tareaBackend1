Blogfiction Backend – Documentación general
===========================================

Este proyecto es la base backend de **Blogfiction.cl**, un sitio centrado en noticias, catálogo de productos y recursos para el mundo de los juegos de mesa, el coleccionismo y la tecnología lúdica.  
Incluye autenticación de administración, formularios con estilo, filtros de datos y páginas coherentes a nivel visual.

---

## Instalación y configuración

### Requisitos previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Git (opcional, para clonar el repositorio)

### Instalación de dependencias

1. **Crear un entorno virtual (recomendado):**

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

2. **Instalar las dependencias del proyecto:**

**Opción A: Instalar desde requirements.txt (recomendado):**

```bash
pip install -r requirements.txt
```

**Opción B: Instalar manualmente:**

```bash
pip install django==5.2.5
pip install pillow
pip install django-crispy-forms
pip install crispy-bootstrap5
pip install djangorestframework
```

### Dependencias del proyecto

El proyecto utiliza las siguientes librerías principales:

| Librería | Versión | Propósito |
|----------|---------|-----------|
| Django | 5.2.5 | Framework web principal |
| Pillow | >=10.0.0 | Procesamiento de imágenes (requerido para ImageField) |
| django-crispy-forms | Latest | Renderizado de formularios con Bootstrap |
| crispy-bootstrap5 | Latest | Integración con Bootstrap 5 |
| djangorestframework | Latest | Framework para construir APIs REST |

**Nota:** Las versiones "Latest" se refieren a las últimas versiones estables disponibles en PyPI al momento de la instalación.

### Configuración de la base de datos

1. **Aplicar migraciones:**

```bash
python manage.py migrate
```

2. **Crear un superusuario (opcional):**

```bash
python manage.py createsuperuser
```

3. **Cargar datos iniciales (si existen fixtures):**

```bash
python manage.py loaddata fixtures/initial_data.json
```

### Configuración de Mailtrap

El proyecto utiliza **Mailtrap** para el envío de emails en desarrollo. La configuración se encuentra en `catalogo1/settings.py`.

#### Datos de configuración actuales:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'sandbox.smtp.mailtrap.io'
EMAIL_HOST_USER = '712a902e021eb5'
EMAIL_HOST_PASSWORD = '6fcb32b0a4fb55'
EMAIL_PORT = 2525
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
DEFAULT_FROM_EMAIL = 'noreply@blogfiction.cl'
```

#### Para configurar tu propia cuenta de Mailtrap:

1. **Crear una cuenta en Mailtrap:**
   - Visita [https://mailtrap.io/](https://mailtrap.io/)
   - Crea una cuenta gratuita o inicia sesión

2. **Obtener credenciales SMTP:**
   - Ve a tu cuenta de Mailtrap
   - Navega a "Email Testing" → "Inboxes" → "SMTP Settings"
   - Selecciona "Sandbox" para desarrollo
   - Copia las credenciales:
     - **Host:** `sandbox.smtp.mailtrap.io`
     - **Port:** `2525`
     - **Username:** (tu usuario de Mailtrap)
     - **Password:** (tu contraseña de Mailtrap)

3. **Actualizar configuración en `catalogo1/settings.py`:**

```python
EMAIL_HOST_USER = 'tu_usuario_mailtrap'
EMAIL_HOST_PASSWORD = 'tu_contraseña_mailtrap'
```

4. **Probar el envío de emails:**
   - Accede a `/contact/` en el navegador
   - Envía un mensaje de prueba
   - Revisa tu bandeja de sandbox en Mailtrap para ver el email recibido

**Nota de seguridad:** ⚠️ No subas las credenciales de Mailtrap a repositorios públicos. Considera usar variables de entorno o un archivo `.env` para almacenar credenciales sensibles.

### Ejecutar el servidor de desarrollo

```bash
python manage.py runserver
```

El servidor estará disponible en `http://127.0.0.1:8000/`

### Comandos útiles

```bash
# Crear migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Recolectar archivos estáticos
python manage.py collectstatic

# Verificar configuración
python manage.py check

# Acceder a la shell de Django
python manage.py shell
```

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
| `miapi` | API REST para productos | `/todos/api/productos/` | API con métodos GET y POST sin autorización que consume productos de la app `venta`. |
| `apiconsumo` | Consumo de API desde la web | `/api-consumo/productos/` | App especializada que consume la API de productos y muestra los datos en la aplicación web. |
| `accounts` | Sistema de registro de usuarios | `/accounts/` | Formularios de registro para Editores y Moderadores con asignación automática de grupos y permisos. |

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

### Miapi (API)
- La API REST consume el modelo `PostProduct` de la app `venta`.  
El modelo `PostProduct` tiene múltiples atributos (title, detail, published, image, author, categories, created, updated) y es coherente con la temática del proyecto.  
La API implementa métodos GET y POST sin autorización sobre estos productos.

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
- La vista `contact` (`contact/views.py`) gestiona el POST, envía el mensaje por email a través de **Mailtrap** y muestra mensajes de éxito/error.  
- El template `contact/contacto.html` renderiza el formulario con `{{ form|crispy }}` y un botón de envío explícito.
- **Envío de emails**: Los mensajes del formulario de contacto se envían automáticamente a través de Mailtrap y aparecen en la bandeja de sandbox del servicio. La configuración de email se encuentra en `catalogo1/settings.py`.
- **Logging**: El sistema incluye logging detallado para debugging del proceso de envío de emails.

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

## API REST

El proyecto incluye una API REST desarrollada en la app `miapi` que consume productos de la app `venta`. La API funciona localmente y no requiere autenticación.

### Endpoints disponibles

| Método | URL | Descripción |
|--------|-----|-------------|
| GET | `/todos/api/productos/` | Obtiene la lista de todos los productos |
| POST | `/todos/api/productos/` | Crea un nuevo producto |

### Modelo utilizado

La API utiliza el modelo `PostProduct` de la app `venta`, que incluye los siguientes campos:
- `id`: Identificador único
- `title`: Título del producto
- `detail`: Descripción detallada
- `published`: Fecha de publicación
- `image`: Imagen del producto (URL absoluta)
- `author`: ID del autor (usuario)
- `author_username`: Nombre de usuario del autor (campo serializado)
- `categories`: IDs de las categorías
- `categories_names`: Nombres de las categorías (campo serializado)
- `created`: Fecha de creación
- `updated`: Fecha de actualización

### Ejemplo de uso GET

```bash
# Obtener todos los productos
curl http://localhost:8000/todos/api/productos/

# O desde el navegador
http://localhost:8000/todos/api/productos/
```

**Respuesta JSON:**
```json
[
  {
    "id": 1,
    "title": "Juego de Estrategia",
    "detail": "Descripción del juego...",
    "published": "2025-01-15T10:30:00Z",
    "image": "http://localhost:8000/media/blog/imagen.jpg",
    "author": 1,
    "author_username": "root",
    "categories": [1, 2],
    "categories_names": ["Estrategia", "Cartas"],
    "created": "2025-01-15T10:30:00Z",
    "updated": "2025-01-15T10:30:00Z"
  }
]
```

### Ejemplo de uso POST

```bash
# Crear un nuevo producto
curl -X POST http://localhost:8000/todos/api/productos/ \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Nuevo Juego",
    "detail": "Descripción del nuevo juego",
    "author": 1,
    "categories": [1]
  }'
```

**Nota:** Si no se proporciona `author`, se asignará automáticamente el primer usuario disponible del sistema.

### Vista HTML con formulario

La API incluye una vista HTML que se muestra cuando se accede desde el navegador:

- **URL:** `/todos/api/productos/` (desde navegador muestra HTML, desde API devuelve JSON)
- **Vista:** `miapi.views.productos_html_view`
- **Template:** `miapi/templates/miapi/productos.html`

La vista HTML incluye:
- Formulario para crear productos usando crispy-forms
- Lista de productos existentes
- Detección automática: HTML para navegadores, JSON para peticiones API

### Consumo desde la aplicación web

La app `apiconsumo` consume la API mediante GET y muestra los productos en una vista web con estilos:

- **URL de la vista web:** `/api-consumo/productos/`
- **Vista:** `apiconsumo.views.productos_api`
- **Template:** `apiconsumo/templates/apiconsumo/productos.html`

La vista consume la API localmente usando `urllib` y renderiza los productos en cards con Bootstrap, mostrando:
- Imagen del producto
- Título y descripción
- Categorías (badges)
- Autor
- Fechas de publicación y creación

### Características de la API

- ✅ **Sin autenticación**: La API es pública y no requiere tokens ni credenciales
- ✅ **Funciona localmente**: Diseñada para desarrollo y pruebas locales
- ✅ **URLs absolutas**: Las imágenes se devuelven con URLs absolutas para facilitar su uso
- ✅ **Campos serializados**: Incluye campos adicionales como `author_username` y `categories_names` para facilitar el consumo
- ✅ **Vista HTML integrada**: Cuando se accede desde el navegador, muestra un formulario HTML para crear productos. Cuando se accede como API (con header `Accept: application/json`), devuelve JSON

---

## Manejo de errores

- Plantilla custom: `core/templates/core/404.html`.  
- Vista: `core.views.error_404`.  
- Handler registrado en `catalogo1/urls.py` (`handler404 = 'core.views.error_404'`).  
- Al poner `DEBUG=False` o ejecutar tests con `override_settings(DEBUG=False)` se muestra el diseño personalizado.

---

## Usuarios de prueba

El sistema incluye los siguientes usuarios de prueba para diferentes roles:

| Usuario | Email | Contraseña | Grupo | Staff | Acceso Admin |
|---------|-------|------------|-------|-------|--------------|
| `root` | admin@blogfiction.cl | `root123` | - | ✅ | ✅ |
| `editor1` | editor@example.com | -` | - | ✅ | ❌ |
| `editor2` | editor2@gmail.com | `root1234` | Editores | ❌ | ✅ |
| `moderador1` | moderador@example.com | - | - | ✅ | ❌ |
| `moderador2` | mod2@gmail.com | `root1234` | Moderadores | ❌ | ✅ |

**Nota:** Los usuarios pueden registrarse como Editores o Moderadores a través del sistema de registro en `/accounts/`. Los usuarios registrados automáticamente obtienen `is_staff = True` para acceder al panel de administración.

---

## Rutas principales

- `/` → Home (`core`)  
- `/noticias/` → Listado filtrable de noticias (`posteo`)  
- `/contact/` → Formulario de contacto (`contact`)  
- `/redes/` → Listado de enlaces sociales (`redes`)  
- `/venta/` y `/venta/categoria/<id>/` → Blog/catalogo de productos (`venta`)  
- `/accounts/` → Sistema de registro de usuarios (`accounts`)
  - `/accounts/` → Selección de tipo de registro (Editor o Moderador)
  - `/accounts/editor/` → Formulario de registro como Editor
  - `/accounts/moderador/` → Formulario de registro como Moderador
  - `/accounts/exitoso/` → Página de confirmación de registro
- `/todos/api/productos/` → API REST para productos - GET (listar) y POST (crear) sin autorización (`miapi`)  
La API consume el modelo `PostProduct` de la app `venta`. Cuando se accede desde el navegador muestra un formulario HTML para crear productos.  
- `/api-consumo/productos/` → Vista web que consume la API de productos (`apiconsumo`)  
- `/admin/` → Panel de administración (usuario `root` / `root123`)  

---

## Requisitos cumplidos

### Requisitos básicos del proyecto

1. ✅ **Modelos relacionados**: `Categoria → Noticia → Comentario` + `Autor` y `Etiqueta`.  
   - Ubicación: `posteo/models.py`
   - Estado: Funcionando correctamente

2. ✅ **Admin personalizado**: panel extendido con múltiples configuraciones.  
   - Ubicación: `posteo/admin.py`
   - Configuraciones: `list_display`, `list_filter`, `search_fields`, `ordering`, `readonly_fields`, `fieldsets`, `autocomplete_fields`, `list_editable`
   - Estado: Funcionando correctamente

3. ✅ **404 custom**: template, vista y handler configurados.  
   - Template: `core/templates/core/404.html`
   - Vista: `core.views.error_404`
   - Handler: `handler404 = 'core.views.error_404'` en `catalogo1/urls.py`
   - Estado: Funcionando correctamente

4. ✅ **Filtros**: query params en noticias (categoría/autor/etiqueta/búsqueda/orden).  
   - Ubicación: `posteo/views.py` (función `noticias`)
   - Parámetros: `categoria`, `autor`, `etiqueta`, `q` (búsqueda), `orden`
   - Estado: Funcionando correctamente

5. ✅ **Context processors**: banners y enlaces sociales dinámicos.  
   - `core.banner_context`: Selecciona imagen de banner según ruta
   - `redes.social_links`: Enlaces a redes sociales para footer
   - Ubicación: `catalogo1/settings.py` (TEMPLATES)
   - Estado: Funcionando correctamente

6. ✅ **Formulario con crispy**: app `contact`.  
   - Formulario: `ContactForm` en `contact/forms.py`
   - Vista: `contact.views.contact`
   - Template: `contact/templates/contact/contacto.html`
   - Estado: Funcionando correctamente

7. ✅ **Apps coherentes**: cada app con responsabilidad clara.  
   - Apps: `core`, `posteo`, `contact`, `redes`, `venta`, `miapi`, `apiconsumo`, `accounts`
   - Cada app tiene su propio `urls.py` y responsabilidad específica
   - Estado: Funcionando correctamente

8. ✅ **URLs por app**: `core`, `posteo`, `contact`, `redes`, `venta`, `miapi`, `apiconsumo`, `accounts` expuestas y enlazadas en el router principal.  
   - Ubicación: `catalogo1/urls.py`
   - Estado: Funcionando correctamente

### Requisitos de grupos y usuarios

9. ✅ **Grupos y usuarios**: sistema de registro con dos grupos (Editores y Moderadores) con diferentes permisos sobre modelos.  
   - **Grupos creados en BD:** ✅
     - "Editores" (3 permisos: `add_noticia`, `change_noticia`, `view_noticia`)
     - "Moderadores" (3 permisos: `change_comentario`, `delete_comentario`, `view_comentario`)
   - **Migración:** `posteo/migrations/0004_crear_grupos_permisos.py` ✅
   - **App `accounts`:** ✅ Agregada a `INSTALLED_APPS` y completamente funcional
   - **Formularios de registro:** ✅ Implementados y accesibles
     - `RegistroEditorForm`: Registro para usuarios del grupo Editores
     - `RegistroModeradorForm`: Registro para usuarios del grupo Moderadores
   - **Vistas:** ✅ Implementadas en `accounts/views.py`
     - `seleccionar_tipo_registro`: Selección de tipo de cuenta
     - `registro_editor`: Procesamiento de registro como Editor
     - `registro_moderador`: Procesamiento de registro como Moderador
     - `registro_exitoso`: Página de confirmación
   - **URLs:** ✅ Configuradas en `accounts/urls.py` e incluidas en `catalogo1/urls.py`
   - **Funcionalidad:**
     - Crea grupos automáticamente si no existen
     - Asigna permisos correctamente a cada grupo
     - Asigna usuarios a sus respectivos grupos
     - Permite acceso al panel de Django (`is_staff = True`)
   - **Templates:** ✅ Templates con Bootstrap y crispy-forms
   - **Estado:** ✅ Funcionando correctamente y probado

### Requisitos de comunicación

10. ✅ **Envío de emails**: el formulario de contacto envía mensajes a través de Mailtrap.  
    - **Ubicación**: `contact/views.py` (función `contact`)
    - **Configuración Mailtrap**: `catalogo1/settings.py` 
      - `EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'`
      - `EMAIL_HOST = 'sandbox.smtp.mailtrap.io'`
      - `EMAIL_PORT = 2525`
      - `EMAIL_USE_TLS = True` (requerido para Mailtrap sandbox)
      - `EMAIL_HOST_USER` y `EMAIL_HOST_PASSWORD` configurados
    - **Funcionalidad**: Al enviar el formulario desde `/contact/`, se envía un email a través de Mailtrap que aparece en la bandeja de sandbox
    - **Manejo de errores**: Si falla el envío, se muestra un mensaje de error al usuario con detalles del problema
    - **Logging**: Se registran todos los pasos del proceso de envío (validación, preparación, envío, resultado)
    - **Estado**: ✅ Funcionando correctamente y probado

### Requisitos de API

11. ✅ **API REST**: API desarrollada en `miapi` con métodos GET y POST sin autorización sobre el modelo `PostProduct` de la app `venta`.  
    - Modelo: `PostProduct` (múltiples atributos: title, detail, published, image, author, categories, created, updated)
    - Endpoint: `/todos/api/productos/`
    - Métodos: GET (listar), POST (crear)
    - Vista HTML: Cuando se accede desde navegador muestra formulario HTML para crear productos
    - Vista API: Cuando se accede como API (header `Accept: application/json`) devuelve JSON
    - Estado: Funcionando correctamente

12. ✅ **Consumo de API**: app `apiconsumo` especializada que consume la API mediante GET y muestra los productos en la aplicación web.  
    - Vista: `apiconsumo.views.productos_api`
    - Template: `apiconsumo/templates/apiconsumo/productos.html`
    - URL: `/api-consumo/productos/`
    - Estado: Funcionando correctamente
