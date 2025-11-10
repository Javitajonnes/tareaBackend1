from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import ContactForm


def contact(request):
    """
    Vista del formulario de contacto.
    Utiliza django-crispy-forms para renderizar el formulario con bootstrap5.
    """
    if request.method == "POST":
        form = ContactForm(data=request.POST)
        if form.is_valid():
            # En esta versión no enviamos correo: solo mostramos mensaje de éxito.
            messages.success(
                request,
                "¡Gracias por escribirnos! Te contactaremos a la brevedad.",
            )
            return redirect(reverse("contact"))
    else:
        form = ContactForm()

    return render(
        request,
        "contact/contacto.html",
        {
            "form": form,  # formulario renderizado con crispy
        },
    )