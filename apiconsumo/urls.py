from django.urls import path
from . import views

app_name = "apiconsumo"

urlpatterns = [
    path('productos/', views.productos_api, name='productos_api'),
]

