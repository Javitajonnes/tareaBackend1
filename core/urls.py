"""URLS de la aplicación core"""

from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path("gallery/", views.gallery, name="gallery"),
    path("faqs/", views.faqs, name="faqs"),
    path("about/", views.about, name="about"),
]

