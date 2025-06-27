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