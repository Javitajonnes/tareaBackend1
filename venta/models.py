from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User


class Category(models.Model):
    name=models.CharField(max_length=50,
                          verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, 
        verbose_name="Fecha de creación")
    updated=models.DateTimeField(auto_now=True,
                                 verbose_name="Fecha de edición")

    class Meta:
        verbose_name="categoria"
        verbose_name_plural="categorias"

    def __str__(self):
        return self.name

class PostProduct(models.Model):
    title=models.CharField(max_length=50,verbose_name="Titulo")
    detail=models.TextField(verbose_name="Detalle")
    published=models.DateTimeField(default=now,
                                   verbose_name="Fecha Publicación")
    image=models.ImageField(upload_to="blog",null=True,
                            blank=True,verbose_name="Imagen")
    author=models.ForeignKey(User,on_delete=models.CASCADE,
                             verbose_name="Autor")
    categories=models.ManyToManyField(Category,
                                      verbose_name="Categorias")
    created = models.DateTimeField(auto_now_add=True, 
        verbose_name="Fecha de creación")
    updated=models.DateTimeField(auto_now=True,
                                 verbose_name="Fecha de edición")
    
    class Meta:
        verbose_name="PosteoProducto"
        verbose_name_plural="PosteoProductos"

    def __str__(self):
        return self.title
    
