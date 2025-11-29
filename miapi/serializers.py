from rest_framework import serializers
from venta.models import PostProduct
from .models import Juego, Ticket
from django.conf import settings


class ProductoSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo PostProduct de la app venta.
    Utilizado por la API para GET y POST sin autorización.
    """
    author_username = serializers.CharField(source='author.username', read_only=True)
    categories_names = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()
    
    class Meta:
        model = PostProduct
        fields = [
            'id', 'title', 'detail', 'published', 'image', 
            'author', 'author_username', 'categories', 'categories_names',
            'created', 'updated'
        ]
        read_only_fields = ['id', 'author', 'created', 'updated']
    
    def get_categories_names(self, obj):
        """Retorna los nombres de las categorías"""
        return [category.name for category in obj.categories.all()]
    
    def get_image(self, obj):
        """Retorna la URL absoluta de la imagen"""
        if obj.image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.image.url)
            # Si no hay request, construir URL manualmente
            return f"{settings.MEDIA_URL}{obj.image.name}"
        return None


class JuegoSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Juego (código de referencia).
    """
    class Meta:
        model = Juego
        fields = ['id', 'nombre', 'descripcion', 'precio', 'categoria', 'stock', 'imagen', 'created', 'updated']
        read_only_fields = ['id', 'created', 'updated']


class TodoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['task', 'completed', 'user']