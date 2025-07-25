# escritura/forms.py

from django import forms
from django.contrib.auth import get_user_model
from .models import Profile, Escrito
from ckeditor_uploader.widgets import CKEditorUploadingWidget

User = get_user_model()

class UserUpdateForm(forms.ModelForm):
    """
    Formulario para actualizar los campos básicos del modelo User.
    """
    first_name = forms.CharField(max_length=30, required=False, label="Nombre")
    last_name = forms.CharField(max_length=150, required=False, label="Apellidos")

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class ProfileUpdateForm(forms.ModelForm):
    """
    Formulario para actualizar los campos del modelo Profile.
    """
    class Meta:
        model = Profile
        fields = ['bio', 'foto_perfil', 'mostrar_en_comunidad']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4}),
        }

class EscritoForm(forms.ModelForm):
    """
    Formulario para la creación y edición de Escritos.
    Utiliza CKEditor para el campo de contenido.
    """
    contenido = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Escrito
        fields = ['titulo', 'contenido', 'estado']
        labels = {
            'titulo': 'Título del Escrito',
            'contenido': 'Contenido',
            'estado': 'Visibilidad',
        }
        help_texts = {
            'estado': 'Elige quién puede ver tu escrito.',
        }
