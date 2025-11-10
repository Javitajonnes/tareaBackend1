from django.db import models

class LinkRed(models.Model):
    key=models.SlugField(verbose_name="Nombre Clave",
                         max_length=100,unique=True)
    name=models.CharField(max_length=50,
                          verbose_name="N.Red")
    url=models.URLField(verbose_name="Enlace",
                        max_length=200,null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True, 
        verbose_name="Fecha de creación")
    updated=models.DateTimeField(auto_now=True,
                                 verbose_name="Fecha de edición")

    class Meta:
        verbose_name="enlace"
        verbose_name_plural="enlaces"

    def __str__(self):
        return self.name
