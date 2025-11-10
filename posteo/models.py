from decimal import Decimal

from django.db import models
from django.utils.text import slugify


class Categoria(models.Model):
    nombre = models.CharField(max_length=60, unique=True, verbose_name="Nombre")
    slug = models.SlugField(max_length=80, unique=True, verbose_name="Slug")
    descripcion = models.TextField(blank=True, verbose_name="Descripción")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)


class Noticia(models.Model):
    titulo = models.CharField(max_length=100, verbose_name="Título")
    detalle = models.TextField(verbose_name="Detalle")
    imagen = models.ImageField(upload_to='noticias/', blank=True, null=True, verbose_name="Imagen")
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name="noticias",
        verbose_name="Categoría",
    )
    autor = models.ForeignKey(
        'Autor',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="noticias",
        verbose_name="Autor",
    )
    etiquetas = models.ManyToManyField(
        'Etiqueta',
        blank=True,
        related_name="noticias",
        verbose_name="Etiquetas",
    )
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


class Comentario(models.Model):
    noticia = models.ForeignKey(
        Noticia,
        on_delete=models.CASCADE,
        related_name="comentarios",
        verbose_name="Noticia",
    )
    nombre = models.CharField(max_length=80, verbose_name="Nombre")
    email = models.EmailField(verbose_name="Correo electrónico")
    contenido = models.TextField(verbose_name="Contenido")
    aprobado = models.BooleanField(default=True, verbose_name="Aprobado")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"
        ordering = ['created']

    def __str__(self):
        return f"Comentario de {self.nombre} en {self.noticia.titulo}"


class Autor(models.Model):
    nombre = models.CharField(max_length=80, unique=True, verbose_name="Nombre")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="Slug")
    email = models.EmailField(blank=True, null=True, verbose_name="Correo electrónico")
    bio = models.TextField(blank=True, verbose_name="Biografía")
    foto = models.ImageField(upload_to='autores/', blank=True, null=True, verbose_name="Foto")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)


class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50, unique=True, verbose_name="Nombre")
    slug = models.SlugField(max_length=80, unique=True, verbose_name="Slug")
    descripcion = models.TextField(blank=True, verbose_name="Descripción")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Etiqueta"
        verbose_name_plural = "Etiquetas"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)
