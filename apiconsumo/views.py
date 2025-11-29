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
        req = urllib.request.Request(api_url)
        req.add_header('Content-Type', 'application/json')
        
        with urllib.request.urlopen(req, timeout=5) as response:
            if response.status == 200:
                data = response.read().decode('utf-8')
                productos = json.loads(data)
            else:
                productos = []
                error_message = f"Error al obtener los productos: {response.status}"
    except urllib.error.HTTPError as e:
        productos = []
        error_message = f"Error HTTP: {e.code} - {e.reason}"
    except urllib.error.URLError as e:
        productos = []
        error_message = f"Error de conexión con la API: {str(e)}"
    except Exception as e:
        productos = []
        error_message = f"Error inesperado: {str(e)}"
    
    context = {
        'productos': productos if 'productos' in locals() else [],
        'error_message': error_message if 'error_message' in locals() else None,
    }
    
    return render(request, 'apiconsumo/productos.html', context)
