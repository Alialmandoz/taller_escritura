# escritura/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Escrito, Profile # MODIFICADO: Importamos también nuestro modelo Profile


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

# AÑADIDO: Formulario para editar el perfil de usuario
class ProfileForm(forms.ModelForm):
    """
    Formulario para que los usuarios editen su propio perfil.
    """
    class Meta:
        model = Profile
        # Especificamos los campos que el usuario puede editar.
        # No incluimos el campo 'user' porque no debe ser modificable.
        fields = ['bio', 'foto_perfil', 'mostrar_en_comunidad']
        labels = {
            'bio': 'Tu Biografía',
            'foto_perfil': 'Cambiar Foto de Perfil',
            'mostrar_en_comunidad': 'Mostrar mi perfil en la página de la comunidad',
        }
        help_texts = {
            'mostrar_en_comunidad': 'Si marcas esta casilla, otros usuarios podrán ver tu nombre y foto en la página principal.',
        }
        # Opcional: Widgets para personalizar la apariencia de los campos
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Cuéntanos un poco sobre ti...'}),
        }