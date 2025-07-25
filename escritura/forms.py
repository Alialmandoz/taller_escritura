# escritura/forms.py

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Escrito, Comentario
from ckeditor_uploader.widgets import CKEditorUploadingWidget

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    """
    Formulario para la creación de nuevos usuarios. Extiende el base
    para incluir el campo de email.
    """
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email', 'first_name', 'last_name')

class UserUpdateForm(forms.ModelForm):
    """
    Formulario para actualizar los campos básicos del modelo User.
    """
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
    """
    contenido = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Escrito
        fields = ['titulo', 'contenido', 'estado']

class ComentarioForm(forms.ModelForm):
    """
    Formulario para crear nuevos comentarios.
    """
    class Meta:
        model = Comentario
        fields = ['texto']
        widgets = {
            'texto': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Añade tu comentario...'
            }),
        }
        labels = {
            'texto': '' # Oculta la etiqueta "Texto del Comentario"
        }