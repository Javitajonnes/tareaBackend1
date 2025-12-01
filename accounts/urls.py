from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.seleccionar_tipo_registro, name='seleccionar_registro'),
    path('editor/', views.registro_editor, name='registro_editor'),
    path('moderador/', views.registro_moderador, name='registro_moderador'),
    path('exitoso/', views.registro_exitoso, name='registro_exitoso'),
]



