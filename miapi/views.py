from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from venta.models import PostProduct
from .models import Juego, Ticket
from .serializers import ProductoSerializer, JuegoSerializer, TodoSerializers
from .forms import ProductoForm


class ProductoListApiView(APIView):
    """
    Vista API para listar y crear productos de la app venta.
    No requiere autenticación (público).
    Métodos disponibles: GET, POST
    """
    
    def get(self, request, *args, **kwargs):
        """
        GET: Obtiene la lista de todos los productos.
        Si es una petición HTML (navegador), muestra la vista con formulario.
        Si es una petición API (JSON), devuelve los datos en JSON.
        """
        # Detectar si es una petición HTML o API
        # Los navegadores envían 'text/html' en Accept, las APIs suelen pedir 'application/json'
        accept_header = request.META.get('HTTP_ACCEPT', '')
        
        # Si el Accept header contiene text/html y no contiene application/json explícitamente
        # o si viene sin Accept header (navegador típico)
        if not accept_header or ('text/html' in accept_header and 'application/json' not in accept_header):
            # Es una petición HTML, mostrar formulario
            return productos_html_view(request)
        
        # Es una petición API, devolver JSON
        productos = PostProduct.objects.all()
        serializer = ProductoSerializer(productos, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        """
        POST: Crea un nuevo producto.
        Si es HTML, procesa el formulario. Si es JSON, procesa la API.
        No requiere autenticación.
        """
        # Detectar si es una petición HTML o API
        content_type = request.META.get('CONTENT_TYPE', '')
        
        # Si es multipart/form-data o application/x-www-form-urlencoded, es un formulario HTML
        if 'multipart/form-data' in content_type or 'application/x-www-form-urlencoded' in content_type:
            # Es un formulario HTML
            return productos_html_view(request)
        
        # Es una petición API JSON
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            # Si no se proporciona author, usar el primer usuario disponible o None
            if 'author' not in request.data or not request.data['author']:
                from django.contrib.auth.models import User
                first_user = User.objects.first()
                if first_user:
                    serializer.save(author=first_user)
                else:
                    return Response(
                        {'error': 'No hay usuarios disponibles. Se requiere un autor.'},
                        status=status.HTTP_400_BAD_REQUEST
                    )
            else:
                serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def productos_html_view(request):
    """
    Vista HTML para mostrar formulario de productos y lista de productos existentes.
    """
    productos = PostProduct.objects.all().order_by('-created')
    
    if request.method == "POST":
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            producto = form.save()
            messages.success(
                request,
                f"¡Producto '{producto.title}' creado exitosamente!"
            )
            return redirect(reverse('api-productos'))
    else:
        form = ProductoForm()
        # Asignar el primer usuario por defecto si existe
        from django.contrib.auth.models import User
        first_user = User.objects.first()
        if first_user:
            form.fields['author'].initial = first_user.id
    
    return render(
        request,
        'miapi/productos.html',
        {
            'form': form,
            'productos': productos,
        }
    )


class JuegoListApiView(APIView):
    """
    Vista API para listar y crear juegos (código de referencia).
    """
    
    def get(self, request, *args, **kwargs):
        juegos = Juego.objects.all()
        serializer = JuegoSerializer(juegos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        serializer = JuegoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoListApiView(APIView):
    #permissions_classes=[permissions.IsAuthenticated]

    def get(self,request, *args, **kwargs):
        todos=Ticket.objects.filter(user=request.user.id)
        serializer=TodoSerializers(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
