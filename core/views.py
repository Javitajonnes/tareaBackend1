from django.shortcuts import render

def home(request):
    return render(request,"core/home.html")

def about(request):
    return render(request,"core/about.html")

def faqs(request):
    return render(request,"core/faqs.html")

def gallery(request):
    return render(request,"core/gallery.html")