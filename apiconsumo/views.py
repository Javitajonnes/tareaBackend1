import json
import urllib.request
import urllib.error
from django.shortcuts import render
from django.conf import settings


def productos_api(request):
    """
    Vista que consume la API de productos de la app venta (método GET).
    Obtiene los productos desde la API local y los muestra en la aplicación web.
    """
    # URL de la API local
    api_url = f"http://{request.get_host()}/todos/api/productos/"
    
    try:
        # Consumir la API GET usando urllib
        # Enviar header Accept: application/json para recibir JSON en lugar de HTML
        req = urllib.request.Request(api_url)
        req.add_header('Accept', 'application/json')
        
        with urllib.request.urlopen(req, timeout=5) as response:
            if response.status == 200:
                data = response.read().decode('utf-8')
                # Verificar que la respuesta no esté vacía
                if not data or data.strip() == '':
                    productos = []
                    error_message = "La API devolvió una respuesta vacía"
                else:
                    try:
                        productos = json.loads(data)
                        # Verificar que productos sea una lista
                        if not isinstance(productos, list):
                            productos = []
                            error_message = f"La API devolvió un formato inesperado: {type(productos)}"
                    except json.JSONDecodeError as json_err:
                        productos = []
                        error_message = f"Error al parsear JSON de la API: {str(json_err)}. Respuesta recibida: {data[:200]}"
            else:
                productos = []
                error_message = f"Error al obtener los productos: HTTP {response.status}"
    except urllib.error.HTTPError as e:
        productos = []
        error_message = f"Error HTTP: {e.code} - {e.reason}"
    except urllib.error.URLError as e:
        productos = []
        error_message = f"Error de conexión con la API: {str(e)}"
    except json.JSONDecodeError as json_err:
        productos = []
        error_message = f"Error al parsear JSON: {str(json_err)}"
    except Exception as e:
        productos = []
        error_message = f"Error inesperado: {str(e)}"
    
    context = {
        'productos': productos if 'productos' in locals() else [],
        'error_message': error_message if 'error_message' in locals() else None,
    }
    
    return render(request, 'apiconsumo/productos.html', context)
