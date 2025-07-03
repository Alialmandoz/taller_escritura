# taller_escritura/settings.py

import os
import dj_database_url
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# --- CONFIGURACIÓN DE PRODUCCIÓN ---
# Usamos os.environ.get() para leer variables de entorno.
# Esto nos permite tener configuraciones diferentes en desarrollo y producción
# sin tener que cambiar el código.
# El segundo argumento es un valor por defecto que se usará si la variable de entorno no existe.

# SECRET_KEY: Crítica para la seguridad. En producción, DEBE ser leída desde una variable de entorno.
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-@e^$b!8n*5s15x_p2j9!%h^b-z53%^v^#o7*g8y-n0%k(t19h+')

# DEBUG: En producción, DEBE ser False. Lo controlamos con una variable de entorno.
# El 'False' como string es importante porque las variables de entorno son siempre strings.
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# ALLOWED_HOSTS: En producción, aquí van los dominios de tu sitio.
# Railway nos dará una URL que pondremos en una variable de entorno.
# El .split(',') permite definir varios hosts separados por comas.
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '127.0.0.1,localhost').split(',')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Tu aplicación
    'escritura',
    # Apps de terceros
    'ckeditor',
    'ckeditor_uploader',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # AÑADIDO: Whitenoise para servir archivos estáticos eficientemente.
    # Debe ir justo después de SecurityMiddleware.
    'whitenoise.middleware.WhiteNoiseMiddleware',
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


# --- CONFIGURACIÓN DE LA BASE DE DATOS ---
# Usamos dj_database_url para leer la variable de entorno DATABASE_URL que Railway nos proporcionará.
# Esta variable contiene toda la información de conexión a la base de datos PostgreSQL.
# Si no la encuentra (como en nuestro entorno local), usará la base de datos SQLite por defecto.
DATABASES = {
    'default': dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
        conn_max_age=600 # Mantiene las conexiones abiertas por 600 segundos para mayor eficiencia.
    )
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

LANGUAGE_CODE = 'es-es'
TIME_ZONE = 'America/Mexico_City'
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
# Directorio donde tu app buscará archivos estáticos adicionales (proyecto-wide).
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
# AÑADIDO: Directorio donde `collectstatic` juntará todos los archivos estáticos para producción.
STATIC_ROOT = BASE_DIR / 'staticfiles'

# AÑADIDO: Configuración de almacenamiento para WhiteNoise.
# Optimiza los archivos estáticos (comprimiéndolos y cacheándolos eficientemente).
STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# Media files (Archivos subidos por los usuarios, como fotos de perfil)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# --- URLs DE AUTENTICACIÓN ---
LOGIN_REDIRECT_URL = 'escritura:lista_escritos'
LOGOUT_REDIRECT_URL = 'escritura:lista_escritos'


# --- CONFIGURACIÓN DE CKEDITOR ---
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