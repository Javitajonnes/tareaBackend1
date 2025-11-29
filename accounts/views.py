from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from .forms import RegistroEditorForm, RegistroModeradorForm


def seleccionar_tipo_registro(request):
    """
    Vista para seleccionar el tipo de registro (Editor o Moderador).
    """
    return render(request, 'accounts/seleccionar_registro.html')


def registro_editor(request):
    """
    Vista para el registro de usuarios del grupo Editores.
    """
    if request.method == 'POST':
        form = RegistroEditorForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(
                request,
                f'¡Registro exitoso! El usuario {user.username} ha sido registrado como Editor y puede acceder al panel de administración.'
            )
            return redirect('accounts:registro_exitoso')
    else:
        form = RegistroEditorForm()
    
    return render(request, 'accounts/registro_editor.html', {'form': form})


def registro_moderador(request):
    """
    Vista para el registro de usuarios del grupo Moderadores.
    """
    if request.method == 'POST':
        form = RegistroModeradorForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(
                request,
                f'¡Registro exitoso! El usuario {user.username} ha sido registrado como Moderador y puede acceder al panel de administración.'
            )
            return redirect('accounts:registro_exitoso')
    else:
        form = RegistroModeradorForm()
    
    return render(request, 'accounts/registro_moderador.html', {'form': form})


def registro_exitoso(request):
    """
    Vista que muestra un mensaje de éxito después del registro.
    """
    return render(request, 'accounts/registro_exitoso.html')
