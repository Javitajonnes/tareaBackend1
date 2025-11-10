"""URLs para la app redes."""

from django.urls import path

from . import views

app_name = "redes"

urlpatterns = [
    path('', views.links, name='links'),
]

