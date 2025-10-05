from django.db import models
from django.utils import timezone
from decimal import Decimal

class Noticia(models.Model):
    titulo = models.CharField(max_length=100, verbose_name="Título")
    detalle = models.TextField(verbose_name="Detalle")
    imagen = models.ImageField(upload_to='noticias/', blank=True, null=True, verbose_name="Imagen")
    categoria = models.CharField(max_length=50, default="General", verbose_name="Categoría")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Noticia"
        verbose_name_plural = "Noticias"
        ordering = ['-created']

    def __str__(self):
        return self.titulo
    
class Replica(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre")
    detalle = models.TextField(verbose_name="Detalle")
    numero = models.SmallIntegerField(verbose_name="Número")
    imagen = models.ImageField(upload_to='replicas/', blank=True, null=True, verbose_name="Imagen")
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'), verbose_name="Precio")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Réplica"
        verbose_name_plural = "Réplicas"
        ordering = ['numero']

    def __str__(self):
        return self.name
