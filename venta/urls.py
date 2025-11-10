"""URLs para la app venta."""

from django.urls import path

from . import views

app_name = "venta"

urlpatterns = [
    path("", views.blog, name="blog"),
    path("categoria/<int:category_id>/", views.category, name="category"),
]

