# escritura/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm # AÑADIDO: Importamos el formulario de creación de usuarios de Django

# AÑADIDO: Formulario personalizado para el registro de usuarios
class CustomUserCreationForm(UserCreationForm):
    """
    Formulario de registro personalizado que hereda de UserCreationForm de Django.
    Por ahora, no añadimos campos extra directamente aquí,
    ya que los campos del perfil (bio, foto) se gestionarán en el modelo Profile.
    """
    class Meta(UserCreationForm.Meta):
        # Le decimos al formulario qué modelo usar (User) y qué campos mostrar.
        # UserCreationForm.Meta ya incluye 'username' y 'password'.
        # Puedes añadir más campos del modelo User aquí si los necesitaras en el registro.
        model = UserCreationForm.Meta.model # Esto se refiere al modelo User