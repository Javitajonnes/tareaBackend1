from django.contrib import admin
from .models import Juego


@admin.register(Juego)
class JuegoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio', 'stock', 'created')
    list_filter = ('categoria', 'created')
    search_fields = ('nombre', 'descripcion', 'categoria')
    ordering = ('-created',)
