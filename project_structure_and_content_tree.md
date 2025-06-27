# Contenido del Proyecto: taller escritura

**Generado el:** 2025-06-27 15:48:09

## Estructura del Proyecto

```text
taller escritura
├── .gitignore
├── Beige Ivory Watercolor Minimalist Productivity New Blog Instagram Post.png
├── Desglose de Funcionalidades de la App.txt
├── README.md
├── manage.py
├── requirements.txt
├── escritura
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_profile.py
│   │   ├── __init__.py
│   ├── templates
│   │   ├── escritura
│   │   │   ├── base.html
│   │   │   ├── confirmar_eliminar_escrito.html
│   │   │   ├── crear_editar_escrito.html
│   │   │   ├── detalle_escrito.html
│   │   │   ├── lista_escritos.html
│   │   │   ├── registro.html
├── static
│   ├── css
│   │   ├── main.css
├── taller_escritura
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── templates
│   │   ├── base.html
```

---

## Archivo: `.gitignore`

[Contenido de '.gitignore' omitido (Extensión no listada: )]

## Archivo: `Beige Ivory Watercolor Minimalist Productivity New Blog Instagram Post.png`

[Contenido de 'Beige Ivory Watercolor Minimalist Productivity New Blog Instagram Post.png' omitido (Extensión no listada: .png)]

## Archivo: `Desglose de Funcionalidades de la App.txt`

```text
Desglose de Funcionalidades de la Aplicación del Taller de Escritura
I. Autenticación y Perfiles de Usuario:
Registro y Login de Usuarios: Los participantes podrán crear una cuenta y acceder a la aplicación.
Implicación técnica: Uso del sistema de autenticación de Django (django.contrib.auth).
Perfiles de Usuario Completos:
Bio: Un campo para una breve descripción personal.
Foto de Perfil: Un campo para subir y mostrar una imagen de perfil.
Lista de Escritos del Usuario: Una vista que muestre todos los escritos publicados por un usuario específico.
Implicación técnica: Extensión del modelo User de Django (recomendado: modelo Profile con OneToOneField).
II. Gestión de Escritos:
Creación y Edición de Escritos: Los usuarios podrán crear nuevos textos y modificar los existentes.
Implicación técnica: Modelos (models.Model), vistas (views), formularios (forms).
Borradores (Drafts): Opción de guardar escritos en progreso sin publicarlos, visibles solo para el autor.
Implicación técnica: Un campo de estado (status o visibility) en el modelo Escrito.
Visibilidad de Escritos:
Público: Visible para todos los participantes.
Privado: Visible solo para el autor.
Implicación técnica: Campo de estado/visibilidad en el modelo Escrito y lógica de permisos en vistas. (La visibilidad "Solo Amigos/Grupo" se dejará para una fase posterior si se implementa un sistema de relaciones sociales).
Editor de Texto Enriquecido (Rich Text Editor): Permitir formato de texto (negritas, cursivas, etc.) en los escritos.
Implicación técnica: Integración de una librería de terceros como django-ckeditor o django-tinymce.
Etiquetas/Categorías (Tags/Categories): Para clasificar y organizar los escritos.
Implicación técnica: Uso de una librería como django-taggit o un modelo Category con ManyToManyField.
Control de Versiones (Versiones Anteriores): Posibilidad de ver y restaurar versiones previas de un escrito.
Implicación técnica: Integración de una librería como django-reversion.
Adjuntar Archivos (Opcional): Posibilidad de subir archivos (imágenes, PDFs) asociados a un escrito.
Implicación técnica: FileField o ImageField en el modelo Escrito, o un modelo Adjunto separado.
III. Interacción y Descubrimiento:
Lectura y Comentarios: Los usuarios podrán leer los escritos de otros y dejar comentarios.
Implicación técnica: Modelo Comentario, vistas para mostrar escritos y añadir comentarios, formularios para comentarios.
Funcionalidad de Búsqueda: Búsqueda de escritos por título, autor, etiquetas, palabras clave.
Implicación técnica: Consultas con el ORM de Django (Q objects, icontains); posible integración futura con soluciones de búsqueda más avanzadas.
Paginación: Manejo eficiente de grandes listados de escritos o comentarios.
Implicación técnica: Uso de la clase Paginator de Django en las vistas.
Panel de Control (Dashboard): Una página principal personalizada para cada usuario al iniciar sesión.
Sus últimos escritos: Mostrar los textos recientes del usuario.
Notificaciones: Un sistema básico de notificaciones (ej. nuevo comentario en tu escrito).
Nuevos escritos de usuarios que sigue: (Requeriría un sistema de "seguidores" - complejo, se planificará para fases futuras si se requiere).
Próximas asignaciones: (Requeriría un sistema de "Asignaciones" o "Eventos" - a definir si es una necesidad clave ahora).
Implicación técnica: Vistas basadas en clases, múltiples consultas a modelos, posiblemente un modelo Notificacion.
IV. Administración y Moderación:
Denuncia de Contenido: Los usuarios pueden reportar escritos o comentarios inapropiados.
Implicación técnica: Un modelo Reporte que se relacione con Escrito y Comentario.
Panel de Moderación: Un área para administradores/instructores para revisar y actuar sobre el contenido reportado.
Implicación técnica: Vistas y plantillas restringidas por permisos, integración con el panel de administración de Django.
Gestión de Usuarios: Herramientas para que el administrador pueda ver, editar o suspender cuentas de usuario.
Implicación técnica: Principalmente a través del panel de administración de Django; posibles vistas personalizadas para tareas específicas.
V. Aspectos de Usabilidad y Diseño:
Diseño Responsivo: La aplicación se adaptará a diferentes tamaños de pantalla (móvil, tablet, escritorio).
Implicación técnica: Principalmente CSS (media queries), posiblemente uso de un framework CSS (Bootstrap/Tailwind).
Modalidad Oscura (Dark Mode): Opción para cambiar el tema visual de la aplicación.
Implicación técnica: CSS (variables), JavaScript, y almacenamiento de preferencia (ej. en Profile o sesiones).

```

---

## Archivo: `README.md`

```markdown
# taller_escritura ✨

Una plataforma digital centralizada y colaborativa para participantes de talleres de escritura.

[![Built with Django](https://img.shields.io/badge/Built%20with-Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Built with Python](https://img.shields.io/badge/Built%20with-Python-3670A0?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Licencia MIT](https://img.shields.io/badge/Licencia-MIT-green.svg)](./LICENSE)
<!--
Puedes añadir más badges aquí a medida que el proyecto crezca, por ejemplo:
[![CI/CD](https://github.com/Alialmandoz/taller_escritura/actions/workflows/ci.yml/badge.svg)](https://github.com/Alialmandoz/taller_escritura/actions/workflows/ci.yml)
-->

## 📖 Tabla de Contenidos

- [taller\_escritura ✨](#taller_escritura-)
  - [📖 Tabla de Contenidos](#-tabla-de-contenidos)
  - [🚀 Introducción](#-introducción)
  - [✨ Características](#-características)
  - [🛠️ Instalación](#️-instalación)
    - [Prerrequisitos](#prerrequisitos)
    - [Pasos de Instalación](#pasos-de-instalación)
    - [Iniciando el Servidor de Desarrollo](#iniciando-el-servidor-de-desarrollo)

## 🚀 Introducción

**taller_escritura** es el "hogar digital" para que los participantes de un taller de escritura desarrollen, organicen y compartan sus textos, y obtengan retroalimentación constructiva de sus pares en un entorno de comunidad y apoyo.

Esta plataforma busca ser la herramienta centralizada donde los escritores pueden:
- Gestionar su proceso creativo de principio a fin.
- Beneficiarse del intercambio y la perspectiva de otros para mejorar sus habilidades.
- Sentirse parte de una comunidad activa y de apoyo.

<!--
![Captura de pantalla de la interfaz](docs/images/screenshot_lista_escritos.png)
*Captura de pantalla de la lista de escritos.*
-->
*(Reemplaza este comentario con capturas de pantalla o un GIF/video cuando los tengas para una mejor presentación visual).*

## ✨ Características

Actualmente, la aplicación cuenta con las siguientes funcionalidades:

-   **Autenticación de Usuarios:**
    -   Registro de nuevas cuentas.
    -   Inicio y cierre de sesión seguro.
-   **Perfiles de Usuario:**
    -   Cada usuario tiene un perfil asociado automáticamente para futuras extensiones (bio, foto de perfil).
-   **Gestión de Escritos:**
    -   Creación de nuevos escritos (título, contenido, estado).
    -   Edición de escritos existentes (solo por su autor).
    -   Visibilidad de escritos: `Público`, `Privado`, `Borrador`.
-   **Visualización de Contenido:**
    -   Lista de todos los escritos marcados como `Público`.
    -   Página de detalle para cada escrito (mostrando el contenido completo).
-   **Panel de Administración de Django:**
    -   Gestión completa (CRUD) de usuarios, perfiles y escritos a través de una interfaz de administración integrada.

## 🛠️ Instalación

Sigue estos pasos para poner en marcha el proyecto en tu entorno local.

### Prerrequisitos
Asegúrate de tener instalado lo siguiente:
-   **Python 3.8+** (preferiblemente la última versión estable, como Python 3.13 que estás usando).
-   **pip** (gestor de paquetes de Python, suele venir con Python).
-   **Git** (para clonar el repositorio).

### Pasos de Instalación

1.  **Clona el repositorio:**
    ```bash
    git clone https://github.com/Alialmandoz/taller_escritura.git
    cd taller_escritura
    ```

2.  **Crea y activa un entorno virtual:**
    Un entorno virtual es crucial para aislar las dependencias del proyecto.
    ```bash
    python -m venv venv
    ```
    -   **En macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```
    -   **En Windows (Command Prompt):**
        ```bash
        venv\Scripts\activate.bat
        ```
    -   **En Windows (PowerShell):**
        ```bash
        venv\Scripts\Activate.ps1
        ```

3.  **Instala las dependencias de Python:**
    Asegúrate de que tu entorno virtual esté activado.
    ```bash
    pip install -r requirements.txt
    ```
    *(Si aún no tienes `requirements.txt`, ejecútalo después de instalar Django y Pillow: `pip freeze > requirements.txt`)*

4.  **Configura los archivos de medios (opcional, para desarrollo):**
    Crea las carpetas necesarias para archivos subidos por usuarios y coloca una imagen de perfil por defecto:
    ```bash
    mkdir media
    mkdir media/profile_pics
    # Coloca una imagen 'default.jpg' dentro de 'media/profile_pics/'
    ```

5.  **Ejecuta las migraciones de la base de datos:**
    Esto creará las tablas necesarias en tu base de datos SQLite.
    ```bash
    python manage.py migrate
    ```

6.  **Crea un superusuario (administrador):**
    Necesitarás esto para acceder al panel de administración.
    ```bash
    python manage.py createsuperuser
    ```
    Sigue las indicaciones para establecer un nombre de usuario, email y contraseña.

### Iniciando el Servidor de Desarrollo

Una vez completados los pasos anteriores, puedes iniciar la aplicación:
```bash
python manage.py runserver


La aplicación estará disponible en http://127.0.0.1:8000/.

🚀 Uso
Accediendo a la Aplicación

Lista de Escritos Públicos: Abre tu navegador y ve a http://127.0.0.1:8000/escritura/.

Panel de Administración: Accede a http://127.0.0.1:8000/admin/ e inicia sesión con tu superusuario.

Flujo de Usuario Básico

Registro: Crea una nueva cuenta en http://127.0.0.1:8000/escritura/registro/.

Inicio de Sesión: Una vez registrado, puedes iniciar sesión usando el enlace "Iniciar Sesión" en la página principal o yendo a /accounts/login/.

Crear un Escrito:

Después de iniciar sesión, verás un botón "+ Crear Nuevo Escrito" en la página de lista.

Haz clic, rellena los campos (Título, Contenido, Visibilidad).

Selecciona Público si quieres que sea visible para todos.

Haz clic en "Publicar Escrito".

Ver un Escrito Detallado: Haz clic en el título de cualquier escrito en la lista para ver su contenido completo.

Editar un Escrito:

Desde la página de detalle de tus propios escritos, verás un botón "Editar".

Haz clic para modificar el título, contenido o visibilidad.

⚙️ Configuración Clave

Las principales configuraciones del proyecto se encuentran en taller_escritura/settings.py.

Variable	Descripción	Valor Actual (ejemplo)
DEBUG	Modo de depuración. True para desarrollo, False para producción.	True
LANGUAGE_CODE	Idioma predeterminado de la aplicación.	es-es
TIME_ZONE	Zona horaria de la aplicación.	America/Mexico_City
MEDIA_URL	URL pública para servir archivos subidos por usuarios.	/media/
MEDIA_ROOT	Ruta en el sistema de archivos donde se guardan los archivos de medios.	BASE_DIR / 'media'
LOGIN_REDIRECT_URL	URL a la que redirigir después de un inicio de sesión exitoso.	'escritura:lista_escritos'
LOGOUT_REDIRECT_URL	URL a la que redirigir después de un cierre de sesión exitoso.	'escritura:lista_escritos'
📦 Estructura del Proyecto
Generated text
taller escritura
├── .gitignore                      # Archivos y directorios ignorados por Git
├── manage.py                       # Utilidad de línea de comandos de Django
├── requirements.txt                # Dependencias de Python del proyecto
├── media/                          # Archivos subidos por usuarios (ej. fotos de perfil)
│   └── profile_pics/
│       └── default.jpg             # Imagen de perfil por defecto
├── escritura/                      # Aplicación principal del taller de escritura
│   ├── __init__.py
│   ├── admin.py                    # Configuración para el panel de administración
│   ├── apps.py                     # Configuración de la aplicación
│   ├── forms.py                    # Formularios personalizados (registro, escrito)
│   ├── models.py                   # Definición de los modelos de datos (Escrito, Profile)
│   ├── tests.py                    # Archivo para pruebas de la aplicación
│   ├── urls.py                     # Definición de URLs específicas de la aplicación
│   ├── views.py                    # Lógica de las vistas (lista, detalle, registro, crear, editar)
│   ├── migrations/                 # Migraciones de base de datos para los modelos
│   │   ├── 0001_initial.py
│   │   ├── 0002_profile.py
│   │   └── __init__.py
│   └── templates/                  # Directorio para plantillas HTML de la aplicación
│       └── escritura/              # Subdirectorio para evitar conflictos de nombres de plantillas
│           ├── crear_editar_escrito.html # Plantilla reutilizable para crear/editar escritos
│           ├── detalle_escrito.html      # Plantilla para el detalle de un escrito
│           ├── lista_escritos.html       # Plantilla para la lista de escritos públicos
│           └── registro.html             # Plantilla para el formulario de registro
└── taller_escritura/               # Configuración global del proyecto Django
    ├── __init__.py
    ├── asgi.py                     # Configuración para despliegue asíncrono
    ├── settings.py                 # Configuración principal del proyecto
    ├── urls.py                     # URLs globales del proyecto
    └── wsgi.py                     # Configuración para despliegue web
IGNORE_WHEN_COPYING_START
content_copy
download
Use code with caution.
Text
IGNORE_WHEN_COPYING_END
🧪 Pruebas

Actualmente, las pruebas automatizadas están en desarrollo. Puedes ejecutar las pruebas predeterminadas de Django con:

Generated bash
python manage.py test
IGNORE_WHEN_COPYING_START
content_copy
download
Use code with caution.
Bash
IGNORE_WHEN_COPYING_END
🤝 Contribución

¡Agradecemos enormemente cualquier contribución al proyecto taller_escritura! Si deseas colaborar, te invitamos a seguir estas pautas:

Reporta Errores o Sugiere Características: Abre un issue en el repositorio de GitHub.

Contribuye con Código:

Haz un fork del repositorio.

Clona tu fork localmente.

Crea una rama para tu característica o corrección (git checkout -b feature/nombre-de-tu-caracteristica o bugfix/descripcion-del-bug).

Realiza tus cambios y asegúrate de que el código sea limpio y comentado.

Haz commit de tus cambios con un mensaje claro y descriptivo (ej. feat: Implementar comentarios de usuarios o fix: Corregir error de visualización en lista de escritos).

Sube tus cambios a tu fork (git push origin feature/nombre-de-tu-caracteristica).

Abre una Pull Request desde tu rama a la rama main del repositorio original, describiendo tus cambios.

🗺️ Roadmap

Las próximas funcionalidades y mejoras planeadas para taller_escritura incluyen:

I. Autenticación y Perfiles de Usuario:

Vista de perfil de usuario completa (mostrar bio, foto, escritos del usuario).

Edición del perfil de usuario.

II. Gestión de Escritos:

Integración de un editor de texto enriquecido (ej. django-ckeditor).

Implementación de etiquetas/categorías para escritos.

Control de versiones de escritos (django-reversion).

Posibilidad de adjuntar archivos a escritos.

III. Interacción y Descubrimiento:

Comentarios en escritos (PRÓXIMO PASO).

Funcionalidad de búsqueda avanzada.

Paginación para listas largas.

Panel de control (dashboard) para cada usuario.

IV. Administración y Moderación:

Sistema de denuncia de contenido.

Panel de moderación para administradores.

V. Aspectos de Usabilidad y Diseño:

Diseño responsivo para diferentes dispositivos.

Implementación de modalidad oscura (dark mode).

❓ FAQ / Troubleshooting

Q: ¿Por qué no veo mis escritos públicos en la lista?
A: Asegúrate de que el campo Estado de tus escritos esté configurado como "Público" en el panel de administración. Recuerda que la vista lista_escritos solo muestra los públicos. Un "hard refresh" del navegador (Ctrl+Shift+R o Cmd+Shift+R) también puede ayudar.

Q: Obtengo un error NoReverseMatch con las URLs de autenticación (login, logout).
A: Verifica que la línea path('accounts/', include('django.contrib.auth.urls')), esté presente en tu archivo taller_escritura/urls.py (el urls.py principal de tu proyecto), y que hayas reiniciado el servidor de desarrollo después de ese cambio.

Q: ¿Cómo activo mi entorno virtual?
A: Si estás en la raíz de tu proyecto, usa source venv/bin/activate (macOS/Linux) o venv\Scripts\activate.bat (Windows Command Prompt) o venv\Scripts\Activate.ps1 (Windows PowerShell).

📄 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

Generated text
MIT License

Copyright (c) 2025 Iván ([Tu nombre real o alias, si deseas])

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
IGNORE_WHEN_COPYING_START
content_copy
download
Use code with caution.
Text
IGNORE_WHEN_COPYING_END
👏 Agradecimientos

A la comunidad de Django y Python por sus excelentes herramientas y documentación.

A todos los futuros contribuyentes que ayuden a mejorar este proyecto.

📞 Contacto

Iván (Alialmandoz) - tu@email.com (Opcional: reemplaza con tu email real)
Proyecto Link: https://github.com/Alialmandoz/taller_escritura
```

---

## Archivo: `manage.py`

```python
#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'taller_escritura.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

```

---

## Archivo: `requirements.txt`

```text
a s g i r e f = = 3 . 8 . 1 
 
 D j a n g o = = 5 . 2 . 3 
 
 p i l l o w = = 1 1 . 2 . 1 
 
 s q l p a r s e = = 0 . 5 . 3 
 
 t z d a t a = = 2 0 2 5 . 2 
 
 
```

---

## Archivo: `escritura/__init__.py`

```python

```

---

## Archivo: `escritura/admin.py`

```python
# escritura/admin.py

from django.contrib import admin
from .models import Escrito, Profile # AÑADIDO: Importamos nuestro modelo 'Escrito'y el "profile".
                             # Es crucial importar el modelo que deseas registrar.

# Register your models here.

# AÑADIDO: Registramos el modelo Escrito en el panel de administración de Django.
# Esto genera automáticamente una interfaz CRUD (Crear, Leer, Actualizar, Borrar)
# para tus objetos Escrito, permitiendo una gestión sencilla desde el navegador.
admin.site.register(Escrito)
admin.site.register(Profile)
```

---

## Archivo: `escritura/apps.py`

```python
from django.apps import AppConfig


class EscrituraConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'escritura'

```

---

## Archivo: `escritura/forms.py`

```python
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
```

---

## Archivo: `escritura/models.py`

```python
# escritura/models.py

from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save # AÑADIDO: Para crear el perfil automáticamente
from django.dispatch import receiver         # AÑADIDO: Para conectar la señal

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
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='BORRADOR')

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
    # OneToOneField: Establece una relación "uno a uno" con el modelo User.
    # Cada User tendrá un (y solo un) Profile asociado.
    # on_delete=models.CASCADE: Si el usuario es eliminado, su perfil también se eliminará.
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # TextField: Campo para una biografía personal (opcional, blank=True permite dejarlo vacío).
    bio = models.TextField(blank=True, null=True, verbose_name="Biografía")

    # ImageField: Campo para subir una imagen de perfil.
    # upload_to='profile_pics/': Las imágenes se guardarán en MEDIA_ROOT/profile_pics/
    # default='default.jpg': Imagen por defecto si no se sube ninguna.
    # blank=True, null=True: El campo es opcional.
    foto_perfil = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics/', blank=True, null=True, verbose_name="Foto de Perfil")

    def __str__(self):
        """
        Representación en string del objeto Profile.
        Muestra el nombre de usuario del usuario asociado al perfil.
        """
        return f"Perfil de {self.user.username}"

# AÑADIDO: Señales para crear/actualizar Profile automáticamente con User
# Las señales permiten que ciertas funciones se ejecuten cuando ocurren eventos
# específicos en otros modelos (ej. cuando se guarda un User).

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
```

---

## Archivo: `escritura/tests.py`

```python
from django.test import TestCase

# Create your tests here.

```

---

## Archivo: `escritura/urls.py`

```python
# escritura/urls.py

from django.urls import path, include
from . import views # Importamos el módulo views de nuestra propia aplicación

# Definición del nombre de la aplicación para URL namespaces
# Es una buena práctica para evitar conflictos de nombres si tienes URLs con el mismo nombre en diferentes apps.
app_name = 'escritura'

urlpatterns = [
    path('', views.lista_escritos, name='lista_escritos'),
    path('<int:pk>/', views.DetalleEscrito.as_view(), name='detalle_escrito'),
    path('registro/', views.registro_usuario, name='registro'),
    path('crear/', views.crear_escrito, name='crear_escrito'),
    path('<int:pk>/editar/', views.editar_escrito, name='editar_escrito'),
    # AÑADIDO: URL para la eliminación de escritos (con confirmación)
    path('<int:pk>/eliminar/', views.eliminar_escrito, name='eliminar_escrito'),
]
```

---

## Archivo: `escritura/views.py`

```python
# escritura/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required # Decorador para requerir autenticación

from .models import Escrito # Importamos nuestro modelo Escrito
from .forms import CustomUserCreationForm, EscritoForm # Importamos nuestros formularios
from django.http import Http404 # Para lanzar un error 404 si el usuario no es el autor
from django.contrib import messages # AÑADIDO: Para mostrar mensajes al usuario

# Vista basada en función para listar escritos públicos
def lista_escritos(request):
    """
    Esta vista recupera todos los objetos Escrito cuyo estado sea 'PUBLICO'
    y los pasa a la plantilla para su visualización.
    """
    # Consulta a la base de datos: Obtiene todos los escritos donde el estado es 'PUBLICO'.
    # .order_by('-fecha_creacion') asegura que los escritos más recientes aparezcan primero.
    escritos = Escrito.objects.filter(estado='PUBLICO').order_by('-fecha_creacion')

    # AÑADIDO PARA DEPURACIÓN: Imprime el queryset para ver qué elementos contiene.
    # Estas líneas te mostrarán en la terminal del servidor qué escritos está recuperando la consulta.
    print(f"DEBUG: Escritos públicos recuperados: {escritos}")
    print(f"DEBUG: Cantidad de escritos públicos: {escritos.count()}")
    for escrito in escritos:
        print(f"DEBUG: Escrito ID: {escrito.pk}, Título: {escrito.titulo}, Estado: {escrito.estado}, Autor: {escrito.autor.username}")


    # Diccionario de contexto: Los datos que queremos pasar a la plantilla.
    # La clave 'escritos' será el nombre de la variable en la plantilla.
    contexto = {
        'escritos': escritos
    }

    # Renderiza la plantilla 'escritura/lista_escritos.html'
    # y le pasa el diccionario 'contexto'.
    return render(request, 'escritura/lista_escritos.html', contexto)


# Vista basada en clase para mostrar el detalle de un escrito
class DetalleEscrito(DetailView):
    """
    Esta vista basada en clase (CBV) se encarga de mostrar los detalles
    de un único objeto Escrito.

    Usa DetailView de Django para simplificar la lógica de obtención de un objeto.
    """
    model = Escrito  # Le decimos a DetailView qué modelo debe usar.
    template_name = 'escritura/detalle_escrito.html' # Ruta a la plantilla para mostrar el detalle.
    context_object_name = 'escrito' # Nombre de la variable que contendrá el objeto en la plantilla.

    def get_queryset(self):
        """
        Sobrescribe get_queryset para asegurar que solo se puedan ver
        escritos que sean públicos.
        """
        # Filtra para obtener solo escritos públicos.
        # Esto añade una capa de seguridad para que los usuarios no puedan acceder
        # a escritos privados o borradores a través de la URL directa.
        return Escrito.objects.filter(estado='PUBLICO')


# Vista para el registro de nuevos usuarios
def registro_usuario(request):
    """
    Esta vista maneja la lógica para el registro de nuevos usuarios.
    - Si la solicitud es GET, muestra el formulario de registro vacío.
    - Si la solicitud es POST, procesa los datos del formulario:
        - Si es válido, crea el usuario, inicia sesión al usuario y redirige a la página principal.
        - Si no es válido, vuelve a mostrar el formulario con los errores.
    """
    if request.method == 'POST':
        # Si la solicitud es POST, el formulario ha sido enviado
        form = CustomUserCreationForm(request.POST) # Crea una instancia del formulario con los datos enviados
        if form.is_valid():
            # Si el formulario es válido, guarda el nuevo usuario
            user = form.save()
            # Opcional: Iniciar sesión al usuario automáticamente después del registro
            login(request, user)
            # Redirige al usuario a una página de éxito (ej. la lista de escritos o un dashboard)
            # Por ahora, redirigimos a la lista de escritos.
            return redirect('escritura:lista_escritos')
    else:
        # Si la solicitud es GET, muestra un formulario vacío
        form = CustomUserCreationForm()
    
    # Renderiza la plantilla con el formulario (vacío o con errores)
    return render(request, 'escritura/registro.html', {'form': form})


# Vista para crear un nuevo escrito
@login_required # Decorador: Solo usuarios autenticados pueden acceder a esta vista.
def crear_escrito(request):
    """
    Esta vista permite a un usuario autenticado crear un nuevo escrito.
    - Si la solicitud es GET, muestra un formulario EscritoForm vacío.
    - Si la solicitud es POST, procesa el formulario:
        - Si es válido, guarda el escrito, asigna el autor (el usuario actual)
          y redirige a la página de detalle del nuevo escrito.
        - Si no es válido, vuelve a mostrar el formulario con los errores.
    """
    if request.method == 'POST':
        form = EscritoForm(request.POST) # Crea una instancia del formulario con los datos enviados
        if form.is_valid():
            # No guardamos el formulario directamente todavía (commit=False)
            # porque necesitamos añadir el autor (el usuario actual) antes de guardar.
            escrito = form.save(commit=False) 
            escrito.autor = request.user # Asigna el autor del escrito al usuario actualmente logueado.
            escrito.save() # Ahora sí, guarda el objeto Escrito completo en la base de datos.
            
            # Redirige a la página de detalle del escrito recién creado.
            # Necesitamos pasar el 'pk' del escrito a la URL.
            return redirect('escritura:detalle_escrito', pk=escrito.pk)
    else:
        # Si la solicitud es GET, muestra un formulario vacío.
        form = EscritoForm()
    
    # Renderiza la plantilla con el formulario (vacío o con errores)
    return render(request, 'escritura/crear_editar_escrito.html', {'form': form, 'es_creacion': True})

# Vista para editar un escrito existente
@login_required # Solo usuarios autenticados pueden acceder.
def editar_escrito(request, pk):
    """
    Esta vista permite a un usuario autenticado editar un escrito existente.
    - pk: La clave primaria (ID) del escrito a editar.
    - Se verifica que el usuario autenticado sea el autor del escrito.
    """
    # Intentar obtener el escrito, o lanzar un 404 si no existe.
    escrito = get_object_or_404(Escrito, pk=pk)

    # VERIFICACIÓN DE PERMISOS: Asegurarse de que solo el autor pueda editar.
    # Si el usuario logueado no es el autor del escrito, levantamos un error 404
    # (por motivos de seguridad, es mejor un 404 que un 403 en algunos casos,
    # para no revelar la existencia del escrito a usuarios no autorizados).
    if request.user != escrito.autor:
        raise Http404("No tienes permiso para editar este escrito.")
        # Alternativamente, podrías redirigir:
        # from django.contrib import messages
        # messages.error(request, "No tienes permiso para editar este escrito.")
        # return redirect('escritura:detalle_escrito', pk=escrito.pk)


    if request.method == 'POST':
        # Si es POST, creamos una instancia del formulario con los datos enviados
        # y le pasamos la instancia del escrito existente para que la actualice.
        form = EscritoForm(request.POST, instance=escrito)
        if form.is_valid():
            # Guarda los cambios en el escrito. Como ya pasamos 'instance', no necesitamos commit=False.
            form.save()
            # Redirige a la página de detalle del escrito editado.
            return redirect('escritura:detalle_escrito', pk=escrito.pk)
    else:
        # Si es GET, creamos una instancia del formulario y la inicializamos
        # con los datos del escrito existente para que aparezcan pre-rellenados.
        form = EscritoForm(instance=escrito)
    
    # Renderiza la misma plantilla usada para crear, pasando el formulario y la bandera.
    # es_creacion = False le dice a la plantilla que es una operación de edición.
    return render(request, 'escritura/crear_editar_escrito.html', {'form': form, 'es_creacion': False})


# AÑADIDO: Vista para eliminar un escrito
@login_required # Solo usuarios autenticados pueden acceder.
def eliminar_escrito(request, pk):
    """
    Esta vista maneja la eliminación de un escrito.
    - Si la solicitud es GET, muestra una página de confirmación.
    - Si la solicitud es POST, procede a eliminar el escrito.
    - Se verifica que el usuario autenticado sea el autor del escrito.
    """
    escrito = get_object_or_404(Escrito, pk=pk)

    # VERIFICACIÓN DE PERMISOS: Asegurarse de que solo el autor pueda eliminar.
    if request.user != escrito.autor:
        messages.error(request, "No tienes permiso para eliminar este escrito.")
        return redirect('escritura:detalle_escrito', pk=escrito.pk)
        # O podrías lanzar un Http404 como en editar_escrito, si prefieres no dar pistas.
        # raise Http404("No tienes permiso para eliminar este escrito.")

    if request.method == 'POST':
        # Si la solicitud es POST, significa que el usuario ha confirmado la eliminación.
        escrito.delete() # ¡Elimina el objeto de la base de datos!
        messages.success(request, f"El escrito '{escrito.titulo}' ha sido eliminado exitosamente.")
        return redirect('escritura:lista_escritos') # Redirige a la lista después de eliminar.

    # Si la solicitud es GET, muestra la página de confirmación.
    return render(request, 'escritura/confirmar_eliminar_escrito.html', {'escrito': escrito})
```

---

## Archivo: `escritura/migrations/0001_initial.py`

```python
# Generated by Django 5.2.3 on 2025-06-27 01:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Escrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('contenido', models.TextField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('estado', models.CharField(choices=[('BORRADOR', 'Borrador'), ('PRIVADO', 'Privado'), ('PUBLICO', 'Público')], default='BORRADOR', max_length=10)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='escritos', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Escrito',
                'verbose_name_plural': 'Escritos',
                'ordering': ['-fecha_creacion'],
            },
        ),
    ]

```

---

## Archivo: `escritura/migrations/0002_profile.py`

```python
# Generated by Django 5.2.3 on 2025-06-27 02:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escritura', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, null=True, verbose_name='Biografía')),
                ('foto_perfil', models.ImageField(blank=True, default='profile_pics/default.jpg', null=True, upload_to='profile_pics/', verbose_name='Foto de Perfil')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

```

---

## Archivo: `escritura/migrations/__init__.py`

```python

```

---

## Archivo: `escritura/templates/escritura/base.html`

```html
{# taller_escritura/templates/base.html #}
{% load static %} {# IMPORTANT: This line loads Django's static files tags #}
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    {# Define a 'title' block that child templates can override #}
    <title>{% block title %}Taller de Escritura{% endblock %}</title>
    
    {# Link to our main CSS file, served from static files #}
    <link rel="stylesheet" href="{% static 'css/main.css' %}">
    
    {# Optional 'head_extra' block for additional CSS/JS specific to child templates #}
    {% block head_extra %}{% endblock %} 
</head>
<body>
    {# Basic navigation/auth links - common across pages #}
    <header class="main-header">
        <nav class="main-nav">
            <div class="logo">
                <a href="{% url 'escritura:lista_escritos' %}">Taller de Escritura</a>
            </div>
            <ul class="nav-links">
                {% if user.is_authenticated %}
                    <li><span class="welcome-message">Hola, {{ user.username }}!</span></li>
                    <li><a href="{% url 'logout' %}">Cerrar Sesión</a></li>
                    <li><a href="{% url 'escritura:crear_escrito' %}" class="button primary">+ Crear Nuevo Escrito</a></li>
                {% else %}
                    <li><a href="{% url 'login' %}" class="button">Iniciar Sesión</a></li>
                    <li><a href="{% url 'escritura:registro' %}" class="button secondary">Registrarse</a></li>
                {% endif %}
            </ul>
        </nav>
    </header>

    <main class="container">
        {# This is the main content block that child templates will fill #}
        {% block content %}
        {% endblock %}
    </main>

    {# Optional 'footer' block #}
    <footer class="main-footer">
        <p>&copy; 2025 Taller de Escritura. Todos los derechos reservados.</p>
    </footer>

    {# Optional 'body_extra' block for JavaScript files at the end of the body #}
    {% block body_extra %}{% endblock %}
</body>
</html>
```

---

## Archivo: `escritura/templates/escritura/confirmar_eliminar_escrito.html`

```html
{# escritura/templates/escritura/confirmar_eliminar_escrito.html #}
{% extends 'base.html' %}

{% block title %}Confirmar Eliminación{% endblock %}

{% block content %}
    <div class="confirmation-container">
        <h1 class="page-title" style="color: #dc3545;">¿Estás seguro de eliminar?</h1>
        <p>Estás a punto de eliminar el escrito **"{{ escrito.titulo }}"** de forma permanente. Esta acción no se puede deshacer.</p>
        <p>Autor: <strong>{{ escrito.autor.username }}</strong></p>

        <form method="post" style="display: flex; gap: 15px; margin-top: 30px; justify-content: center;">
            {% csrf_token %} {# ¡CRÍTICO para la seguridad! #}
            <button type="submit" class="button danger">Sí, Eliminar</button>
            <a href="{% url 'escritura:detalle_escrito' pk=escrito.pk %}" class="button secondary">No, Cancelar</a>
        </form>
    </div>

    <style>
        /* Estilos específicos para la página de confirmación */
        .confirmation-container {
            text-align: center;
            background-color: #FAF7F0;
            padding: 40px;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
            max-width: 500px;
            margin: 50px auto;
        }
        .confirmation-container p {
            font-size: 1.1em;
            margin-bottom: 25px;
            line-height: 1.6;
        }
    </style>
{% endblock %}

```

---

## Archivo: `escritura/templates/escritura/crear_editar_escrito.html`

```html
{# escritura/templates/escritura/crear_editar_escrito.html #}
{% extends 'base.html' %}

{% block title %}
    {% if es_creacion %}Crear Nuevo Escrito{% else %}Editar Escrito{% endif %}
{% endblock %}

{% block content %}
    <h1 class="page-title">{% if es_creacion %}Crear Nuevo Escrito{% else %}Editar Escrito{% endif %}</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit" class="button primary">
            {% if es_creacion %}Publicar Escrito{% else %}Guardar Cambios{% endif %}
        </button>
    </form>
    <a href="{% url 'escritura:lista_escritos' %}" class="back-link">← Volver a la lista de escritos</a>
{% endblock %}
```

---

## Archivo: `escritura/templates/escritura/detalle_escrito.html`

```html
{# escritura/templates/escritura/detalle_escrito.html #}
{% extends 'base.html' %}

{% block title %}{{ escrito.titulo }} - Detalle del Escrito{% endblock %}

{% block content %}
    <div class="header-section">
        <h1 class="page-title">{{ escrito.titulo }}</h1>
        {% if user.is_authenticated and user == escrito.autor %}
            {# MODIFICADO: Agrupamos los botones de acción para un mejor control de layout #}
            <div class="action-buttons">
                <a href="{% url 'escritura:editar_escrito' pk=escrito.pk %}" class="button warning">Editar</a>
                {# AÑADIDO: Botón para iniciar el proceso de eliminación #}
                <a href="{% url 'escritura:eliminar_escrito' pk=escrito.pk %}" class="button danger">Eliminar</a>
            </div>
        {% endif %}
    </div>

    <p class="meta-info">
        Por: {{ escrito.autor.username }} |
        Publicado el: {{ escrito.fecha_creacion|date:"d M Y H:i" }} |
        Última actualización: {{ escrito.fecha_actualizacion|date:"d M Y H:i" }}
    </p>
    <div class="content">
        <p>{{ escrito.contenido }}</p>
    </div>

    <a href="{% url 'escritura:lista_escritos' %}" class="back-link">← Volver a la lista de escritos</a>
{% endblock %}
```

---

## Archivo: `escritura/templates/escritura/lista_escritos.html`

```html
{# escritura/templates/escritura/lista_escritos.html #}
{% extends 'base.html' %} {# Extends the base template #}

{% block title %}Lista de Escritos Públicos{% endblock %} {# Sets the specific title for this page #}

{% block content %} {# This content will be inserted into the 'content' block in base.html #}
    <h1 class="page-title">Escritos Públicos del Taller</h1>

    {% if escritos %}
        <ul class="escrito-list">
            {% for escrito in escritos %}
                <li class="escrito-item">
                    <h2><a href="{% url 'escritura:detalle_escrito' pk=escrito.pk %}">{{ escrito.titulo }}</a></h2>
                    <p>{{ escrito.contenido|truncatechars:200 }}</p> 
                    <div class="escrito-meta">
                        <p>Por: {{ escrito.autor.username }}</p>
                        <p>Publicado el: {{ escrito.fecha_creacion|date:"d M Y H:i" }}</p>
                    </div>
                </li>
            {% endfor %}
        </ul>
    {% else %}
        <p>No hay escritos públicos disponibles en este momento.</p>
    {% endif %}
{% endblock %}
```

---

## Archivo: `escritura/templates/escritura/registro.html`

```html
{# escritura/templates/escritura/registro.html #}
{% extends 'base.html' %}

{% block title %}Registro de Usuario{% endblock %}

{% block content %}
    <h1 class="page-title">Registro</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit" class="button">Registrarse</button>
    </form>
    <div class="login-link">
        ¿Ya tienes una cuenta? <a href="{% url 'login' %}">Inicia sesión aquí</a>
    </div>
{% endblock %}
```

---

## Archivo: `static/css/main.css`

```css
/* static/css/main.css */

/* Base Styles */
body {
    font-family: Arial, sans-serif;
    margin: 0; /* Reset default body margin */
    background-color: #F5EFE6; /* Nuevo color de fondo principal */
    color: #333333; /* Color de texto general */
    display: flex;
    flex-direction: column; /* Para layout de pie de página pegajoso */
    min-height: 100vh; /* Asegura que el body ocupe el 100% del alto de la ventana */
}

/* Main Content Container */
.container {
    max-width: 800px; /* Límite de ancho para desktops */
    margin: 20px auto; /* Centrar y añadir margen superior/inferior */
    background-color: #FAF7F0; /* Nuevo color de fondo para el contenido/tarjetas */
    padding: 20px; /* Ajuste de padding para móviles */
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    flex-grow: 1; /* Permite que el contenedor crezca y empuje el pie de página hacia abajo */
    box-sizing: border-box; /* Asegura que padding y borde no aumenten el ancho total */
}

/* Headings */
h1, h2, h3, h4, h5, h6 {
    color: #AA775A; /* Nuevo color para encabezados */
    margin-top: 0;
    margin-bottom: 20px;
}

/* Links */
a {
    color: #6B4F4F; /* Nuevo color para enlaces */
    text-decoration: none;
}
a:hover {
    text-decoration: underline;
}

/* Buttons */
.button {
    background-color: #AA775A; /* Nuevo color de fondo para botones primarios */
    color: white;
    padding: 8px 15px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 0.9em;
    text-decoration: none;
    font-weight: bold;
    display: inline-block;
    text-align: center;
    transition: background-color 0.3s ease; /* Transición suave al pasar el ratón */
}
.button:hover {
    background-color: #8C644E; /* Nuevo color de fondo para hover */
    text-decoration: none;
}

/* Specific button variants - ajustados a la nueva paleta */
.button.primary { /* Usado para "Crear Nuevo Escrito", "Publicar Escrito", "Guardar Cambios" */
    background-color: #AA775A;
}
.button.primary:hover {
    background-color: #8C644E;
}

.button.secondary { /* Usado para "Registrarse" */
    background-color: #E8D8C9; /* Un tono más claro, complementario */
    color: #6B4F4F; /* Texto oscuro para contraste */
}
.button.secondary:hover {
    background-color: #CC9980;
}

.button.warning { /* Usado para "Editar" - ahora se alinea más a un color de acción neutral/primaria */
    background-color: #AA775A;
    color: white;
}
.button.warning:hover {
    background-color: #8C644E;
}


/* Header Styles */
.main-header {
    background-color: #CC9980; /* Nuevo color de fondo para el encabezado */
    color: white;
    padding: 15px 20px; /* Ajuste de padding para móviles */
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.main-nav {
    display: flex;
    flex-wrap: wrap; /* Permite que los elementos se envuelvan en pantallas pequeñas */
    justify-content: space-between;
    align-items: center;
    max-width: 1200px; /* Límite opcional para el ancho de la navegación */
    margin: 0 auto;
}

.logo {
    flex-basis: 100%; /* El logo ocupa todo el ancho en móviles */
    text-align: center;
    margin-bottom: 10px;
}
.logo a {
    color: white;
    font-size: 1.8em; /* Tamaño de fuente ligeramente más grande para el logo */
    font-weight: bold;
    text-decoration: none;
    display: block; /* Asegura que el enlace ocupe todo el espacio del logo */
}

.nav-links {
    list-style: none;
    margin: 0;
    padding: 0;
    display: flex;
    flex-wrap: wrap; /* Permite que los enlaces se envuelvan */
    justify-content: center; /* Centra los enlaces en móviles */
    gap: 15px; /* Espacio entre elementos de navegación */
    align-items: center;
    width: 100%; /* Ocupa todo el ancho disponible */
}

.nav-links li {
    margin: 0;
}

.nav-links a, .nav-links span {
    color: white;
    text-decoration: none;
    font-weight: bold;
    padding: 5px 0;
    white-space: nowrap; /* Evita que los textos como "Hola, usuario!" se rompan */
}

.nav-links a:hover {
    text-decoration: underline;
}

.welcome-message {
    font-weight: bold;
    margin-right: 0; /* Ya no necesitamos margen si están centrados */
    color: white;
}

/* Footer Styles */
.main-footer {
    background-color: #AA775A; /* Nuevo color para el pie de página */
    color: white;
    text-align: center;
    padding: 20px;
    margin-top: 40px; /* Margen superior para separarlo del contenido */
}

/* Form Styles (reused and adapted) */
form {
    display: flex;
    flex-direction: column;
}
p {
    margin-bottom: 15px;
}
p label {
    display: block;
    margin-bottom: 5px;
    font-weight: bold;
    color: #6B4F4F; /* Nuevo color para etiquetas de formulario */
}
input[type="text"],
input[type="password"],
input[type="email"],
select,
textarea {
    width: 100%;
    padding: 10px;
    border: 1px solid #CC9980; /* Nuevo color para borde de campos */
    border-radius: 4px;
    box-sizing: border-box;
    font-family: Arial, sans-serif;
    background-color: #FAF7F0; /* Fondo de campo, más claro */
}
textarea {
    resize: vertical;
    min-height: 150px; /* Altura mínima para el área de texto */
}
ul.errorlist {
    color: red;
    list-style-type: none;
    padding-left: 0;
    margin-top: 5px;
    font-size: 0.9em;
}
.helptext {
    font-size: 0.8em;
    color: #8C644E; /* Nuevo color para texto de ayuda */
    margin-top: 5px;
}

/* Specific Escrito List/Detail Styles */
.escrito-list {
    list-style: none;
    padding: 0;
}
.escrito-item {
    background-color: #FAF7F0; /* Fondo de item de lista */
    margin-bottom: 15px;
    padding: 15px;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
.escrito-item h2 {
    margin-top: 0;
    color: #AA775A; /* Color de título de escrito */
}
.escrito-item h2 a {
    text-decoration: none;
    color: #AA775A;
}
.escrito-item h2 a:hover {
    text-decoration: underline;
}
.escrito-item p {
    line-height: 1.6;
}
.escrito-meta {
    font-size: 0.9em;
    color: #6B4F4F; /* Color de metadata */
    margin-top: 10px;
    border-top: 1px solid #E8D8C9; /* Línea separadora suave */
    padding-top: 10px;
}

/* Escrito Detail Specific Styles */
.header-section {
    display: flex;
    flex-wrap: wrap; /* Permite que los elementos se envuelvan */
    justify-content: space-between;
    align-items: center;
    margin-bottom: 10px;
}
.header-section h1 {
    flex-grow: 1; /* Permite que el título crezca */
    margin-right: 10px; /* Espacio entre título y botón */
}
.content {
    line-height: 1.8;
    color: #444444; /* Un gris ligeramente más oscuro para el contenido principal */
    white-space: pre-wrap;
}
.back-link {
    display: block;
    margin-top: 30px;
    text-align: center;
    text-decoration: none;
    color: #6B4F4F; /* Enlace de volver */
    font-weight: bold;
}
.back-link:hover {
    text-decoration: underline;
}

<<<<<<< HEAD:static/css/main.css
/* Media Queries for Responsiveness */

/* Small devices (phones, 600px and down) - Estilos base ya son para esto */

/* Medium devices (tablets, 600px and up) */
@media (min-width: 600px) {
    .container {
        padding: 30px; /* Más padding en pantallas más grandes */
    }
    .main-header {
        padding: 15px 30px;
    }
    .logo {
        flex-basis: auto; /* El logo ya no ocupa todo el ancho */
        text-align: left;
        margin-bottom: 0;
    }
    .nav-links {
        justify-content: flex-end; /* Alinear enlaces a la derecha */
        width: auto;
    }
}

/* Large devices (desktops, 992px and up) */
@media (min-width: 992px) {
    .container {
        margin-top: 40px; /* Más margen superior en pantallas grandes */
        margin-bottom: 40px;
    }
    h1 {
        font-size: 2.5em; /* Aumentar tamaño de h1 en pantallas grandes */
    }
    .logo a {
        font-size: 2em; /* Logo más grande */
    }
}
=======
/* AÑADIDO: Estilo para botones de acción */
.action-buttons {
    display: flex;
    gap: 10px; /* Espacio entre los botones */
    margin-left: 10px; /* Separación del título si es necesario */
}

/* AÑADIDO: Estilo para botón de eliminación (danger) */
.button.danger {
    background-color: #dc3545; /* Rojo */
}
.button.danger:hover {
    background-color: #c82333; /* Rojo más oscuro al pasar el ratón */
}
>>>>>>> ca996659e6b1d8f590b998bd8609d9f77266ca7a:taller_escritura/static/css/main.css

```

---

## Archivo: `taller_escritura/__init__.py`

```python

```

---

## Archivo: `taller_escritura/asgi.py`

```python
"""
ASGI config for taller_escritura project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'taller_escritura.settings')

application = get_asgi_application()

```

---

## Archivo: `taller_escritura/settings.py`

```python
# taller_escritura/settings.py

"""
Django settings for taller_escritura project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-@e^$b!8n*5s15x_p2j9!%h^b-z53%^v^#o7*g8y-n0%k(t19h+' # ¡ADVERTENCIA! Cambia esto por una clave única y segura en producción.

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True # Durante el desarrollo, True es útil para ver errores detallados.
             # En producción, esto DEBE ser False para seguridad y rendimiento.

ALLOWED_HOSTS = [] # En desarrollo, suele estar vacío o contener '127.0.0.1', 'localhost'.
                   # En producción, aquí irán los dominios de tu sitio web (ej: ['taller-escritura.com', 'www.taller-escritura.com']).


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # AÑADIDO: Tu aplicación personalizada 'escritura'.
    # Es crucial añadirla aquí para que Django sepa que existe y la cargue.
    'escritura',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'taller_escritura.urls' # Define dónde están las URLs principales de tu proyecto.

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'taller_escritura/templates'], # MODIFICADO: Añade la ruta al directorio de plantillas globales.
        'APP_DIRS': True, # Esto le dice a Django que busque plantillas dentro de las carpetas 'templates' de cada aplicación en INSTALLED_APPS.
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'taller_escritura.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3', # La base de datos predeterminada para desarrollo (SQLite).
                                          # Fácil de usar, pero para producción se recomienda PostgreSQL o MySQL.
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

# MODIFICADO: Define el idioma predeterminado de tu aplicación.
# 'es-es' para español de España. Puedes usar 'es-mx' para México, 'es-ar' para Argentina, etc.
LANGUAGE_CODE = 'es-es'

# MODIFICADO: Define la zona horaria predeterminada de tu aplicación.
# Es crucial para manejar correctamente fechas y horas.
# Puedes encontrar una lista completa de zonas horarias aquí:
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones (columna TZ database name)
TIME_ZONE = 'America/Mexico_City'

USE_I18N = True # Habilita el sistema de internacionalización de Django.

USE_TZ = True # Habilita el soporte para zonas horarias en los datetimes.


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/' # La URL base para servir archivos estáticos.

# AÑADIDO: Where Django's staticfiles app will look for additional static files.
# This is for project-wide static files, not specific to an app.
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField' # Tipo de campo predeterminado para claves primarias automáticas.


# Configuración para archivos de medios (subidos por los usuarios)
MEDIA_URL = '/media/' # La URL base para acceder a los archivos de medios en el navegador.
MEDIA_ROOT = BASE_DIR / 'media' # La ruta absoluta en el sistema de archivos donde Django guardará los archivos.

# Puedes crear una imagen de "perfil por defecto" aquí.
# Por ejemplo: taller_escritura/media/profile_pics/default.jpg
# Asegúrate de crear el directorio 'media' en la raíz de tu proyecto.

LOGIN_REDIRECT_URL = 'escritura:lista_escritos' 

# URL a la que redirigir después de un cierre de sesión exitoso.
# También redirigimos a la lista de escritos públicos, o podrías tener una página de "gracias por visitar".
LOGOUT_REDIRECT_URL = 'escritura:lista_escritos' 
```

---

## Archivo: `taller_escritura/urls.py`

```python
from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('escritura/', include('escritura.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]

```

---

## Archivo: `taller_escritura/wsgi.py`

```python
"""
WSGI config for taller_escritura project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'taller_escritura.settings')

application = get_wsgi_application()

```

---

## Archivo: `taller_escritura/templates/base.html`

```html
{# taller_escritura/templates/base.html #}
{% load static %} {# IMPORTANT: This line loads Django's static files tags #}
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    {# AÑADIDO: Define a 'title' block that child templates can override #}
    <title>{% block title %}Taller de Escritura{% endblock %}</title>

    {# MODIFICADO: Link to our main CSS file, served from static files #}
    <link rel="stylesheet" href="{% static 'css/main.css' %}">

    {# AÑADIDO: Optional 'head_extra' block for additional CSS/JS specific to child templates #}
    {% block head_extra %}{% endblock %}
</head>
<body>
    {# AÑADIDO: Basic navigation/auth links - common across pages #}
    <header class="main-header">
        <nav class="main-nav">
            <div class="logo">
                <a href="{% url 'escritura:lista_escritos' %}">Taller de Escritura</a>
            </div>
            <ul class="nav-links">
                {% if user.is_authenticated %}
                    <li><span class="welcome-message">Hola, {{ user.username }}!</span></li>
                    <li><a href="{% url 'logout' %}">Cerrar Sesión</a></li>
                    <li><a href="{% url 'escritura:crear_escrito' %}" class="button primary">+ Crear Nuevo Escrito</a></li>
                {% else %}
                    <li><a href="{% url 'login' %}" class="button">Iniciar Sesión</a></li>
                    <li><a href="{% url 'escritura:registro' %}" class="button secondary">Registrarse</a></li>
                {% endif %}
            </ul>
        </nav>
    </header>

    <main class="container">
        {# AÑADIDO: This is the main content block that child templates will fill #}
        {% block content %}
        {% endblock %}
    </main>

    {# AÑADIDO: Optional 'footer' block #}
    <footer class="main-footer">
        <p>© 2025 Taller de Escritura. Todos los derechos reservados.</p>
    </footer>

    {# AÑADIDO: Optional 'body_extra' block for JavaScript files at the end of the body #}
    {% block body_extra %}{% endblock %}
</body>
</html>

```

---

## Lista de Archivos con Contenido Omitido

*(Binarios, errores de codificación/lectura, o errores inesperados durante el procesamiento)*

- `.gitignore (Extensión no listada)`
- `Beige Ivory Watercolor Minimalist Productivity New Blog Instagram Post.png (Extensión no listada)`

## Lista de Archivos Omitidos por Tamaño Excesivo

Ninguno.
