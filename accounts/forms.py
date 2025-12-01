from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission
from posteo.models import Noticia, Comentario
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Row, Column


class RegistroEditorForm(UserCreationForm):
    """
    Formulario de registro para usuarios del grupo Editores.
    Crea el grupo y asigna permisos si no existen.
    """
    first_name = forms.CharField(
        label="Nombre",
        required=True,
        max_length=30,
    )
    last_name = forms.CharField(
        label="Apellido",
        required=True,
        max_length=30,
    )
    email = forms.EmailField(
        label="Correo electrónico",
        required=True,
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.form_id = "registro-editor-form"
        self.helper.attrs = {"novalidate": True}
        self.helper.layout = Layout(
            Field("username", css_class="mb-3"),
            Row(
                Column(Field("first_name"), css_class="col-12 col-md-6 mb-3"),
                Column(Field("last_name"), css_class="col-12 col-md-6 mb-3"),
            ),
            Field("email", css_class="mb-3"),
            Field("password1", css_class="mb-3"),
            Field("password2", css_class="mb-3"),
        )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        
        if commit:
            user.save()
            
            # Obtener o crear el grupo Editores
            grupo_editores, created = Group.objects.get_or_create(name='Editores')
            
            # Si el grupo fue creado, asignar permisos
            if created:
                noticia_content_type = ContentType.objects.get_for_model(Noticia)
                permisos = Permission.objects.filter(
                    content_type=noticia_content_type,
                    codename__in=['add_noticia', 'change_noticia', 'view_noticia']
                )
                grupo_editores.permissions.set(permisos)
            
            # Asignar usuario al grupo
            user.groups.add(grupo_editores)
            user.is_staff = True  # Permitir acceso al panel de Django
            user.save()
        
        return user


class RegistroModeradorForm(UserCreationForm):
    """
    Formulario de registro para usuarios del grupo Moderadores.
    Crea el grupo y asigna permisos si no existen.
    """
    first_name = forms.CharField(
        label="Nombre",
        required=True,
        max_length=30,
    )
    last_name = forms.CharField(
        label="Apellido",
        required=True,
        max_length=30,
    )
    email = forms.EmailField(
        label="Correo electrónico",
        required=True,
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.form_id = "registro-moderador-form"
        self.helper.attrs = {"novalidate": True}
        self.helper.layout = Layout(
            Field("username", css_class="mb-3"),
            Row(
                Column(Field("first_name"), css_class="col-12 col-md-6 mb-3"),
                Column(Field("last_name"), css_class="col-12 col-md-6 mb-3"),
            ),
            Field("email", css_class="mb-3"),
            Field("password1", css_class="mb-3"),
            Field("password2", css_class="mb-3"),
        )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        
        if commit:
            user.save()
            
            # Obtener o crear el grupo Moderadores
            grupo_moderadores, created = Group.objects.get_or_create(name='Moderadores')
            
            # Si el grupo fue creado, asignar permisos
            if created:
                comentario_content_type = ContentType.objects.get_for_model(Comentario)
                permisos = Permission.objects.filter(
                    content_type=comentario_content_type,
                    codename__in=['change_comentario', 'delete_comentario', 'view_comentario']
                )
                grupo_moderadores.permissions.set(permisos)
            
            # Asignar usuario al grupo
            user.groups.add(grupo_moderadores)
            user.is_staff = True  # Permitir acceso al panel de Django
            user.save()
        
        return user



