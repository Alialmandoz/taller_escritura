# escritura/models.py

from django.db import models
from django.contrib.auth import get_user_model # Importa la función para obtener el modelo de usuario activo

# AÑADIDO: Obtén el modelo de usuario actualmente activo.
# Esto es una buena práctica para referenciar al modelo de usuario de Django,
# ya que permite que en el futuro se pueda reemplazar por un modelo de usuario personalizado.
User = get_user_model()

# AÑADIDO: Definición del modelo Escrito
class Escrito(models.Model):
    # Opciones para el estado de visibilidad del escrito
    # Usamos tuplas de (valor_real_en_bd, nombre_legible_para_humanos)
    ESTADO_CHOICES = [
        ('BORRADOR', 'Borrador'),    # Visible solo para el autor
        ('PRIVADO', 'Privado'),      # Visible solo para el autor
        ('PUBLICO', 'Público'),      # Visible para todos los participantes
    ]

    # Campo ForeignKey: Establece una relación "muchos a uno" con el modelo User.
    # Un usuario puede tener muchos escritos, pero un escrito pertenece a un solo autor.
    # on_delete=models.CASCADE: Si el autor es eliminado, sus escritos también se eliminarán.
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='escritos')

    # CharField: Campo para texto corto, como títulos. max_length es obligatorio.
    titulo = models.CharField(max_length=200)

    # TextField: Campo para texto largo, ideal para el contenido del escrito.
    contenido = models.TextField()

    # DateTimeField: Guarda la fecha y hora de creación.
    # auto_now_add=True: Establece la fecha y hora actual automáticamente cuando se crea el objeto.
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    # DateTimeField: Guarda la fecha y hora de la última modificación.
    # auto_now=True: Actualiza la fecha y hora cada vez que el objeto es guardado.
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    # CharField con choices: Permite seleccionar un valor de una lista predefinida.
    # default='BORRADOR': El valor por defecto al crear un nuevo escrito.
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='BORRADOR')

    # Método __str__ (Método "string" en Python):
    # Define cómo se representa un objeto de esta clase cuando se imprime o se muestra en el admin de Django.
    # Es muy útil para la depuración y para una mejor visualización.
    def __str__(self):
        return f"{self.titulo} por {self.autor.username}"

    # Clase Meta (Opcional pero útil):
    # Aquí puedes definir opciones para el modelo que no son campos.
    class Meta:
        # Ordena los escritos por fecha de creación de forma descendente por defecto.
        ordering = ['-fecha_creacion']
        # Establece un nombre más legible para el modelo en el panel de administración
        # (singular y plural).
        verbose_name = "Escrito"
        verbose_name_plural = "Escritos"