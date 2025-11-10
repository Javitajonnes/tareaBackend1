from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Row, Column, Submit


class ContactForm(forms.Form):
    name = forms.CharField(
        label="Nombre completo",
        required=True,
        max_length=100,
    )
    email = forms.EmailField(
        label="Correo electrónico",
        required=True,
    )
    content = forms.CharField(
        label="Mensaje",
        required=True,
        widget=forms.Textarea(attrs={"rows": 5}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.form_id = "contact-form"
        self.helper.attrs = {"novalidate": True}
        # Definimos el layout usando clases de Bootstrap para mantener
        # el estilo consistente con el resto del sitio.
        self.helper.layout = Layout(
            Row(
                Column(Field("name"), css_class="col-12 col-md-6 mb-3"),
                Column(Field("email"), css_class="col-12 col-md-6 mb-3"),
            ),
            Field("content", css_class="mb-3"),
            Submit("submit", "Enviar mensaje", css_class="btn btn-primary px-4"),
        )
