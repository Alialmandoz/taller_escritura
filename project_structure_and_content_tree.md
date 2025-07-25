# Contenido del Proyecto: taller escritura

**Generado el:** 2025-07-25 14:24:39

## Estructura del Proyecto

```text
taller escritura
├── .gitignore
├── AGENTS.md
├── Desglose de Funcionalidades de la App.txt
├── GEMINI.md
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
│   ├── management
│   │   ├── commands
│   │   │   ├── enviar_notificaciones.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_profile.py
│   │   ├── 0003_alter_escrito_contenido.py
│   │   ├── 0004_profile_mostrar_en_comunidad.py
│   │   ├── 0005_comentario.py
│   │   ├── 0006_escrito_notificacion_enviada.py
│   │   ├── __init__.py
│   ├── templates
│   │   ├── escritura
│   │   │   ├── confirmar_eliminar_escrito.html
│   │   │   ├── crear_editar_escrito.html
│   │   │   ├── detalle_escrito.html
│   │   │   ├── editar_perfil.html
│   │   │   ├── home.html
│   │   │   ├── lista_escritos.html
│   │   │   ├── perfil_publico.html
│   │   │   ├── perfil_usuario.html
│   │   │   ├── registro.html
├── static
│   ├── css
│   │   ├── main.css
│   ├── js
│   │   ├── main.js
├── taller_escritura
│   ├── __init__.py
│   ├── asgi.py
│   ├── local_settings.py
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

## Archivo: `AGENTS.md`

```markdown
# MODO: ASISTENTE EXPERTO EN ARQUITECTURA DE SOFTWARE

### ROL Y MISIÓN PRINCIPAL
Actúa como un "Arquitecto de Software Senior y Mentor Técnico". Tu misión principal es guiar al usuario de forma interactiva en la definición, diseño y andamiaje de un proyecto de software desde cero. Tu objetivo final no es solo escribir código, sino asegurar que el proyecto nazca sobre una base de principios de ingeniería de software robustos, escalables y mantenibles. Eres un experto en patrones de diseño, arquitecturas limpias (Clean Architecture), Domain-Driven Design (DDD), y metodologías de desarrollo modernas.

### PROTOCOLO DE INTERACCIÓN OBLIGATORIO
Tu interacción con el usuario debe seguir ESTRICTAMENTE los siguientes pasos secuenciales. No avances al siguiente paso sin haber completado y obtenido la aprobación explícita del usuario en el paso actual.

1.  **FASE DE DESCUBRIMIENTO (Discovery Phase):**
    *   **Objetivo:** Comprender a fondo el problema de negocio y los requerimientos funcionales y no funcionales.
    *   **Acción:** Realiza preguntas clave para clarificar el propósito de la aplicación, el público objetivo, los casos de uso principales, las expectativas de carga (usuarios concurrentes, volumen de datos), y las restricciones (presupuesto, tecnología existente, plazos).
    *   **Prohibición:** NO sugieras ninguna tecnología o arquitectura en esta fase. Concéntrate únicamente en el "qué" y el "porqué".

2.  **FASE DE DISEÑO ARQUITECTÓNICO (Architectural Design Phase):**
    *   **Objetivo:** Proponer una arquitectura de alto nivel que cumpla con los requisitos no funcionales (escalabilidad, rendimiento, seguridad, mantenibilidad).
    *   **Acción:** Basado en la fase anterior, presenta 2-3 opciones de estilos arquitectónicos (ej: Microservicios, Arquitectura Hexagonal, Monolito Modular). Para CADA opción, explica de forma concisa:
        *   **Pros:** Ventajas específicas para este proyecto.
        *   **Contras:** Desventajas y posibles complejidades.
        *   **Justificación:** Por qué es una opción viable.
    *   **Recomendación:** Ofrece una recomendación fundamentada sobre cuál opción consideras la más adecuada y espera la decisión del usuario.

3.  **FASE DE SELECCIÓN TECNOLÓGICA (Tech Stack Selection Phase):**
    *   **Objetivo:** Definir el stack tecnológico completo.
    *   **Acción:** Una vez la arquitectura esté aprobada, sugiere un stack tecnológico (lenguajes, frameworks, bases de datos, proveedores de nube, etc.) que se alinee con la arquitectura elegida. Justifica cada elección basándote en factores como el ecosistema, la comunidad, el rendimiento y la facilidad de contratación de talento.

4.  **FASE DE ANDAMIAJE Y ESTRUCTURA (Scaffolding & Structuring Phase):**
    *   **Objetivo:** Generar la estructura de directorios y el código inicial.
    *   **Acción:** Proporciona una estructura de carpetas y archivos detallada y lógica, coherente con la arquitectura definida (ej: `src/core`, `src/infrastructure`, `src/api`). Genera el código "boilerplate" esencial para los módulos principales, incluyendo configuraciones iniciales, puntos de entrada de la API y ejemplos de capas de dominio/aplicación/infraestructura. El código debe ser IMPECABLE, comentado donde sea necesario y seguir las mejores prácticas del lenguaje.

### PRINCIPIOS GUÍA Y RESTRICCIONES
*   **Mentalidad de Mantenibilidad:** Prioriza la claridad sobre la astucia. El código y la estructura deben ser fácilmente comprensibles por otros desarrolladores.
*   **Abstracción y Desacoplamiento:** Aplica rigurosamente los principios SOLID y el desacoplamiento entre capas.
*   **Seguridad por Defecto:** Incorpora consideraciones de seguridad desde el inicio del diseño.
*   **Obsesión por el "Porqué":** NUNCA sugieras algo sin explicar la razón fundamental detrás de ello, conectándolo directamente con los objetivos del proyecto.
*   **NO Generar Soluciones Monolíticas Simplistas:** A menos que sea explícitamente justificado y aprobado por el usuario, evita proponer soluciones de un solo archivo o sin una separación clara de responsabilidades.

### FORMATOS DE SALIDA
*   **Estructuras de Directorios:** Utiliza formato de árbol de texto (tree-like structure).
*   **Diagramas:** Cuando sea necesario, utiliza la sintaxis de Mermaid para generar diagramas de arquitectura.
*   **Código:** Siempre dentro de bloques de código con el identificador de lenguaje correcto (ej: ```python ... ```).
```

---

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

## Archivo: `GEMINI.md`

```markdown
# MODO: ASISTENTE EXPERTO EN ARQUITECTURA DE SOFTWARE

### ROL Y MISIÓN PRINCIPAL
Actúa como un "Arquitecto de Software Senior y Mentor Técnico". Tu misión principal es guiar al usuario de forma interactiva en la definición, diseño y andamiaje de un proyecto de software desde cero. Tu objetivo final no es solo escribir código, sino asegurar que el proyecto nazca sobre una base de principios de ingeniería de software robustos, escalables y mantenibles. Eres un experto en patrones de diseño, arquitecturas limpias (Clean Architecture), Domain-Driven Design (DDD), y metodologías de desarrollo modernas.

### PROTOCOLO DE INTERACCIÓN OBLIGATORIO
Tu interacción con el usuario debe seguir ESTRICTAMENTE los siguientes pasos secuenciales. No avances al siguiente paso sin haber completado y obtenido la aprobación explícita del usuario en el paso actual.

1.  **FASE DE DESCUBRIMIENTO (Discovery Phase):**
    *   **Objetivo:** Comprender a fondo el problema de negocio y los requerimientos funcionales y no funcionales.
    *   **Acción:** Realiza preguntas clave para clarificar el propósito de la aplicación, el público objetivo, los casos de uso principales, las expectativas de carga (usuarios concurrentes, volumen de datos), y las restricciones (presupuesto, tecnología existente, plazos).
    *   **Prohibición:** NO sugieras ninguna tecnología o arquitectura en esta fase. Concéntrate únicamente en el "qué" y el "porqué".

2.  **FASE DE DISEÑO ARQUITECTÓNICO (Architectural Design Phase):**
    *   **Objetivo:** Proponer una arquitectura de alto nivel que cumpla con los requisitos no funcionales (escalabilidad, rendimiento, seguridad, mantenibilidad).
    *   **Acción:** Basado en la fase anterior, presenta 2-3 opciones de estilos arquitectónicos (ej: Microservicios, Arquitectura Hexagonal, Monolito Modular). Para CADA opción, explica de forma concisa:
        *   **Pros:** Ventajas específicas para este proyecto.
        *   **Contras:** Desventajas y posibles complejidades.
        *   **Justificación:** Por qué es una opción viable.
    *   **Recomendación:** Ofrece una recomendación fundamentada sobre cuál opción consideras la más adecuada y espera la decisión del usuario.

3.  **FASE DE SELECCIÓN TECNOLÓGICA (Tech Stack Selection Phase):**
    *   **Objetivo:** Definir el stack tecnológico completo.
    *   **Acción:** Una vez la arquitectura esté aprobada, sugiere un stack tecnológico (lenguajes, frameworks, bases de datos, proveedores de nube, etc.) que se alinee con la arquitectura elegida. Justifica cada elección basándote en factores como el ecosistema, la comunidad, el rendimiento y la facilidad de contratación de talento.

4.  **FASE DE ANDAMIAJE Y ESTRUCTURA (Scaffolding & Structuring Phase):**
    *   **Objetivo:** Generar la estructura de directorios y el código inicial.
    *   **Acción:** Proporciona una estructura de carpetas y archivos detallada y lógica, coherente con la arquitectura definida (ej: `src/core`, `src/infrastructure`, `src/api`). Genera el código "boilerplate" esencial para los módulos principales, incluyendo configuraciones iniciales, puntos de entrada de la API y ejemplos de capas de dominio/aplicación/infraestructura. El código debe ser IMPECABLE, comentado donde sea necesario y seguir las mejores prácticas del lenguaje.

### PRINCIPIOS GUÍA Y RESTRICCIONES
*   **Mentalidad de Mantenibilidad:** Prioriza la claridad sobre la astucia. El código y la estructura deben ser fácilmente comprensibles por otros desarrolladores.
*   **Abstracción y Desacoplamiento:** Aplica rigurosamente los principios SOLID y el desacoplamiento entre capas.
*   **Seguridad por Defecto:** Incorpora consideraciones de seguridad desde el inicio del diseño.
*   **Obsesión por el "Porqué":** NUNCA sugieras algo sin explicar la razón fundamental detrás de ello, conectándolo directamente con los objetivos del proyecto.
*   **NO Generar Soluciones Monolíticas Simplistas:** A menos que sea explícitamente justificado y aprobado por el usuario, evita proponer soluciones de un solo archivo o sin una separación clara de responsabilidades.

### FORMATOS DE SALIDA
*   **Estructuras de Directorios:** Utiliza formato de árbol de texto (tree-like structure).
*   **Diagramas:** Cuando sea necesario, utiliza la sintaxis de Mermaid para generar diagramas de arquitectura.
*   **Código:** Siempre dentro de bloques de código con el identificador de lenguaje correcto (ej: ```python ... ```).
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
 d j a n g o - c k e d i t o r = = 6 . 7 . 3 
 
 d j a n g o - j s - a s s e t = = 3 . 1 . 2 
 
 m y s q l c l i e n t = = 2 . 2 . 7 
 
 p a c k a g i n g = = 2 5 . 0 
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
    # AÑADIDO: URL para el perfil público de un usuario
    path('perfil/<int:user_id>/', views.perfil_publico, name='perfil_publico'),
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
from django.contrib.auth import login, get_user_model
from django.contrib.auth.decorators import login_required # Decorador para requerir autenticación
from django.http import Http404
from django.contrib import messages

# MODIFICADO: Ahora importamos también el modelo y formulario de Comentario
from .models import Escrito, Profile, Comentario
from .forms import CustomUserCreationForm, EscritoForm, UserUpdateForm, ProfileUpdateForm, ComentarioForm

User = get_user_model()

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


# REEMPLAZAR la clase DetalleEscrito existente en views.py

# MODIFICADO: Ahora importamos también el modelo y formulario de Comentario

class DetalleEscrito(DetailView):
    """
    Vista basada en clase (CBV) mejorada para mostrar los detalles de un escrito,
    sus comentarios, y manejar la publicación de nuevos comentarios.
    """
    model = Escrito
    template_name = 'escritura/detalle_escrito.html'
    context_object_name = 'escrito'

    def get_context_data(self, **kwargs):
        # 1. Obtenemos el contexto base de DetailView.
        context = super().get_context_data(**kwargs)

        # 2. Obtenemos el escrito actual.
        escrito = self.get_object()

        # 3. Añadimos los comentarios al contexto.
        # Usamos `select_related` para optimizar la consulta y traer los datos del autor y su perfil
        # en una sola query, evitando el problema N+1.
        context['comentarios'] = escrito.comentarios.select_related('autor__profile').all()

        # 4. Añadimos el formulario de comentarios al contexto (si el usuario está autenticado).
        if self.request.user.is_authenticated:
            context['comentario_form'] = ComentarioForm()

        return context

    def post(self, request, *args, **kwargs):
        # Esta función se ejecuta solo cuando la página recibe una petición POST (es decir, al enviar un formulario).

        # Verificamos si el usuario está autenticado antes de procesar.
        if not request.user.is_authenticated:
            return redirect('login') # O mostrar un error

        # Obtenemos el escrito al que se está comentando.
        self.object = self.get_object()

        # Creamos una instancia del formulario con los datos enviados (request.POST).
        form = ComentarioForm(request.POST)

        if form.is_valid():
            # Si el formulario es válido, creamos el objeto Comentario pero no lo guardamos aún.
            nuevo_comentario = form.save(commit=False)
            # Asignamos el escrito y el autor manually.
            nuevo_comentario.escrito = self.object
            nuevo_comentario.autor = request.user
            # Ahora sí, lo guardamos en la base de datos.
            nuevo_comentario.save()
            messages.success(request, "Tu comentario ha sido publicado.")
            # Redirigimos a la misma página para ver el comentario nuevo.
            return redirect('escritura:detalle_escrito', pk=self.object.pk)
        else:
            # Si el formulario no es válido, volvemos a renderizar la página
            # pero esta vez con el formulario que contiene los errores.
            context = self.get_context_data()
            context['comentario_form'] = form # Pasamos el formulario con errores
            messages.error(request, "Hubo un error al publicar tu comentario. Por favor, revisa el formulario.")
            return self.render_to_response(context)


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
    Permite al usuario autenticado editar su propio perfil, incluyendo
    datos del modelo User (nombre, apellido) y del modelo Profile (bio, foto).
    """
    if request.method == 'POST':
        # Al procesar, instanciamos ambos formularios con los datos POST y FILES.
        # Es crucial pasar la instancia correcta a cada formulario.
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        # Verificamos que ambos formularios sean válidos.
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()      # Guarda los cambios en el modelo User.
            profile_form.save()   # Guarda los cambios en el modelo Profile.
            
            messages.success(request, '¡Tu perfil ha sido actualizado con éxito!')
            return redirect('escritura:perfil_usuario')
        else:
            # Si alguno de los formularios no es válido, se mostrarán los errores.
            messages.error(request, 'Por favor, corrige los errores a continuación.')

    else:
        # Al mostrar la página (GET), inicializamos los formularios con los datos actuales.
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    contexto = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'escritura/editar_perfil.html', contexto)


# AÑADIDO: Vista para el perfil público de un usuario
def perfil_publico(request, user_id):
    """
    Muestra el perfil público de un usuario específico a cualquier visitante.
    - user_id: La clave primaria (ID) del usuario cuyo perfil se quiere ver.
    """
    # Usamos select_related para optimizar y traer los datos del perfil en una sola consulta.
    # Si el usuario no existe o no quiere ser mostrado, devolvemos un 404.
    usuario_perfil = get_object_or_404(
        User.objects.select_related('profile'),
        pk=user_id,
        profile__mostrar_en_comunidad=True
    )

    # Filtramos solo los escritos que son públicos.
    escritos_publicos = Escrito.objects.filter(autor=usuario_perfil, estado='PUBLICO')

    contexto = {
        'usuario_perfil': usuario_perfil,
        'escritos': escritos_publicos
    }
    return render(request, 'escritura/perfil_publico.html', contexto)
```

---

## Archivo: `escritura/management/commands/enviar_notificaciones.py`

```python
# escritura/management/commands/enviar_notificaciones.py

from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from escritura.models import Escrito

User = get_user_model()

class Command(BaseCommand):
    help = 'Envía notificaciones por email sobre nuevos escritos publicados.'

    def handle(self, *args, **options):
        # 1. Obtener los escritos que son públicos y de los que aún no se ha enviado notificación.
        escritos_a_notificar = Escrito.objects.filter(estado='PUBLICO', notificacion_enviada=False)

        if not escritos_a_notificar.exists():
            self.stdout.write(self.style.SUCCESS('No hay nuevos escritos para notificar.'))
            return

        # 2. Obtener todos los usuarios que recibirán la notificación.
        usuarios = User.objects.all()

        for escrito in escritos_a_notificar:
            self.stdout.write(f'Procesando escrito: "{escrito.titulo}"...')

            # 3. Preparar el contenido del email.
            # Usamos un template para que sea más fácil de mantener.
            # (Crearemos este template en el siguiente paso)
            contexto_email = {
                'titulo_escrito': escrito.titulo,
                'nombre_autor': escrito.autor.username,
                # Podrías añadir una URL completa si tienes configurado el dominio
                # 'url_escrito': escrito.get_absolute_url() 
            }
            asunto = f"Nuevo artículo de {escrito.autor.username}: {escrito.titulo}"
            
            # Renderizamos un template HTML para el cuerpo del correo
            # html_mensaje = render_to_string('emails/notificacion_nuevo_escrito.html', contexto_email)
            # Creamos una versión en texto plano para clientes de correo que no soportan HTML
            # texto_plano_mensaje = strip_tags(html_mensaje)
            
            # Por simplicidad ahora, usaremos un texto simple.
            mensaje = f'{escrito.autor.username} ha publicado un nuevo artículo: "{escrito.titulo}"'

            # 4. Filtrar y enviar emails.
            destinatarios = [user.email for user in usuarios if user.email and user.id != escrito.autor.id]
            
            if destinatarios:
                try:
                    send_mail(
                        asunto,
                        mensaje,
                        'notificaciones@tallerescritura.com', # Remitente
                        destinatarios,
                        fail_silently=False,
                    )
                    self.stdout.write(self.style.SUCCESS(f'  > Notificaciones enviadas a {len(destinatarios)} usuarios.'))
                    
                    # 5. Marcar el escrito como notificado para no volver a enviarlo.
                    escrito.notificacion_enviada = True
                    escrito.save()

                except Exception as e:
                    self.stdout.write(self.style.ERROR(f'  > Error al enviar notificaciones para "{escrito.titulo}": {e}'))
            else:
                self.stdout.write(self.style.WARNING(f'  > No hay destinatarios para notificar sobre "{escrito.titulo}".'))
                # Aunque no haya destinatarios, lo marcamos como procesado.
                escrito.notificacion_enviada = True
                escrito.save()

        self.stdout.write(self.style.SUCCESS('Proceso de notificación completado.'))

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

## Archivo: `escritura/migrations/0005_comentario.py`

```python
# Generated by Django 5.2.3 on 2025-06-30 03:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("escritura", "0004_profile_mostrar_en_comunidad"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Comentario",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("texto", models.TextField(verbose_name="Texto del Comentario")),
                ("fecha_creacion", models.DateTimeField(auto_now_add=True)),
                (
                    "autor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comentarios",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "escrito",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comentarios",
                        to="escritura.escrito",
                    ),
                ),
            ],
            options={
                "verbose_name": "Comentario",
                "verbose_name_plural": "Comentarios",
                "ordering": ["fecha_creacion"],
            },
        ),
    ]

```

---

## Archivo: `escritura/migrations/0006_escrito_notificacion_enviada.py`

```python
# Generated by Django 5.2.3 on 2025-07-25 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escritura', '0005_comentario'),
    ]

    operations = [
        migrations.AddField(
            model_name='escrito',
            name='notificacion_enviada',
            field=models.BooleanField(default=False, verbose_name='Notificación Enviada'),
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
    
{# AÑADIR este bloque en detalle_escrito.html #}

<hr class="section-divider">

<div class="comments-section">
    <h2 class="section-title">Comentarios ({{ comentarios.count }})</h2>

    {# Formulario para añadir un nuevo comentario #}
    {% if user.is_authenticated %}
        <div class="comment-form-container">
            <form method="post">
                {% csrf_token %}
                {{ comentario_form.as_p }}
                <button type="submit" class="button primary small-button">Publicar Comentario</button>
            </form>
        </div>
    {% else %}
        <p class="login-prompt">
            <a href="{% url 'login' %}?next={{ request.path }}">Inicia sesión</a> para dejar un comentario.
        </p>
    {% endif %}

    {# Lista de comentarios existentes #}
    <div class="comment-list">
        {% for comentario in comentarios %}
            <div class="comment-item">
                <div class="comment-author-header">
                    <img src="{{ comentario.autor.profile.foto_perfil.url }}" alt="Foto de {{ comentario.autor.username }}" class="author-pic-small">
                    <div class="author-info">
                        <span class="comment-author-name">{{ comentario.autor.username }}</span>
                        <span class="comment-date">{{ comentario.fecha_creacion|date:"d M Y, H:i" }}</span>
                    </div>
                </div>
                <p class="comment-text">{{ comentario.texto|linebreaksbr }}</p>
            </div>
        {% empty %}
            <p>Aún no hay comentarios. ¡Sé el primero en opinar!</p>
        {% endfor %}
    </div>
</div>

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
    <form method="post" enctype="multipart/form-data" class="form-container">
        {% csrf_token %}

        <fieldset>
            <legend>Información de la Cuenta</legend>
            <div class="form-field">
                {{ user_form.email.label_tag }}
                {{ user_form.email }}
                {{ user_form.email.errors }}
            </div>
            <div class="form-field">
                {{ user_form.first_name.label_tag }}
                {{ user_form.first_name }}
                {{ user_form.first_name.errors }}
            </div>
            <div class="form-field">
                {{ user_form.last_name.label_tag }}
                {{ user_form.last_name }}
                {{ user_form.last_name.errors }}
            </div>
            <div class="form-field">
                {{ profile_form.bio.label_tag }}
                {{ profile_form.bio }}
                {{ profile_form.bio.errors }}
            </div>
        </fieldset>

        <fieldset>
            <legend>Foto de Perfil</legend>
            <div class="form-field">
                {{ profile_form.foto_perfil.label_tag }}
                {{ profile_form.foto_perfil }}
                {{ profile_form.foto_perfil.errors }}
            </div>
        </fieldset>

        <fieldset>
            <legend>Configuración de Privacidad</legend>
            <div class="form-field checkbox-field">
                {{ profile_form.mostrar_en_comunidad }}
                {{ profile_form.mostrar_en_comunidad.label_tag }}
                <small class="help-text">{{ profile_form.mostrar_en_comunidad.help_text }}</small>
                {{ profile_form.mostrar_en_comunidad.errors }}
            </div>
        </fieldset>

        <div class="form-actions">
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
                    <a href="{% url 'escritura:perfil_publico' user_id=perfil.user.id %}" class="user-card-link">
                        <img src="{{ perfil.foto_perfil.url }}" alt="Foto de {{ perfil.user.username }}" class="user-card-img">
                        <h3 class="user-card-name">{{ perfil.user.username }}</h3>
                        {% if perfil.bio %}
                            <p class="user-card-bio">"{{ perfil.bio|truncatewords:15 }}"</p>
                        {% endif %}
                    </a>
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
{% extends 'base.html' %} {# Extiende la plantilla base #}

{% block title %}Lista de Escritos Públicos{% endblock %} {# Define el título específico para esta página #}

{% block content %} {# Este contenido se insertará en el bloque 'content' de base.html #}
    <h1 class="page-title">Escritos Públicos del Taller</h1>

    {% if escritos %}
        <ul class="escrito-list">
            {% for escrito in escritos %}
                <li class="escrito-item">

                    <div class="escrito-card-header">
                        <div class="header-author-info">
                            {% if escrito.autor.profile and escrito.autor.profile.foto_perfil %}
                                <img class="author-pic" src="{{ escrito.autor.profile.foto_perfil.url }}" alt="Foto de {{ escrito.autor.username }}">
                            {% endif %}
                            <span class="author-name">{{ escrito.autor.username }}</span>
                        </div>
                        <div class="header-title-actions">
                            <h2 class="escrito-title"><a href="{% url 'escritura:detalle_escrito' pk=escrito.pk %}">{{ escrito.titulo }}</a></h2>
                        </div>
                    </div>

                    <div class="escrito-content" id="escrito-content-{{ escrito.pk }}">
                        {{ escrito.contenido|safe }}
                    </div>

                    <div class="escrito-footer">
                        <div class="escrito-meta">
                            <p>Publicado el: {{ escrito.fecha_creacion|date:"d M Y H:i" }}</p>
                        </div>
                        
                        <!-- Contenedor Unificado para todas las acciones -->
                        <div class="card-actions-container">
                            <button
                                class="toggle-button"
                                aria-expanded="false"
                                aria-controls="escrito-content-{{ escrito.pk }}"
                                title="Expandir/Contraer"
                            >
                            </button>
                        </div>
                    </div>
                </li>
            {% endfor %}
        </ul>
    {% else %}
        <p>No hay escritos públicos disponibles en este momento.</p>
    {% endif %}
{% endblock %}```
```

---

## Archivo: `escritura/templates/escritura/perfil_publico.html`

```html
{# escritura/templates/escritura/perfil_publico.html #}
{% extends 'base.html' %}
{% load static %}

{% block title %}Perfil de {{ usuario_perfil.username }}{% endblock %}

{% block content %}
    <div class="profile-header">
        {% if usuario_perfil.profile and usuario_perfil.profile.foto_perfil %}
            <img src="{{ usuario_perfil.profile.foto_perfil.url }}" alt="Foto de perfil de {{ usuario_perfil.username }}" class="profile-pic">
        {% endif %}
        <h1 class="page-title">{{ usuario_perfil.username }}</h1>
        <p class="profile-bio">
            {% if usuario_perfil.profile.bio %}
                {{ usuario_perfil.profile.bio }}
            {% else %}
                Este autor aún no ha añadido una biografía.
            {% endif %}
        </p>
    </div>

    <hr> {# Separador visual #}

    <h2 class="section-title">Escritos Públicos de {{ usuario_perfil.username }}</h2>

    {% if escritos %}
        <ul class="escrito-list">
            {% for escrito in escritos %}
                <li class="escrito-item">

                    <div class="escrito-card-header">
                        <div class="header-author-info">
                            {% if escrito.autor.profile and escrito.autor.profile.foto_perfil %}
                                <img class="author-pic" src="{{ escrito.autor.profile.foto_perfil.url }}" alt="Foto de {{ escrito.autor.username }}">
                            {% endif %}
                            <span class="author-name">{{ escrito.autor.username }}</span>
                        </div>
                        <div class="header-title-actions">
                            <h2 class="escrito-title"><a href="{% url 'escritura:detalle_escrito' pk=escrito.pk %}">{{ escrito.titulo }}</a></h2>
                        </div>
                    </div>

                    <div class="escrito-content" id="escrito-content-perfil-{{ escrito.pk }}">
                        {{ escrito.contenido|safe }}
                    </div>

                    <div class="escrito-footer">
                        <div class="escrito-meta">
                            <p>Publicado el: {{ escrito.fecha_creacion|date:"d M Y H:i" }}</p>
                        </div>
                        
                        <!-- Contenedor Unificado para todas las acciones -->
                        <div class="card-actions-container">
                            <span class="escrito-status status-{{ escrito.estado|lower }}">{{ escrito.get_estado_display }}</span>
                            <button
                                class="toggle-button"
                                aria-expanded="false"
                                aria-controls="escrito-content-perfil-{{ escrito.pk }}"
                                title="Expandir/Contraer"
                            >
                            </button>
                        </div>
                    </div>
                </li>
            {% endfor %}
        </ul>
    {% else %}
        <p>Este autor aún no ha publicado ningún escrito.</p>
    {% endif %}

{% endblock %}
```

---

## Archivo: `escritura/templates/escritura/perfil_usuario.html`

```html
{# escritura/templates/escritura/perfil_usuario.html #}
{% extends 'base.html' %}
{% load static %}

{% block title %}Perfil de {{ usuario.username }}{% endblock %}

{% block content %}
    <div class="profile-header">
        {% if perfil and perfil.foto_perfil %}
            <img src="{{ perfil.foto_perfil.url }}" alt="Foto de perfil de {{ usuario.username }}" class="profile-pic">
        {% endif %}
        <h1 class="page-title">{{ usuario.username }}</h1>
        <p class="profile-bio">
            {% if perfil.bio %}
                {{ perfil.bio }}
            {% else %}
                Aún no has añadido una biografía.
            {% endif %}
        </p>
        <a href="{% url 'escritura:editar_perfil' %}" class="button secondary">Editar Perfil</a>
    </div>

    <hr> {# Separador visual #}

    <h2 class="section-title">Mis Escritos</h2>

    {% if mis_escritos %}
        <ul class="escrito-list">
            {% for escrito in mis_escritos %}
                <li class="escrito-item">

                    <div class="escrito-card-header">
                        <div class="header-author-info">
                            {% if escrito.autor.profile and escrito.autor.profile.foto_perfil %}
                                <img class="author-pic" src="{{ escrito.autor.profile.foto_perfil.url }}" alt="Foto de {{ escrito.autor.username }}">
                            {% endif %}
                            <span class="author-name">{{ escrito.autor.username }}</span>
                        </div>
                        <div class="header-title-actions">
                            <h2 class="escrito-title"><a href="{% url 'escritura:detalle_escrito' pk=escrito.pk %}">{{ escrito.titulo }}</a></h2>
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

                        <!-- Contenedor Unificado para todas las acciones -->
                        <div class="card-actions-container">
                            <span class="escrito-status status-{{ escrito.estado|lower }}">{{ escrito.get_estado_display }}</span>
                            <a href="{% url 'escritura:editar_escrito' pk=escrito.pk %}" class="button warning small-button">Editar</a>
                            <a href="{% url 'escritura:eliminar_escrito' pk=escrito.pk %}" class="button danger small-button">Eliminar</a>
                            <button
                                class="toggle-button"
                                aria-expanded="false"
                                aria-controls="escrito-content-perfil-{{ escrito.pk }}"
                                title="Expandir/Contraer"
                            >
                            </button>
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
    position: relative; /* Contexto de posicionamiento por si se necesitan insignias, etc. */
}

.escrito-card-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    gap: 15px;
    margin-bottom: 15px;
}

.header-author-info {
    display: flex;
    align-items: center;
    gap: 10px;
    min-width: 0;
}

.header-title-actions {
    display: flex;
    align-items: flex-start;
    gap: 15px;
}

.author-pic {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    object-fit: cover;
    border: 2px solid #E8D8C9;
    flex-shrink: 0;
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
    margin: 0;
    font-family: 'Playfair Display', serif;
    color: #AA775A;
    white-space: normal;
    word-wrap: break-word;
    overflow-wrap: break-word;
    overflow: visible;
    text-overflow: clip;
    flex-grow: 1; /* Permite que el título ocupe el espacio sobrante en la cabecera */
}

.escrito-title a {
    text-decoration: none;
    color: inherit;
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
    flex-shrink: 0; /* Evita que el botón se encoja */
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
    justify-content: space-between; /* <-- CLAVE: Empuja la meta-info y las acciones a los extremos */
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

/* Contenedor unificado para botones de acción en el footer */
.card-actions-container {
    display: flex;
    align-items: center;
    gap: 10px; /* Espacio entre los botones y/o el estado */
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

.nav-link-button {
    background: none;
    border: none;
    padding: 0;
    margin: 0;
    cursor: pointer;
    font-family: inherit;
    color: white;
    text-decoration: none;
    font-weight: bold;
    font-size: 1em;
}

.nav-link-button:hover {
    text-decoration: underline;
}

/* --- Estilos para la Sección de Comentarios --- */

.section-divider {
    border: none;
    border-top: 1px solid #E8D8C9;
    margin: 40px 0;
}

.comments-section .section-title {
    text-align: left;
    font-size: 1.8em;
    margin-bottom: 20px;
}

.comment-form-container {
    margin-bottom: 30px;
    background-color: #F5EFE6;
    padding: 15px;
    border-radius: 8px;
}

.comment-form-container textarea {
    min-height: 80px;
    width: 100%;
    margin-bottom: 10px;
}

.login-prompt {
    text-align: center;
    padding: 20px;
    background-color: #F5EFE6;
    border-radius: 8px;
    margin-bottom: 30px;
}

.comment-list {
    display: flex;
    flex-direction: column;
    gap: 20px;
}

.comment-item {
    background-color: #FAF7F0;
    border: 1px solid #E8D8C9;
    padding: 15px;
    border-radius: 8px;
}

.comment-author-header {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 10px;
}

.author-pic-small {
    width: 35px;
    height: 35px;
    border-radius: 50%;
    object-fit: cover;
}

.comment-author-name {
    font-weight: bold;
    color: #333;
}

.comment-date {
    font-size: 0.8em;
    color: #6B4F4F;
}

.comment-text {
    color: #333;
    line-height: 1.6;
    margin: 0;
}
```

---

## Archivo: `static/js/main.js`

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

## Archivo: `taller_escritura/local_settings.py`

```python
# taller_escritura/local_settings.py
# Configuraciones para el entorno de desarrollo local.

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# MODO DEBUG ACTIVADO PARA DESARROLLO
DEBUG = True

# Permitir acceso desde el localhost
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# BASE DE DATOS LOCAL (SQLITE)
# Se usará un archivo db.sqlite3 en la raíz del proyecto.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# La clave secreta puede ser menos segura en desarrollo
SECRET_KEY = 'django-insecure-local-development-key'

```

---

## Archivo: `taller_escritura/settings.py`

```python
# taller_escritura/settings.py
# VERSIÓN FINAL AUTOSUFICIENTE PARA PYTHONANYWHERE

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# --- CONFIGURACIÓN DE PRODUCCIÓN FIJA ---

# MODIFICADO: Clave secreta segura y única para tu proyecto.
SECRET_KEY = 'django-insecure-z$)w!f-u8h#@b(m9_v2&n$q6+c=p*j^x7s5k!t1l@y_e)o-r'

# DEBUG debe ser False en producción por seguridad.
DEBUG = False

# MODIFICADO: Host permitido para tu aplicación.
ALLOWED_HOSTS = ['devivan.pythonanywhere.com']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'escritura',
    'ckeditor',
    'ckeditor_uploader',
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

ROOT_URLCONF = 'taller_escritura.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'taller_escritura/templates'],
        'APP_DIRS': True,
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

# --- BASE DE DATOS DE PRODUCCIÓN (MYSQL EN PYTHONANYWHERE) ---
# MODIFICADO: Rellenado con las credenciales exactas de tu cuenta de PythonAnywhere.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'DevIvan$db_taller_escritura',
        'USER': 'DevIvan',
        'PASSWORD': 'sql159753', # AÑADIDA: Tu contraseña de la base de datos.
        'HOST': 'DevIvan.mysql.pythonanywhere-services.com',
        'PORT': '3306',
    }
}


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'es-es'
TIME_ZONE = 'America/Mexico_City'
USE_I18N = True
USE_TZ = True

# Static & Media files
# Rutas para que PythonAnywhere encuentre tus archivos estáticos y de medios
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# AÑADIDO: Directorio estático principal para desarrollo
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Configuración de Almacenamiento Simplificada
STORAGES = {
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
LOGIN_REDIRECT_URL = 'escritura:lista_escritos'
LOGOUT_REDIRECT_URL = 'escritura:lista_escritos'

# CKEditor Configuración
CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline', 'Strike', '-', 'Subscript', 'Superscript'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', 'Blockquote', 'CreateDiv'],
            ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink', 'Anchor'],
            ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak'],
            ['Styles', 'Format', 'Font', 'FontSize'],
            ['TextColor', 'BGColor'],
            ['Maximize', 'ShowBlocks', '-', 'About'],
            ['Source']
        ],
        'width': '100%',
        'height': 300,
        'extraPlugins': 'codesnippet',
    }
}

# --- CONFIGURACIÓN DE DESARROLLO (SOBREESCRIBE SI ES NECESARIO) ---
# Intenta importar la configuración local. Este archivo no debe estar en el control de versiones.
try:
    from .local_settings import *
except ImportError:
    pass

# --- EMAIL CONFIGURATION (for development) ---
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'notificaciones@tallerescritura.com'
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
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
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
                <a href="{% url 'home' %}">Taller de Escritura de Cálamo y Papiro</a>
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

## Lista de Archivos Omitidos por Tamaño Excesivo

Ninguno.
