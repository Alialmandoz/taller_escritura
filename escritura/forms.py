# escritura/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Escrito # Importamos nuestro modelo Escrito


# Formulario personalizado para el registro de usuarios
class CustomUserCreationForm(UserCreationForm):
    """
    Formulario de registro personalizado que hereda de UserCreationForm de Django.
    Por ahora, no añadimos campos extra directamente aquí,
    ya que los campos del perfil (bio, foto) se gestionarán en el modelo Profile.
    """
    class Meta(UserCreationForm.Meta):
        model = UserCreationForm.Meta.model
        # Si NO quieres pedir el email en el registro, simplemente usa los campos predeterminados:
        fields = UserCreationForm.Meta.fields
        # Si SÍ quieres pedir el email en el registro, descomenta la línea de abajo:
        # fields = UserCreationForm.Meta.fields + ('email',)


# Formulario para crear y editar objetos Escrito (sin cambios)
class EscritoForm(forms.ModelForm):
    """
    Formulario basado en el modelo Escrito para crear y editar textos.
    """
    class Meta:
        model = Escrito
        fields = ['titulo', 'contenido', 'estado'] 
        labels = {
            'titulo': 'Título del Escrito',
            'contenido': 'Contenido del Texto',
            'estado': 'Visibilidad',
        }