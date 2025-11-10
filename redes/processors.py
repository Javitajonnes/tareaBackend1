from .models import LinkRed


def social_links(request):
    """
    Context processor que expone enlaces a redes sociales.
    Devuelve un diccionario con la lista de links para ser iterados en los templates.
    """
    links = LinkRed.objects.filter(url__isnull=False).order_by('name')
    return {
        "footer_social_links": links,
    }