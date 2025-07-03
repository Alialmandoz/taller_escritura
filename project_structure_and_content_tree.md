# Contenido del Proyecto: taller escritura

**Generado el:** 2025-06-30 00:41:04

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
│   │   ├── 0003_alter_escrito_contenido.py
│   │   ├── 0004_profile_mostrar_en_comunidad.py
│   │   ├── __init__.py
│   ├── templates
│   │   ├── escritura
│   │   │   ├── confirmar_eliminar_escrito.html
│   │   │   ├── crear_editar_escrito.html
│   │   │   ├── detalle_escrito.html
│   │   │   ├── editar_perfil.html
│   │   │   ├── home.html
│   │   │   ├── lista_escritos.html
│   │   │   ├── perfil_usuario.html
│   │   │   ├── registro.html
├── static
│   ├── css
│   │   ├── main.css
│   ├── js
│   │   ├── Main.js
├── taller_escritura
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── templates
│   │   ├── base.html
│   │   ├── registration
│   │   │   ├── login.html
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

## 🚀 Introducción

**taller_escritura** es el "hogar digital" para que los participantes de un taller de escritura desarrollen, organicen y compartan sus textos, y obtengan retroalimentación constructiva de sus pares en un entorno de comunidad y apoyo.

Esta plataforma busca ser la herramienta centralizada donde los escritores pueden gestionar su proceso creativo, beneficiarse del intercambio de ideas y sentirse parte de una comunidad activa.

## ✨ Características

La plataforma cuenta actualmente con las siguientes funcionalidades:

*   **Autenticación y Perfiles:**
    *   Registro, inicio y cierre de sesión de usuarios.
    *   Modelo `Profile` preparado para futuras ampliaciones (bio, foto).
    *   Página de perfil de usuario que muestra sus datos y una lista de todos sus escritos.

*   **Gestión Completa de Escritos (CRUD):**
    *   Creación de nuevos textos con un editor de texto enriquecido (CKEditor).
    *   Edición de escritos existentes (restringido al autor).
    *   Eliminación de escritos (restringido al autor, con página de confirmación).
    *   Control de visibilidad (`Público`, `Privado`, `Borrador`).

*   **Mejoras de UI/UX:**
    *   Paleta de colores y tipografías consistentes para una estética cuidada.
    *   Diseño responsivo base para una correcta visualización en móviles y escritorio.
    *   Sistema de mensajes para dar feedback al usuario (ej. "Escrito creado con éxito").
    *   ✨ **¡Nuevo!** Los escritos en la lista principal se pueden **expandir y contraer** para facilitar la lectura y reducir el desorden visual.

## ⚙️ Puesta en Marcha (Getting Started)

Sigue estos pasos para ejecutar el proyecto en tu entorno local.

**Prerrequisitos:**
*   Python 3.8+
*   pip & venv
*   Git

**Pasos:**

1.  **Clona el repositorio:**
    ```bash
    git clone https://github.com/Alialmandoz/taller_escritura.git
    cd taller_escritura
    ```

2.  **Crea y activa un entorno virtual:**
    ```bash
    # En macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # En Windows
    python -m venv venv
    venv\Scripts\activate
    ```

3.  **Instala las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Ejecuta las migraciones de la base de datos:**
    ```bash
    python manage.py migrate
    ```

5.  **Crea un superusuario (administrador):**
    ```bash
    python manage.py createsuperuser
    ```

6.  **¡Inicia el servidor!**
    ```bash
    python manage.py runserver
    ```
    La aplicación estará disponible en `http://127.0.0.1:8000/escritura/`.

## 🗺️ Roadmap (Hoja de Ruta)

El progreso del proyecto y las próximas funcionalidades planeadas.

*   [x] **Fase 1: Fundamentos**
    *   [x] Autenticación y Perfiles de Usuario básicos.
    *   [x] CRUD completo para Escritos.
    *   [x] Sistema de visibilidad (Público, Privado, Borrador).
    *   [x] Integración de Editor de Texto Enriquecido (CKEditor).
*   [x] **Fase 2: Usabilidad y Diseño**
    *   [x] Implementación de plantilla base y estilos CSS globales.
    *   [x] Diseño responsivo inicial.
    *   [x] Sistema de Mensajes de Django.
    *   [x] Funcionalidad para expandir/contraer escritos en la lista.
*   [ ] **Fase 3: Interacción y Comunidad (Próximos Pasos)**
    *   [ ] Edición de perfil de usuario (bio, foto de perfil).
    *   [ ] Sistema de comentarios en los escritos.
    *   [ ] Paginación en la lista de escritos.
    *   [ ] Funcionalidad de búsqueda.
*   [ ] **Fase 4: Funcionalidades Avanzadas**
    *   [ ] Implementación de etiquetas/categorías para los escritos.
    *   [ ] Sistema de notificaciones (ej. "Alguien comentó tu escrito").
    *   [ ] Panel de Control (Dashboard) personalizado para el usuario.

## 🤝 Contribución

Las contribuciones son bienvenidas. Para errores o sugerencias, por favor, abre un *issue*. Para contribuir con código, sigue el flujo estándar de `Fork` -> `Crea una Rama` -> `Pull Request`.

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
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
 d j a n g o - c k e d i t o r = = 6 . 7 . 3 
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
```

---

## Archivo: `escritura/models.py`

```python
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
    path('<int:pk>/eliminar/', views.eliminar_escrito, name='eliminar_escrito'),
    path('perfil/', views.perfil_usuario, name='perfil_usuario'),
    # AÑADIDO: URL para la página de edición del perfil
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
]
```

---

## Archivo: `escritura/views.py`

```python
# escritura/views.py

from django.shortcuts import render, get_object_or_404, redirect

# AÑADIDO: Vista para la página principal
def pagina_principal(request):
    """
    Renderiza la página de inicio/landing page.
    Obtiene todos los perfiles que han aceptado ser mostrados públicamente.
    """
    # Usamos select_related('user') para optimizar la consulta.
    # Evita que Django haga una consulta a la base de datos por cada usuario en el bucle de la plantilla.
    perfiles_publicos = Profile.objects.filter(mostrar_en_comunidad=True).select_related('user')

    contexto = {
        'perfiles_publicos': perfiles_publicos
    }
    return render(request, 'escritura/home.html', contexto)


from django.views.generic import DetailView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required # Decorador para requerir autenticación
from django.http import Http404
from django.contrib import messages

from .models import Escrito, Profile # MODIFICADO: Importamos también el modelo Profile
from .forms import CustomUserCreationForm, EscritoForm, ProfileForm # MODIFICADO: Importamos ProfileForm

# Vista basada en función para listar escritos públicos
def lista_escritos(request):
    """
    Esta vista recupera todos los objetos Escrito cuyo estado sea 'PUBLICO'
    y los pasa a la plantilla para su visualización.
    """
    # MODIFICADO: Se optimiza la consulta para incluir los datos del autor y su perfil.
    # Esto evita múltiples consultas a la base de datos (problema N+1) en la plantilla.
    escritos = Escrito.objects.filter(estado='PUBLICO').select_related('autor__profile').order_by('-fecha_creacion')

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
        # Si es GET, muestra un formulario vacío.
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


# AÑADIDO: Vista para mostrar el perfil del usuario y sus escritos
@login_required # Solo usuarios autenticados pueden acceder a su perfil.
def perfil_usuario(request):
    """
    Esta vista muestra el perfil del usuario autenticado, incluyendo
    su biografía, foto de perfil y una lista de TODOS sus escritos
    (sin importar el estado: borrador, privado, público).
    """
    # El objeto 'request.user' ya está disponible gracias a @login_required
    # y el middleware de autenticación.
    usuario = request.user

    # Intentamos obtener el perfil del usuario.
    # Gracias a la señal post_save que creamos, cada usuario debería tener un perfil.
    try:
        perfil = usuario.profile
    except Profile.DoesNotExist:
        # En un escenario muy improbable (ej. si la señal falló o se deshabilitó),
        # podríamos crear uno aquí o redirigir. Por ahora, asumimos que existe.
        perfil = Profile.objects.create(user=usuario)
        # Podrías añadir un mensaje de warning aquí si esto fuera algo que debe ser notado:
        # messages.warning(request, "Tu perfil fue creado automáticamente. Por favor, complétalo.")

    # MODIFICADO: Se optimiza la consulta para evitar el problema N+1.
    # Usamos `select_related` para traer la información del autor y su perfil
    # en una única consulta a la base de datos, mejorando drásticamente el rendimiento.
    mis_escritos = Escrito.objects.filter(autor=usuario).select_related('autor__profile').order_by('-fecha_creacion')

    contexto = {
        'usuario': usuario,      # El objeto User
        'perfil': perfil,        # El objeto Profile asociado
        'mis_escritos': mis_escritos # Todos los escritos del usuario
    }

    return render(request, 'escritura/perfil_usuario.html', contexto)


# AÑADIDO: Vista para editar el perfil del usuario
@login_required
def editar_perfil(request):
    """
    Permite al usuario autenticado editar su propio perfil (bio y foto).
    """
    if request.method == 'POST':
        # Al procesar el formulario, pasamos la instancia del perfil a actualizar.
        # ¡CRÍTICO! Pasamos request.FILES para manejar la subida de la imagen.
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save() # Guarda los cambios en el perfil del usuario.
            messages.success(request, '¡Tu perfil ha sido actualizado con éxito!')
            return redirect('escritura:perfil_usuario')
    else:
        # Al mostrar el formulario por primera vez, lo inicializamos con los datos actuales del perfil.
        form = ProfileForm(instance=request.user.profile)

    contexto = {
        'form': form
    }
    return render(request, 'escritura/editar_perfil.html', contexto)
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

## Archivo: `escritura/migrations/0003_alter_escrito_contenido.py`

```python
# Generated by Django 5.2.3 on 2025-06-27 19:45

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("escritura", "0002_profile"),
    ]

    operations = [
        migrations.AlterField(
            model_name="escrito",
            name="contenido",
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]

```

---

## Archivo: `escritura/migrations/0004_profile_mostrar_en_comunidad.py`

```python
# Generated by Django 5.2.3 on 2025-06-30 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escritura', '0003_alter_escrito_contenido'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='mostrar_en_comunidad',
            field=models.BooleanField(default=False, help_text='Marca esta casilla si deseas que tu perfil sea visible en la página principal.', verbose_name='Mostrar mi perfil en la página de la comunidad'),
        ),
    ]

```

---

## Archivo: `escritura/migrations/__init__.py`

```python

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
    {# AÑADIDO: Renderiza los archivos JS/CSS necesarios para el editor de texto enriquecido #}
    {{ form.media }}

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
    <div class="content">
        {{ escrito.contenido|safe }}
    </div>
    <p class="meta-info">
        Por: {{ escrito.autor.username }} |
        Publicado el: {{ escrito.fecha_creacion|date:"d M Y H:i" }} |
        Última actualización: {{ escrito.fecha_actualizacion|date:"d M Y H:i" }}
    </p>
    

    <a href="{% url 'escritura:lista_escritos' %}" class="back-link">← Volver a la lista de escritos</a>
{% endblock %}
```

---

## Archivo: `escritura/templates/escritura/editar_perfil.html`

```html
{# escritura/templates/escritura/editar_perfil.html #}
{% extends 'base.html' %}

{% block title %}Editar Mi Perfil{% endblock %}

{% block content %}
    <h1 class="page-title">Editar Mi Perfil</h1>

    {# ¡CRÍTICO! El atributo enctype es necesario para subir archivos (la foto de perfil). #}
    <form method="post" enctype="multipart/form-data">
        {% csrf_token %}

        {{ form.as_p }}

        <div style="display: flex; gap: 15px; margin-top: 20px;">
            <button type="submit" class="button primary">Guardar Cambios</button>
            <a href="{% url 'escritura:perfil_usuario' %}" class="button secondary">Cancelar</a>
        </div>
    </form>
{% endblock %}

```

---

## Archivo: `escritura/templates/escritura/home.html`

```html
{# escritura/templates/escritura/home.html #}
{% extends 'base.html' %}
{% load static %}

{% block title %}Bienvenido al Taller de Escritura{% endblock %}

{% block content %}

<div class="landing-page">
    <!-- HERO SECTION -->
    <section class="hero-section">
        <div class="hero-content">
            <h1 class="hero-title">Taller de Escritura de Cálamo y Papiro</h1>
            <p class="hero-subtitle">Donde tus historias encuentran su voz y tu creatividad no tiene límites.</p>
            <a href="{% url 'escritura:registro' %}" class="button primary large-button">Únete a la Comunidad</a>
        </div>
    </section>

    <!-- ABOUT SECTION -->
    <section class="about-section">
        <h2 class="section-title">¿Qué es Cálamo y Papiro?</h2>
        <p>Somos más que un taller; somos un refugio para creadores. Un espacio digital seguro y colaborativo diseñado para que escritores de todos los niveles puedan desarrollar sus textos, compartir ideas y recibir retroalimentación constructiva. Creemos en el poder de la comunidad para pulir el talento y en la disciplina de la escritura para dar forma a la imaginación.</p>
    </section>

    <!-- COMMUNITY SECTION -->
    <section class="community-section">
        <h2 class="section-title">Nuestra Comunidad</h2>
        <div class="community-gallery">
            {% for perfil in perfiles_publicos %}
                <div class="user-card">
                    <img src="{{ perfil.foto_perfil.url }}" alt="Foto de {{ perfil.user.username }}" class="user-card-img">
                    <h3 class="user-card-name">{{ perfil.user.username }}</h3>
                    {% if perfil.bio %}
                        <p class="user-card-bio">"{{ perfil.bio|truncatewords:15 }}"</p>
                    {% endif %}
                </div>
            {% empty %}
                <p class="community-empty">Nuestros miembros son un poco tímidos. ¡Pronto verás aquí los perfiles de nuestra increíble comunidad!</p>
            {% endfor %}
        </div>
    </section>
</div>

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
                    
                    {# MODIFICADO: Estructura de cabecera re-agrupada #}
                    <div class="escrito-card-header">
                        <div class="header-author-info">
                            <img class="author-pic" src="{{ escrito.autor.profile.foto_perfil.url }}" alt="Foto de {{ escrito.autor.username }}">
                            <span class="author-name">{{ escrito.autor.username }}</span>
                        </div>
                        <div class="header-title-actions">
                            <h2 class="escrito-title"><a href="{% url 'escritura:detalle_escrito' pk=escrito.pk %}">{{ escrito.titulo }}</a></h2>
                            <button 
                                class="toggle-button" 
                                aria-expanded="false" 
                                aria-controls="escrito-content-{{ escrito.pk }}"
                                title="Expandir/Contraer"
                            >
                            </button>
                        </div>
                    </div>
                    
                    <div class="escrito-content" id="escrito-content-{{ escrito.pk }}">
                        {{ escrito.contenido|safe }} 
                    </div>

                    <div class="escrito-footer">
                        <div class="escrito-meta">
                            <p>Publicado el: {{ escrito.fecha_creacion|date:"d M Y H:i" }}</p>
                        </div>
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

## Archivo: `escritura/templates/escritura/perfil_usuario.html`

```html
{# escritura/templates/escritura/perfil_usuario.html #}
{% extends 'base.html' %}
{% load static %} {# Asegúrate de cargar static para las imágenes #}

{% block title %}Perfil de {{ usuario.username }}{% endblock %}

{% block content %}
    <div class="profile-header">
        <img src="{{ perfil.foto_perfil.url }}" alt="Foto de perfil de {{ usuario.username }}" class="profile-pic">
        <h1 class="page-title">{{ usuario.username }}</h1>
        <p class="profile-bio">
            {% if perfil.bio %}
                {{ perfil.bio }}
            {% else %}
                Aún no has añadido una biografía.
            {% endif %}
        </p>
        {# MODIFICADO: El enlace ahora apunta a la página de edición. #}
        <a href="{% url 'escritura:editar_perfil' %}" class="button secondary">Editar Perfil</a>
    </div>

    <hr> {# Separador visual #}

    <h2 class="section-title">Mis Escritos</h2>

    {% if mis_escritos %}
        <ul class="escrito-list">
            {% for escrito in mis_escritos %}
                <li class="escrito-item">
                    
                    {# MODIFICADO: Estructura de cabecera re-agrupada #}
                    <div class="escrito-card-header">
                        <div class="header-author-info">
                            <img class="author-pic" src="{{ escrito.autor.profile.foto_perfil.url }}" alt="Foto de {{ escrito.autor.username }}">
                            <span class="author-name">{{ escrito.autor.username }}</span>
                        </div>
                        <div class="header-title-actions">
                            <h2 class="escrito-title"><a href="{% url 'escritura:detalle_escrito' pk=escrito.pk %}">{{ escrito.titulo }}</a></h2>
                            <button 
                                class="toggle-button" 
                                aria-expanded="false" 
                                aria-controls="escrito-content-perfil-{{ escrito.pk }}"
                                title="Expandir/Contraer"
                            >
                            </button>
                        </div>
                    </div>
                    
                    <div class="escrito-content" id="escrito-content-perfil-{{ escrito.pk }}">
                        {{ escrito.contenido|safe }} 
                    </div>

                    <div class="escrito-footer">
                        <div class="escrito-meta">
                            <p>Publicado el: {{ escrito.fecha_creacion|date:"d M Y H:i" }}</p>
                            {% if escrito.fecha_creacion != escrito.fecha_actualizacion %}
                                <p>Última actualización: {{ escrito.fecha_actualizacion|date:"d M Y H:i" }}</p>
                            {% endif %}
                        </div>
                        <div class="escrito-status-actions">
                            <span class="escrito-status status-{{ escrito.estado|lower }}">{{ escrito.get_estado_display }}</span>
                            <div class="action-buttons">
                                <a href="{% url 'escritura:editar_escrito' pk=escrito.pk %}" class="button warning small-button">Editar</a>
                                <a href="{% url 'escritura:eliminar_escrito' pk=escrito.pk %}" class="button danger small-button">Eliminar</a>
                            </div>
                        </div>
                    </div>
                </li>
            {% endfor %}
        </ul>
    {% else %}
        <p>Aún no has creado ningún escrito. <a href="{% url 'escritura:crear_escrito' %}">¡Empieza a escribir ahora!</a></p>
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
    font-family: 'Lato', sans-serif; /* APLICADO: Lato para el cuerpo de texto */
    margin: 0; /* Reset default body margin */
    background-color: #F5EFE6; /* Nuevo color de fondo principal (beige claro) */
    color: #333333; /* Color de texto general (gris oscuro) */
    display: flex;
    flex-direction: column; /* Para layout de pie de página pegajoso */
    min-height: 100vh; /* Asegura que el body ocupe el 100% del alto de la ventana */
}

/* Main Content Container */
.container {
    max-width: 800px; /* Límite de ancho para desktops */
    margin: 20px auto; /* Centrar y añadir margen superior/inferior */
    background-color: #FAF7F0; /* Nuevo color de fondo para el contenido/tarjetas (marfil) */
    padding: 20px; /* Ajuste de padding para móviles */
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    flex-grow: 1; /* Permite que el contenedor crezca y empuje el pie de página hacia abajo */
    box-sizing: border-box; /* Asegura que padding y borde no aumenten el ancho total */
}

/* Headings */
h1, h2, h3, h4, h5, h6 {
    font-family: 'Playfair Display', serif; /* APLICADO: Playfair Display para los encabezados */
    color: #AA775A; /* Nuevo color para encabezados (naranja/marrón cálido) */
    margin-top: 0;
    margin-bottom: 20px;
}

/* Links */
a {
    color: #6B4F4F; /* Nuevo color para enlaces (marrón oscuro) */
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
    font-family: 'Lato', sans-serif; /* APLICADO: Lato para botones */
}
.button:hover {
    background-color: #8C644E; /* Nuevo color de fondo para hover (marrón más oscuro) */
    text-decoration: none;
}

/* Specific button variants - ajustados a la nueva paleta */
.button.primary { /* Usado para "Crear Nuevo Escrito", "Publicar Escrito", "Guardar Cambios" */
    background-color: #AA775A;
}
.button.primary:hover {
    background-color: #8C644E;
}

.button.secondary { /* Usado para "Registrarse", "No, Cancelar" */
    background-color: #E8D8C9; /* Un tono más claro, complementario */
    color: #6B4F4F; /* Texto oscuro para contraste */
}
.button.secondary:hover {
    background-color: #CC9980; /* Un tono más fuerte para hover */
}

.button.warning { /* Usado para "Editar" */
    background-color: #AA775A; /* Se alinea con el color primario */
    color: white;
}
.button.warning:hover {
    background-color: #8C644E;
}

.button.danger { /* Usado para "Eliminar", "Sí, Eliminar" */
    background-color: #dc3545; /* Rojo estándar para peligro */
}
.button.danger:hover {
    background-color: #c82333; /* Rojo más oscuro al pasar el ratón */
}

/* Header Styles */
.main-header {
    background-color: #CC9980; /* Nuevo color de fondo para el encabezado (marrón rojizo claro) */
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
    font-family: 'Playfair Display', serif; /* APLICADO: Playfair Display para el logo */
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
    font-family: 'Lato', sans-serif; /* APLICADO: Lato para enlaces de navegación */
}

.nav-links a:hover {
    text-decoration: underline;
}

.welcome-message {
    font-weight: bold;
    margin-right: 0; /* Ya no necesitamos margen si están centrados */
    color: white;
    font-family: 'Lato', sans-serif; /* APLICADO: Lato para el mensaje de bienvenida */
}

/* Footer Styles */
.main-footer {
    background-color: #AA775A; /* Nuevo color para el pie de página (marrón rojizo cálido) */
    color: white;
    text-align: center;
    padding: 20px;
    margin-top: 40px; /* Margen superior para separarlo del contenido */
    font-family: 'Lato', sans-serif; /* APLICADO: Lato para el pie de página */
}

/* Form Styles (reused and adapted) */
form {
    display: flex;
    flex-direction: column;
}
form p {
    margin-bottom: 15px;
}
form p label {
    display: block;
    margin-bottom: 5px;
    font-weight: bold;
    color: #6B4F4F; /* Nuevo color para etiquetas de formulario */
    font-family: 'Lato', sans-serif; /* APLICADO: Lato para etiquetas de formulario */
}
input[type="text"],
input[type="password"],
input[type="email"],
select,
textarea {
    font-family: 'Lato', sans-serif; /* APLICADO: Lato para campos de formulario */
    width: 100%;
    padding: 10px;
    border: 1px solid #CC9980; /* Nuevo color para borde de campos */
    border-radius: 4px;
    box-sizing: border-box;
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
    font-family: 'Lato', sans-serif; /* APLICADO: Lato para mensajes de error de formulario */
}
.helptext {
    font-size: 0.8em;
    color: #8C644E; /* Nuevo color para texto de ayuda */
    margin-top: 5px;
    font-family: 'Lato', sans-serif; /* APLICADO: Lato para texto de ayuda */
}

/* Specific Escrito List/Detail Styles */
.escrito-list {
    list-style: none;
    padding: 0;
}

.escrito-item {
    background-color: #FAF7F0;
    margin-bottom: 20px;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

/* AÑADIDO: Nueva cabecera unificada */
.escrito-card-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 15px;
    margin-bottom: 15px;
}

/* AÑADIDO: Grupo para info del autor a la izquierda */
.header-author-info {
    display: flex;
    align-items: center;
    gap: 10px;
    min-width: 0; /* Evita que el contenedor se desborde si el nombre es largo */
}

/* AÑADIDO: Grupo para título y acciones a la derecha */
.header-title-actions {
    display: flex;
    align-items: center;
    gap: 15px;
}

.author-pic {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    object-fit: cover;
    border: 2px solid #E8D8C9;
    flex-shrink: 0; /* Evita que la imagen se encoja */
}

.author-name {
    font-weight: bold;
    color: #6B4F4F;
    font-family: 'Lato', sans-serif;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

.escrito-title {
    margin: 0; /* Quitamos margen del h2 */
    font-family: 'Playfair Display', serif;
    color: #AA775A;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

.escrito-title a {
    text-decoration: none;
    color: inherit; /* Hereda el color del h2 */
}

.escrito-title a:hover {
    text-decoration: underline;
}

.escrito-meta p {
    margin: 0;
    line-height: 1.4;
}

.escrito-content {
    max-height: 100px;
    overflow: hidden;
    position: relative;
    transition: max-height 0.4s ease-in-out;
    line-height: 1.6;
    font-family: 'Lato', sans-serif;
}

.escrito-item.is-expanded .escrito-content {
    max-height: 1500px;
}

.escrito-content::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    height: 30px;
    background: linear-gradient(to bottom, transparent, #FAF7F0);
    transition: opacity 0.4s ease-in-out;
}

.escrito-item.is-expanded .escrito-content::after {
    opacity: 0;
}

.toggle-button {
    width: 28px;
    height: 28px;
    background-color: #E8D8C9;
    color: #AA775A;
    border: 1px solid #CC9980;
    border-radius: 50%;
    cursor: pointer;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 20px;
    font-weight: bold;
    line-height: 1;
    padding: 0;
    transition: background-color 0.3s, transform 0.3s;
    flex-shrink: 0;
}

.toggle-button:hover {
    background-color: #CC9980;
    color: white;
}

.toggle-button::before {
    content: '+';
}

.escrito-item.is-expanded .toggle-button::before {
    content: '−';
}

.escrito-item.is-expanded .toggle-button {
    transform: rotate(180deg);
}

.escrito-footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 15px;
    margin-top: 15px;
    padding-top: 15px;
    border-top: 1px solid #E8D8C9;
    font-size: 0.9em;
    color: #6B4F4F;
    font-family: 'Lato', sans-serif;
}

.escrito-status-actions {
    display: flex;
    align-items: center;
    gap: 15px;
    flex-wrap: wrap;
}

/* Escrito Detail Specific Styles */
.header-section {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 10px;
}
.header-section h1 {
    flex-grow: 1;
    margin-right: 10px;
    font-family: 'Playfair Display', serif;
}
.action-buttons {
    display: flex;
    gap: 10px;
}
.content {
    line-height: 1.8;
    color: #444444;
    font-family: 'Lato', sans-serif;
}
.content p {
    margin-bottom: 1em;
}
.back-link {
    display: block;
    margin-top: 30px;
    text-align: center;
    text-decoration: none;
    color: #6B4F4F;
    font-weight: bold;
    font-family: 'Lato', sans-serif;
}
.back-link:hover {
    text-decoration: underline;
}

/* Estilos para el sistema de mensajes de Django */
.messages {
    list-style: none;
    padding: 0;
    margin-bottom: 20px;
    font-family: 'Lato', sans-serif;
}

.messages li {
    padding: 15px;
    margin-bottom: 10px;
    border-radius: 5px;
    font-weight: bold;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border: 1px solid transparent;
    color: #333;
    position: relative;
}

.messages li.success {
    background-color: #d4edda;
    border-color: #c3e6cb;
    color: #155724;
}

.messages li.info {
    background-color: #d1ecf1;
    border-color: #bee5eb;
    color: #0c5460;
}

.messages li.warning {
    background-color: #fff3cd;
    border-color: #ffeeba;
    color: #856404;
}

.messages li.error {
    background-color: #f8d7da;
    border-color: #f5c6cb;
    color: #721c24;
}

.close-message {
    cursor: pointer;
    font-weight: bold;
    font-size: 1.2em;
    padding: 0 5px;
    line-height: 1;
}
.close-message:hover {
    color: black;
}


/* Media Queries for Responsiveness */

@media (min-width: 600px) {
    .container {
        padding: 30px;
    }
    .main-header {
        padding: 15px 30px;
    }
    .logo {
        flex-basis: auto;
        text-align: left;
        margin-bottom: 0;
    }
    .nav-links {
        justify-content: flex-end;
        width: auto;
    }
}

@media (min-width: 992px) {
    .container {
        margin-top: 40px;
        margin-bottom: 40px;
    }
    h1 {
        font-size: 2.5em;
    }
    .logo a {
        font-size: 2em;
    }
}

/* Estilos específicos para la página de perfil */
.profile-header {
    text-align: center;
    margin-bottom: 40px;
    padding-bottom: 20px;
    border-bottom: 1px solid #E8D8C9;
}
.profile-pic {
    width: 150px;
    height: 150px;
    border-radius: 50%;
    object-fit: cover;
    margin-bottom: 15px;
    border: 3px solid #AA775A;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}
.profile-bio {
    font-size: 1.1em;
    color: #6B4F4F;
    max-width: 600px;
    margin: 0 auto 20px auto;
    line-height: 1.6;
}
.section-title {
    text-align: center;
    margin-top: 40px;
    margin-bottom: 30px;
    font-size: 2em;
    color: #AA775A;
    font-family: 'Playfair Display', serif;
}
hr {
    border: none;
    border-top: 1px dashed #E8D8C9;
    margin: 40px 0;
}

.escrito-status {
    padding: 5px 10px;
    border-radius: 4px;
    font-size: 0.8em;
    font-weight: bold;
    color: white;
    text-transform: uppercase;
    font-family: 'Lato', sans-serif;
}
.status-borrador { background-color: #6c757d; }
.status-privado { background-color: #AA775A; }
.status-publico { background-color: #28a745; }

.small-button {
    padding: 5px 10px;
    font-size: 0.8em;
}

@media (max-width: 600px) {
    .profile-bio {
        padding: 0 10px;
    }
    /* En pantallas pequeñas, permitimos que la cabecera se envuelva */
    .escrito-card-header {
        flex-wrap: wrap;
    }
}

/* Estilos para la página de inicio (home.html) */
.landing-page { padding: 0; }

.hero-section {
    background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('https://images.unsplash.com/photo-1455390582262-044cdead277a?ixlib=rb-4.0.3&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1971') no-repeat center center/cover;
    color: white;
    text-align: center;
    padding: 100px 20px;
    background-color: transparent !important;
}

.hero-section .hero-title {
    color: white;
    font-size: 3em;
    font-family: 'Playfair Display', serif;
}

.hero-section .hero-subtitle {
    font-size: 1.2em;
    margin-bottom: 30px;
    font-family: 'Lato', sans-serif;
    color: white;
}

.hero-section .large-button {
    padding: 15px 30px;
    font-size: 1.1em;
}

.about-section, .community-section {
    padding: 60px 20px;
    max-width: 900px;
    margin: 0 auto;
    background-color: #FAF7F0;
    border-radius: 0;
}

.about-section .section-title,
.community-section .section-title {
    text-align: center;
    margin-bottom: 40px;
    font-size: 2.2em;
    color: #AA775A;
    font-family: 'Playfair Display', serif;
}

.community-gallery {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 20px;
}

.user-card {
    background-color: #FAF7F0;
    border: 1px solid #E8D8C9;
    border-radius: 8px;
    width: 200px;
    text-align: center;
    padding: 20px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.05);
}

.user-card-img {
    width: 100px;
    height: 100px;
    border-radius: 50%;
    object-fit: cover;
    border: 3px solid #CC9980;
    margin-bottom: 10px;
}

.user-card-name {
    font-size: 1.2em;
    margin: 10px 0 10px 0;
    color: #6B4F4F;
    font-family: 'Playfair Display', serif;
}

.user-card-bio {
    font-size: 0.9em;
    color: #6B4F4F;
    font-style: italic;
    font-family: 'Lato', sans-serif;
    line-height: 1.4;
}

.community-empty {
    width: 100%;
    text-align: center;
    color: #6B4F4F;
    font-family: 'Lato', sans-serif;
    padding: 20px 0;
}

/* AÑADIDO: Estilos para que el botón de logout parezca un enlace en la barra de navegación */
.nav-link-button {
    background: none;
    border: none;
    padding: 0;
    margin: 0;
    cursor: pointer;
    font-family: inherit; /* Hereda la fuente de su contenedor (ul.nav-links) */
    
    /* Replicamos los estilos de .nav-links a */
    color: white;
    text-decoration: none;
    font-weight: bold;
    font-size: 1em; /* Asegura que el tamaño de fuente sea el mismo */
}

.nav-link-button:hover {
    text-decoration: underline;
}
```

---

## Archivo: `static/js/Main.js`

```javascript
// static/js/main.js

// Usamos 'DOMContentLoaded' para asegurarnos de que el script se ejecuta
// solo después de que todo el HTML de la página se haya cargado y parseado.
// Es una buena práctica para evitar errores de "elemento no encontrado".
document.addEventListener('DOMContentLoaded', function () {

    // SECCIÓN: Lógica para contraer/expandir escritos en la lista
    // -----------------------------------------------------------

    // 1. Seleccionamos todos los elementos de la lista de escritos.
    const escritoItems = document.querySelectorAll('.escrito-item');

    // 2. Iteramos sobre cada elemento de la lista para añadirle la funcionalidad.
    escritoItems.forEach(item => {
        // Encontramos el contenido y el botón dentro de cada item.
        const content = item.querySelector('.escrito-content');
        const toggleButton = item.querySelector('.toggle-button');

        // Si no encontramos el contenido o el botón, saltamos al siguiente item.
        if (!content || !toggleButton) return;

        // Por defecto, comprobamos si el contenido es más alto que nuestra altura colapsada.
        // Si no lo es, no necesitamos el botón, así que lo ocultamos.
        // `scrollHeight` es la altura total del contenido, `clientHeight` es la altura visible.
        if (content.scrollHeight <= content.clientHeight) {
            toggleButton.style.display = 'none';
        }

        // 3. Añadimos un 'escuchador de eventos' al botón.
        //    Esto ejecuta una función cada vez que el usuario hace clic en el botón.
        toggleButton.addEventListener('click', () => {
            // `classList.toggle` es un método muy útil:
            // - Si la clase 'is-expanded' existe en el 'item', la quita.
            // - Si la clase 'is-expanded' no existe, la añade.
            // Esto nos permite cambiar entre los dos estados con una sola línea.
            item.classList.toggle('is-expanded');

            // MEJORA DE ACCESIBILIDAD: Actualizamos el atributo aria-expanded.
            const isExpanded = item.classList.contains('is-expanded');
            toggleButton.setAttribute('aria-expanded', isExpanded);
        });
    });
});
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
    # AÑADIDO: Apps de CKEditor
    'ckeditor',
    'ckeditor_uploader', # Necesario para subir imágenes
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

# AÑADIDO: Configuración específica para django-ckeditor
CKEDITOR_UPLOAD_PATH = 'uploads/' # Las imágenes subidas desde el editor se guardarán en MEDIA_ROOT/uploads/

# Opcional: Configuración de la barra de herramientas de CKEditor
# Puedes personalizar qué botones aparecen en el editor.
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom', # Define una barra de herramientas personalizada
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline', 'Strike', '-', 'Subscript', 'Superscript'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', 'Blockquote', 'CreateDiv'],
            ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink', 'Anchor'],
            ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak'],
            ['Styles', 'Format', 'Font', 'FontSize'],
            ['TextColor', 'BGColor'],
            ['Maximize', 'ShowBlocks', '-', 'About'],
            ['Source'] # Botón para ver el código fuente HTML
        ],
        'width': '100%', # Opcional: Ancho del editor
        'height': 300,   # Opcional: Alto del editor
        'extraPlugins': 'codesnippet', # Ejemplo: Añadir un plugin para snippets de código
        # Más opciones en: https://ckeditor.com/docs/ckeditor4/latest/api/CKEDITOR_config.html
    }
}
```

---

## Archivo: `taller_escritura/urls.py`

```python
from django.contrib import admin
from django.urls import path, include 
from django.conf import settings # AÑADIDO: Para importar settings
from django.conf.urls.static import static # AÑADIDO: Para servir archivos media en desarrollo
from escritura import views # AÑADIDO: Importamos las vistas de nuestra app

urlpatterns = [
    # AÑADIDO: URL para la página principal
    path('', views.pagina_principal, name='home'),

    path('admin/', admin.site.urls),
    path('escritura/', include('escritura.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    # AÑADIDO: URLs para django-ckeditor-uploader
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

# AÑADIDO: Configuración para servir archivos de medios en el servidor de desarrollo.
# ¡Esto solo debe usarse en desarrollo (DEBUG = True)!
# En producción, un servidor web como Nginx o Apache se encargará de servir los archivos media.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

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
{% load static %}
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Taller de Escritura de Cálamo y Papiro {% endblock %}</title>
    
    {# AÑADIDO: Enlaces para importar las fuentes de Google Fonts #}
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Lato:wght@400;700&family=Playfair+Display:wght@400;700&display=swap" rel="stylesheet">

    {# MODIFICADO: Link a nuestro archivo CSS principal (debe ir después de las fuentes para poder usarlas) #}
    <link rel="stylesheet" href="{% static 'css/main.css' %}">
    
    {% block head_extra %}{% endblock %} 
</head>
<body>
    <header class="main-header">
        <nav class="main-nav">
            <div class="logo">
                <a href="{% url 'escritura:lista_escritos' %}">Taller de Escritura de Cálamo y Papiro</a>
            </div>
            <ul class="nav-links">
                {% if user.is_authenticated %}
                    <li><span class="welcome-message">Hola, {{ user.username }}!</span></li>
                    {# AÑADIDO: Enlace a la página de perfil #}
                    <li><a href="{% url 'escritura:perfil_usuario' %}">Mi Perfil</a></li>
                    
                    {# MODIFICADO: Reemplazamos el enlace <a> por un formulario <form> #}
                    <li>
                        <form method="post" action="{% url 'logout' %}" style="display: inline;">
                            {% csrf_token %}
                            <button type="submit" class="nav-link-button">Cerrar Sesión</button>
                        </form>
                    </li>
                    
                    <li><a href="{% url 'escritura:crear_escrito' %}" class="button primary">+ Crear Nuevo Escrito</a></li>
                {% else %}
                    <li><a href="{% url 'login' %}" class="button">Iniciar Sesión</a></li>
                    <li><a href="{% url 'escritura:registro' %}" class="button secondary">Registrarse</a></li>
                {% endif %}
            </ul>
        </nav>
    </header>

    <main class="container">
        {# AÑADIDO: Bloque para mostrar mensajes del sistema de Django #}
        {% if messages %}
            <ul class="messages">
                {% for message in messages %}
                    {# Cada mensaje tiene tags como 'success', 'info', 'warning', 'error' #}
                    <li{% if message.tags %} class="{{ message.tags }}"{% endif %}>
                        {{ message }}
                        <span class="close-message" onclick="this.parentNode.style.display='none';">×</span> {# Pequeña "X" para cerrar #}
                    </li>
                {% endfor %}
            </ul>
        {% endif %}
        {# Fin del bloque de mensajes #}

        {% block content %}
        {% endblock %}
    </main>

    <footer class="main-footer"> {# MODIFICADO: Cambiado de <footer> a <footer class="main-footer"> para consistencia #}
        <p>© 2025 Taller de Escritura. Todos los derechos reservados.</p>
    </footer>

    {% block body_extra %}{% endblock %}

    {# AÑADIDO: Carga del archivo JavaScript principal del sitio. #}
    {# Se coloca al final del body para no bloquear la renderización del contenido de la página. #}
    <script src="{% static 'js/main.js' %}"></script>
</body>
</html>
```

---

## Archivo: `taller_escritura/templates/registration/login.html`

```html
{# taller_escritura/templates/registration/login.html #}
{% extends 'base.html' %}

{% block title %}Iniciar Sesión{% endblock %}

{% block content %}
    <h1 class="page-title">Iniciar Sesión</h1>

    {% if form.errors %}
        <p style="color: red;">Tu nombre de usuario y contraseña no coinciden. Por favor, inténtalo de nuevo.</p>
    {% endif %}

    {% if next %}
        {% if user.is_authenticated %}
            <p>Tu cuenta no tiene acceso a esta página. Para continuar, por favor inicia sesión con una cuenta que tenga acceso.</p>
        {% else %}
            <p>Por favor, inicia sesión para ver esta página.</p>
        {% endif %}
    {% endif %}

    <form method="post" action="{% url 'login' %}">
        {# CORREGIDO: Añadimos la etiqueta CSRF token. ¡Esto es fundamental para la seguridad! #}
        {% csrf_token %}
        
        {{ form.as_p }}
        
        <button type="submit" class="button primary" style="margin-top: 20px;">Iniciar Sesión</button>
        <input type="hidden" name="next" value="{{ next }}">
    </form>

    <div style="margin-top: 20px;">
        <p><a href="{% url 'password_reset' %}">¿Olvidaste tu contraseña?</a></p>
        <p>¿No tienes una cuenta? <a href="{% url 'escritura:registro' %}">Regístrate aquí</a>.</p>
    </div>

{% endblock %}
```

---

## Lista de Archivos con Contenido Omitido

*(Binarios, errores de codificación/lectura, o errores inesperados durante el procesamiento)*

- `.gitignore (Extensión no listada)`
- `Beige Ivory Watercolor Minimalist Productivity New Blog Instagram Post.png (Extensión no listada)`

## Lista de Archivos Omitidos por Tamaño Excesivo

Ninguno.
