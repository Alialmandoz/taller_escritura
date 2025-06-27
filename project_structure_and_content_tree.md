# Contenido del Proyecto: taller escritura

**Generado el:** 2025-06-26 23:10:23

## Estructura del Proyecto

```text
taller escritura
├── .gitignore
├── Beige Ivory Watercolor Minimalist Productivity New Blog Instagram Post.png
├── manage.py
├── escritura
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── __init__.py
│   ├── templates
│   │   ├── escritura
│   │   │   ├── detalle_escrito.html
│   │   │   ├── lista_escritos.html
├── taller_escritura
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
```

---

## Archivo: `.gitignore`

[Contenido de '.gitignore' omitido (Extensión no listada: )]

## Archivo: `Beige Ivory Watercolor Minimalist Productivity New Blog Instagram Post.png`

[Contenido de 'Beige Ivory Watercolor Minimalist Productivity New Blog Instagram Post.png' omitido (Extensión no listada: .png)]

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

## Archivo: `escritura/__init__.py`

```python

```

---

## Archivo: `escritura/admin.py`

```python
# escritura/admin.py

from django.contrib import admin
from .models import Escrito # AÑADIDO: Importamos nuestro modelo 'Escrito'.
                             # Es crucial importar el modelo que deseas registrar.

# Register your models here.

# AÑADIDO: Registramos el modelo Escrito en el panel de administración de Django.
# Esto genera automáticamente una interfaz CRUD (Crear, Leer, Actualizar, Borrar)
# para tus objetos Escrito, permitiendo una gestión sencilla desde el navegador.
admin.site.register(Escrito)
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

## Archivo: `escritura/models.py`

```python
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

from django.urls import path
from . import views # Importamos el módulo views de nuestra propia aplicación

# Definición del nombre de la aplicación para URL namespaces
# Es una buena práctica para evitar conflictos de nombres si tienes URLs con el mismo nombre en diferentes apps.
app_name = 'escritura'

urlpatterns = [
    # path(ruta_url, vista_a_llamar, name=nombre_para_referenciar_url)
    # path('', ...) significa la raíz de esta app (ej: /escritura/)
    path('', views.lista_escritos, name='lista_escritos'),

    # AÑADIDO: URL para el detalle de un escrito.
    # <int:pk> es un conversor de path que captura un número entero (la clave primaria del escrito)
    # y lo pasa como argumento 'pk' a la vista DetalleEscrito.
    # .as_view() se usa para llamar vistas basadas en clase.
    path('<int:pk>/', views.DetalleEscrito.as_view(), name='detalle_escrito'),
]
```

---

## Archivo: `escritura/views.py`

```python
# escritura/views.py

from django.shortcuts import render, get_object_or_404 # Importamos get_object_or_404
from django.views.generic import DetailView           # AÑADIDO: Importamos DetailView de las CBV
from .models import Escrito                           # Importamos nuestro modelo Escrito

# AÑADIDO: Vista basada en función para listar escritos públicos
def lista_escritos(request):
    """
    Esta vista recupera todos los objetos Escrito cuyo estado sea 'PUBLICO'
    y los pasa a la plantilla para su visualización.
    """
    escritos = Escrito.objects.filter(estado='PUBLICO').order_by('-fecha_creacion')
    contexto = {
        'escritos': escritos
    }
    return render(request, 'escritura/lista_escritos.html', contexto)

# AÑADIDO: Vista basada en clase para mostrar el detalle de un escrito
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

## Archivo: `escritura/migrations/__init__.py`

```python

```

---

## Archivo: `escritura/templates/escritura/detalle_escrito.html`

```html
<!-- escritura/templates/escritura/detalle_escrito.html -->
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ escrito.titulo }} - Detalle del Escrito</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            background-color: #f4f4f4;
            color: #333;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            background-color: #fff;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        }
        h1 {
            color: #0056b3;
            margin-bottom: 10px;
        }
        .meta-info {
            font-size: 0.9em;
            color: #666;
            margin-bottom: 20px;
            border-bottom: 1px solid #eee;
            padding-bottom: 10px;
        }
        .content {
            line-height: 1.8;
            color: #444;
            white-space: pre-wrap; /* Mantiene saltos de línea y espacios del TextField */
        }
        .back-link {
            display: block;
            margin-top: 30px;
            text-decoration: none;
            color: #007bff;
            font-weight: bold;
        }
        .back-link:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>{{ escrito.titulo }}</h1> {# Muestra el título del escrito #}
        <p class="meta-info">
            Por: {{ escrito.autor.username }} | 
            Publicado el: {{ escrito.fecha_creacion|date:"d M Y H:i" }} |
            Última actualización: {{ escrito.fecha_actualizacion|date:"d M Y H:i" }}
        </p>
        <div class="content">
            {# Muestra el contenido completo del escrito #}
            {# Considerar la integración de un editor de texto enriquecido aquí en el futuro #}
            <p>{{ escrito.contenido }}</p> 
        </div>
        
        {# AÑADIDO: Enlace para volver a la lista de escritos #}
        {# La etiqueta {% url %} es la mejor manera de crear enlaces dinámicos en Django. #}
        {# 'escritura:lista_escritos' usa el namespace 'escritura' y el nombre de la URL 'lista_escritos'. #}
        <a href="{% url 'escritura:lista_escritos' %}" class="back-link">&larr; Volver a la lista de escritos</a>
    </div>
</body>
</html>
```

---

## Archivo: `escritura/templates/escritura/lista_escritos.html`

```html
<!-- escritura/templates/escritura/lista_escritos.html -->
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lista de Escritos del Taller</title>
    <style>
        /* CSS básico para hacer la página un poco más legible */
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            background-color: #f4f4f4;
            color: #333;
        }
        h1 {
            color: #0056b3;
        }
        .escrito-list {
            list-style: none;
            padding: 0;
        }
        .escrito-item {
            background-color: #fff;
            margin-bottom: 15px;
            padding: 15px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        .escrito-item h2 {
            margin-top: 0;
            color: #007bff;
        }
        /* AÑADIDO: Estilo para los enlaces de título */
        .escrito-item h2 a {
            text-decoration: none; /* Quita el subrayado predeterminado */
            color: #007bff; /* Color azul para el enlace */
        }
        .escrito-item h2 a:hover {
            text-decoration: underline; /* Subrayado al pasar el ratón */
        }
        .escrito-item p {
            line-height: 1.6;
        }
        .escrito-meta {
            font-size: 0.9em;
            color: #666;
            margin-top: 10px;
            border-top: 1px solid #eee;
            padding-top: 10px;
        }
    </style>
</head>
<body>
    <h1>Escritos Públicos del Taller</h1>

    {% if escritos %} {# Si la lista de escritos no está vacía... #}
        <ul class="escrito-list">
            {# Bucle para iterar sobre cada escrito en la lista 'escritos' #}
            {% for escrito in escritos %}
                <li class="escrito-item">
                    {# MODIFICADO: El título ahora es un enlace al detalle del escrito. #}
                    {# La etiqueta {% url %} genera la URL dinámicamente usando el nombre 'escritura:detalle_escrito' #}
                    {# y le pasa el 'pk' (clave primaria) del escrito actual como argumento. #}
                    <h2><a href="{% url 'escritura:detalle_escrito' pk=escrito.pk %}">{{ escrito.titulo }}</a></h2>
                    {# slice de contenido para mostrar solo una parte #}
                    <p>{{ escrito.contenido|truncatechars:200 }}</p> 
                    <div class="escrito-meta">
                        <p>Por: {{ escrito.autor.username }}</p> {# Muestra el nombre de usuario del autor #}
                        <p>Publicado el: {{ escrito.fecha_creacion|date:"d M Y H:i" }}</p> {# Formato de fecha #}
                    </div>
                </li>
            {% endfor %}
        </ul>
    {% else %} {# Si no hay escritos, muestra un mensaje #}
        <p>No hay escritos públicos disponibles en este momento.</p>
    {% endif %}
</body>
</html>
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
        'DIRS': [], # Puedes añadir rutas a directorios de plantillas globales aquí.
                    # Por ahora, Django buscará plantillas dentro de cada app en una carpeta 'templates'.
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

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField' # Tipo de campo predeterminado para claves primarias automáticas.
```

---

## Archivo: `taller_escritura/urls.py`

```python
from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('escritura/', include('escritura.urls')),
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

## Lista de Archivos con Contenido Omitido

*(Binarios, errores de codificación/lectura, o errores inesperados durante el procesamiento)*

- `.gitignore (Extensión no listada)`
- `Beige Ivory Watercolor Minimalist Productivity New Blog Instagram Post.png (Extensión no listada)`

## Lista de Archivos Omitidos por Tamaño Excesivo

Ninguno.
