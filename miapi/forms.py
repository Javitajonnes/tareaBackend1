from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Row, Column, Submit
from venta.models import PostProduct, Category
from django.contrib.auth.models import User


class ProductoForm(forms.ModelForm):
    """
    Formulario para crear productos usando el modelo PostProduct.
    Utilizado en la vista HTML de la API.
    """
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Categorías"
    )
    
    class Meta:
        model = PostProduct
        fields = ['title', 'detail', 'image', 'author', 'categories']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'detail': forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'Título',
            'detail': 'Descripción',
            'image': 'Imagen',
            'author': 'Autor',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.form_id = "producto-form"
        self.helper.form_enctype = "multipart/form-data"
        self.helper.attrs = {"novalidate": True}
        self.helper.layout = Layout(
            Field("title", css_class="mb-3"),
            Field("detail", css_class="mb-3"),
            Field("image", css_class="mb-3"),
            Field("author", css_class="mb-3"),
            Field("categories", css_class="mb-3"),
            Submit("submit", "Crear Producto", css_class="btn btn-primary px-4"),
        )

