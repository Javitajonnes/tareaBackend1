from django.urls import path
from .views import ProductoListApiView, JuegoListApiView, TodoListApiView, productos_html_view

urlpatterns = [
    path('api/productos/', ProductoListApiView.as_view(), name='api-productos'),
    path('api/juegos/', JuegoListApiView.as_view(), name='api-juegos'),
    path('api', TodoListApiView.as_view()),
]