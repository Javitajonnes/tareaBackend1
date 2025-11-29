from django.db import migrations
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType


def crear_grupos(apps, schema_editor):
    # Obtener los modelos
    noticia_content_type = ContentType.objects.get_for_model(apps.get_model('posteo', 'Noticia'))
    
    # Crear grupo de Editores
    editores, created = Group.objects.get_or_create(name='Editores')
    permisos_editores = Permission.objects.filter(
        content_type=noticia_content_type,
        codename__in=['add_noticia', 'change_noticia', 'view_noticia']
    )
    editores.permissions.set(permisos_editores)
    
    # Crear grupo de Moderadores
    moderadores, created = Group.objects.get_or_create(name='Moderadores')
    comentario_content_type = ContentType.objects.get_for_model(apps.get_model('posteo', 'Comentario'))
    permisos_moderadores = Permission.objects.filter(
        content_type=comentario_content_type,
        codename__in=['change_comentario', 'delete_comentario', 'view_comentario']
    )
    moderadores.permissions.set(permisos_moderadores)


def revertir_grupos(apps, schema_editor):
    Group.objects.filter(name__in=['Editores', 'Moderadores']).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('posteo', '0001_initial'),  # Ajusta según tu última migración
    ]

    operations = [
        migrations.RunPython(crear_grupos, revertir_grupos),
    ]