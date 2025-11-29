"""
=============================================================================
APP MAIL - CÓDIGO DE REFERENCIA DEL DESARROLLO
=============================================================================

Esta app contiene código de referencia utilizado durante el desarrollo
para probar el envío de emails a través de Mailtrap.

IMPORTANTE: Esta funcionalidad ya NO se utiliza en producción.
El envío de emails se realiza desde la app 'contact' a través del 
formulario de contacto que envía mensajes a Mailtrap.

Este código se mantiene como referencia para futuras implementaciones
o para entender cómo se configuró inicialmente el envío de emails.

Para el envío de emails en producción, ver:
- contact/views.py (función contact)
- catalogo1/settings.py (configuración EMAIL_*)
=============================================================================
"""

from django.core.mail import send_mail
from django.http import HttpResponse


def send_example_email(request):
    """
    Vista de prueba para enviar emails (código de referencia).
    El envío de emails se realiza desde contact/views.py
    """
    try:        
        send_mail(
            subject='Email from Django',
            message='This is an email sent from Django application.',
            from_email='example@your_mailtrap_domain',
            recipient_list=['test@example.com'],
            fail_silently=False,
        )
        
        return HttpResponse('Email sent successfully!')
    except Exception as e:
        return HttpResponse(f'Failed to send email: {str(e)}')
