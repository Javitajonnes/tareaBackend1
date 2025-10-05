from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Noticia

def noticias(request):
    noticias_list = Noticia.objects.all().order_by('-created')
    paginator = Paginator(noticias_list, 5)  # 5 noticias por página
    page_number = request.GET.get('page')
    noticias = paginator.get_page(page_number)
    return render(request, 'posteo/noticias.html', {'noticias': noticias})
