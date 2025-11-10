from django.shortcuts import render,get_object_or_404
from .models import PostProduct,Category


def blog(request):
    post=PostProduct.objects.all()
    return render(request,"venta/blog.html",
                  {'post':post})

def category(request,category_id):
    ctg=Category.objects.get(id=category_id)
    post=PostProduct.objects.filter(categories=ctg)
    #ctg=get_object_or_404(Category,id=category_id)
    return render(request,"venta/category.html",
                  {'ctg':ctg,'post':post})


