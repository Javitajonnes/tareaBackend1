from django.shortcuts import render

from .models import LinkRed


def links(request):
    """Vista pública que muestra los enlaces configurados en el admin."""
    enlaces = LinkRed.objects.filter(url__isnull=False).order_by('name')
    # Reutilizamos el template genérico para listarlos de forma sencilla.
    return render(request, 'redes/lista.html', {'enlaces': enlaces})
