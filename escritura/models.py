# escritura/models.py

from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save # AÑADIDO: Para crear el perfil automáticamente
from django.dispatch import receiver         # AÑADIDO: Para conectar la señal
from ckeditor_uploader.fields import RichTextUploadingField # MODIFICADO: Importa RichTextUploadingField

# Obtén el modelo de usuario actualmente activo.
User = get_user_model()

# Definición del modelo Escrito (contenido existente)
class Escrito(models.Model):
    # Opciones para el estado de visibilidad del escrito
    ESTADO_CHOICES = [
        ('BORRADOR', 'Borrador'),
        ('PRIVADO', 'Privado'),
        ('PUBLICO', 'Público'),
    ]

    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='escritos')
    titulo = models.CharField(max_length=200)
    contenido = RichTextUploadingField() # MODIFICADO: Usa RichTextUploadingField para permitir subir archivos
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='BORRADOR')
    notificacion_enviada = models.BooleanField(default=False, verbose_name="Notificación Enviada")

    def __str__(self):
        return f"{self.titulo} por {self.autor.username}"

    class Meta:
        ordering = ['-fecha_creacion']
        verbose_name = "Escrito"
        verbose_name_plural = "Escritos"

# AÑADIDO: Definición del modelo Profile
class Profile(models.Model):
    """
    Modelo de perfil de usuario extendido.
    Tiene una relación uno a uno con el modelo User de Django.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True, verbose_name="Biografía")
    foto_perfil = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics/', blank=True, null=True, verbose_name="Foto de Perfil")

    # AÑADIDO: Campo para el control de privacidad
    mostrar_en_comunidad = models.BooleanField(
        default=False,
        verbose_name="Mostrar mi perfil en la página de la comunidad",
        help_text="Marca esta casilla si deseas que tu perfil sea visible en la página principal."
    )

    def __str__(self):
        """
        Representación en string del objeto Profile.
        Muestra el nombre de usuario del usuario asociado al perfil.
        """
        return f"Perfil de {self.user.username}"

# AÑADIDO: Señales para crear/actualizar Profile automáticamente con User
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Esta función se ejecuta CADA VEZ que un objeto User es guardado.
    Si el usuario es nuevo (created=True), se crea automáticamente un objeto Profile
    asociado a ese usuario.
    """
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    Esta función se ejecuta CADA VEZ que un objeto User es guardado.
    Asegura que el Profile asociado al usuario también se guarde.
    """
    instance.profile.save()


# AÑADIR AL FINAL DE models.py

class Comentario(models.Model):
    """
    Modelo para almacenar los comentarios de un escrito.
    """
    # Relación con el escrito: Muchos comentarios pueden pertenecer a un escrito.
    # on_delete=models.CASCADE: Si se borra un escrito, se borran todos sus comentarios.
    # related_name='comentarios': Nos permitirá acceder a los comentarios desde un objeto Escrito (ej: mi_escrito.comentarios.all()).
    escrito = models.ForeignKey(Escrito, on_delete=models.CASCADE, related_name='comentarios')

    # Relación con el autor: Muchos comentarios pueden ser de un mismo usuario.
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comentarios')

    # Contenido del comentario.
    texto = models.TextField(verbose_name="Texto del Comentario")

    # Fecha de creación. Se guarda automáticamente al crear el comentario.
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Ordena los comentarios del más antiguo al más reciente por defecto.
        ordering = ['fecha_creacion']
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"

    def __str__(self):
        # Representación en texto para el admin y la depuración.
        return f'Comentario de {self.autor.username} en "{self.escrito.titulo}"'