# Contenido del Proyecto: taller escritura

**Generado el:** 2025-06-26 23:59:53

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
│   │   │   ├── crear_editar_escrito.html
│   │   │   ├── detalle_escrito.html
│   │   │   ├── lista_escritos.html
│   │   │   ├── registro.html
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
from django.contrib.auth.forms import UserCreationForm # Importamos el formulario de creación de usuarios de Django
from .models import Escrito #  Importamos nuestro modelo Escrito


# Formulario personalizado para el registro de usuarios
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

# Formulario para crear y editar objetos Escrito
class EscritoForm(forms.ModelForm):
    """
    Formulario basado en el modelo Escrito para crear y editar textos.
    """
    class Meta:
        model = Escrito # Le decimos a Django que este formulario está basado en el modelo Escrito.
        # Definimos los campos del modelo Escrito que queremos incluir en el formulario.
        # Excluimos 'autor', 'fecha_creacion' y 'fecha_actualizacion' porque
        # se gestionarán automáticamente en la vista.
        fields = ['titulo', 'contenido', 'estado'] 
        
        # Opcional: Puedes personalizar las etiquetas o widgets de los campos.
        labels = {
            'titulo': 'Título del Escrito',
            'contenido': 'Contenido del Texto',
            'estado': 'Visibilidad',
        }
        # widgets = {
        #     'contenido': forms.Textarea(attrs={'cols': 80, 'rows': 15}),
        # }
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
    path('accounts/', include('django.contrib.auth.urls')),
]
```

---

## Archivo: `escritura/views.py`

```python
# escritura/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required # AÑADIDO: Decorador para requerir autenticación

from .models import Escrito
from .forms import CustomUserCreationForm, EscritoForm # MODIFICADO: Importamos también EscritoForm


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
    
# AÑADIDO: Vista para el registro de nuevos usuarios
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
            # AÑADIDO: No guardamos el formulario directamente todavía (commit=False)
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

## Archivo: `escritura/templates/escritura/crear_editar_escrito.html`

```html
<!-- escritura/templates/escritura/crear_editar_escrito.html -->
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% if es_creacion %}Crear Nuevo Escrito{% else %}Editar Escrito{% endif %}</title>
    <style>
        /* Reutiliza estilos de formularios previos para consistencia */
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            background-color: #f4f4f4;
            color: #333;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 80vh;
        }
        .container {
            background-color: #fff;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
            width: 100%;
            max-width: 700px; /* Un poco más ancho para el contenido */
            box-sizing: border-box;
        }
        h1 {
            color: #0056b3;
            text-align: center;
            margin-bottom: 20px;
        }
        form {
            display: flex;
            flex-direction: column;
        }
        p { /* Estilo para cada campo del formulario renderizado por Django */
            margin-bottom: 15px;
        }
        p label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        input[type="text"],
        select, /* Estilo para el campo 'estado' que es un select */
        textarea { /* Estilo para el campo 'contenido' que será un textarea */
            width: 100%;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
            box-sizing: border-box;
            font-family: Arial, sans-serif; /* Asegurar fuente consistente */
        }
        textarea {
            resize: vertical; /* Permite redimensionar verticalmente */
            min-height: 200px; /* Altura mínima para el área de texto */
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
            color: #666;
            margin-top: 5px;
        }
        button {
            background-color: #007bff;
            color: white;
            padding: 12px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 1.1em;
            margin-top: 20px;
        }
        button:hover {
            background-color: #0056b3;
        }
        .back-link {
            display: block;
            margin-top: 20px;
            text-align: center;
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
        <h1>{% if es_creacion %}Crear Nuevo Escrito{% else %}Editar Escrito{% endif %}</h1>
        <form method="post">
            {% csrf_token %} {# ¡CRÍTICO para la seguridad! #}
            {{ form.as_p }} 
            <button type="submit">
                {% if es_creacion %}Publicar Escrito{% else %}Guardar Cambios{% endif %}
            </button>
        </form>
        <a href="{% url 'escritura:lista_escritos' %}" class="back-link">&larr; Volver a la lista de escritos</a>
    </div>
</body>
</html>
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
    <div class="auth-links">
        {% if user.is_authenticated %}
            <span class="welcome-message">Hola, {{ user.username }}!</span>
            <a href="{% url 'logout' %}">Cerrar Sesión</a>
        {% else %}
            <a href="{% url 'login' %}">Inicia sesión aquí</a>
            <a href="{% url 'escritura:registro' %}">Registrarse</a>
        {% endif %}
    </div>

    {# AÑADIDO: Enlace para crear un nuevo escrito (solo visible si el usuario está autenticado) #}
    {% if user.is_authenticated %}
        <div style="text-align: right; margin-bottom: 20px;">
            <a href="{% url 'escritura:crear_escrito' %}" style="background-color: #28a745; color: white; padding: 8px 15px; border-radius: 5px; text-decoration: none; font-weight: bold;">+ Crear Nuevo Escrito</a>
        </div>
    {% endif %}

    <h1>Escritos Públicos del Taller</h1>

    {% if escritos %}
        <!-- ... tu lista de escritos existente ... -->
    {% else %}
        <p>No hay escritos públicos disponibles en este momento.</p>
    {% endif %}
</body>
</html>
```

---

## Archivo: `escritura/templates/escritura/registro.html`

```html
<!-- escritura/templates/escritura/registro.html -->
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registro de Usuario</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            background-color: #f4f4f4;
            color: #333;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 80vh;
        }
        .container {
            background-color: #fff;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
            width: 100%;
            max-width: 400px;
            box-sizing: border-box;
        }
        h1 {
            color: #0056b3;
            text-align: center;
            margin-bottom: 20px;
        }
        form {
            display: flex;
            flex-direction: column;
        }
        p { /* Estilo para cada campo del formulario renderizado por Django */
            margin-bottom: 15px;
        }
        p label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        input[type="text"],
        input[type="password"],
        input[type="email"] {
            width: 100%;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
            box-sizing: border-box; /* Incluye padding y borde en el ancho total */
        }
        ul.errorlist { /* Estilo para la lista de errores del formulario */
            color: red;
            list-style-type: none;
            padding-left: 0;
            margin-top: 5px;
            font-size: 0.9em;
        }
        .helptext { /* Estilo para el texto de ayuda de Django Forms */
            font-size: 0.8em;
            color: #666;
            margin-top: 5px;
        }
        button {
            background-color: #007bff;
            color: white;
            padding: 12px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 1.1em;
            margin-top: 20px;
        }
        button:hover {
            background-color: #0056b3;
        }
        .login-link {
            text-align: center;
            margin-top: 20px;
            font-size: 0.9em;
        }
        .login-link a {
            color: #007bff;
            text-decoration: none;
            font-weight: bold;
        }
        .login-link a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Registro</h1>
        <form method="post">
            {% csrf_token %} {# AÑADIDO: ¡MUY IMPORTANTE! Token de seguridad de Django #}
            {# Renderiza el formulario de Django como párrafos. Cada campo será un <p> con su label y input. #}
            {{ form.as_p }} 
            <button type="submit">Registrarse</button>
        </form>
        <div class="login-link">
            ¿Ya tienes una cuenta? <a href="#">Inicia sesión aquí</a> {# AÑADIDO: Placeholder para el enlace de login #}
        </div>
    </div>
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
