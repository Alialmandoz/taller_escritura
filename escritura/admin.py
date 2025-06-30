# escritura/admin.py

from django.contrib import admin
# MODIFICADO: Importamos también el modelo Comentario
from .models import Escrito, Profile, Comentario
                             # Es crucial importar el modelo que deseas registrar.

# Register your models here.

# AÑADIDO: Registramos el modelo Escrito en el panel de administración de Django.
# Esto genera automáticamente una interfaz CRUD (Crear, Leer, Actualizar, Borrar)
# para tus objetos Escrito, permitiendo una gestión sencilla desde el navegador.
admin.site.register(Escrito)
admin.site.register(Profile)
# AÑADIDO: Registramos el nuevo modelo Comentario
admin.site.register(Comentario)