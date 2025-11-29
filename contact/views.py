import logging
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse
from django.conf import settings

from .forms import ContactForm

# Configurar logger para debugging
logger = logging.getLogger(__name__)


def contact(request):
    """
    Vista del formulario de contacto.
    Utiliza django-crispy-forms para renderizar el formulario con bootstrap5.
    Envía el mensaje a través de Mailtrap.
    """
    if request.method == "POST":
        form = ContactForm(data=request.POST)
        logger.info(f"Formulario recibido. Válido: {form.is_valid()}")
        
        if form.is_valid():
            # Obtener los datos del formulario
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']
            
            logger.info(f"Formulario válido. Preparando email para: {name} ({email})")
            
            # Preparar el asunto y mensaje del email
            subject = f'Nuevo mensaje de contacto de {name}'
            message = f'''Has recibido un nuevo mensaje de contacto desde Blogfiction.cl

Nombre: {name}
Email: {email}

Mensaje:
{content}

---
Este mensaje fue enviado desde el formulario de contacto de Blogfiction.cl'''
            
            # Email de destino (bandeja de sandbox de Mailtrap)
            # En producción, esto debería ser el email del administrador
            recipient_list = ['test@example.com']  # Mailtrap capturará este email en su sandbox
            
            try:
                logger.info(f"Intentando enviar email a través de Mailtrap...")
                logger.info(f"From: {settings.DEFAULT_FROM_EMAIL}")
                logger.info(f"To: {recipient_list}")
                logger.info(f"Subject: {subject}")
                
                # Enviar el email a través de Mailtrap
                result = send_mail(
                    subject=subject,
                    message=message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=recipient_list,
                    fail_silently=False,
                )
                
                logger.info(f"Email enviado exitosamente. Resultado: {result}")
                
                messages.success(
                    request,
                    "¡Gracias por escribirnos! Tu mensaje ha sido enviado correctamente. Te contactaremos a la brevedad.",
                )
            except Exception as e:
                # Si hay un error al enviar el email, mostrar mensaje de error
                logger.error(f"Error al enviar email: {str(e)}", exc_info=True)
                messages.error(
                    request,
                    f"Hubo un problema al enviar tu mensaje. Por favor, intenta nuevamente más tarde. Error: {str(e)}",
                )
        else:
            logger.warning(f"Formulario inválido. Errores: {form.errors}")
            # Si el formulario no es válido, mostrar los errores
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
            
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