from django.db import models
from django.contrib.auth.models import User


class Juego(models.Model):
    """
    Modelo para representar juegos de mesa, coherente con la temática
    del proyecto Blogfiction.cl (juegos de mesa, coleccionismo, tecnología lúdica).
    Este modelo será utilizado por la API con métodos GET y POST.
    """
    nombre = models.CharField(max_length=100, verbose_name="Nombre del juego")
    descripcion = models.TextField(verbose_name="Descripción")
    precio = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        default=0.00,
        verbose_name="Precio"
    )
    categoria = models.CharField(
        max_length=50,
        verbose_name="Categoría",
        help_text="Ej: Estrategia, Cartas, Miniaturas, etc."
    )
    stock = models.IntegerField(
        default=0,
        verbose_name="Stock disponible"
    )
    imagen = models.ImageField(
        upload_to='juegos/',
        blank=True,
        null=True,
        verbose_name="Imagen del juego"
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Fecha de creación"
    )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name="Fecha de actualización"
    )

    class Meta:
        verbose_name = "Juego"
        verbose_name_plural = "Juegos"
        ordering = ['-created']

    def __str__(self):
        return self.nombre


class Ticket(models.Model):
    task=models.CharField(max_length=100)
    completed=models.BooleanField(default=False)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.task
