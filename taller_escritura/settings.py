# taller_escritura/settings.py
# VERSIÓN FINAL Y ROBUSTA v2 PARA DEPURACIÓN EN RAILWAY

import os
from pathlib import Path
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# --- Variables de Entorno y Depuración ---
# Leemos la SECRET_KEY directamente de las variables de entorno.
# Si no existe, la app fallará en el arranque, lo cual es bueno porque nos obliga a configurarla.
SECRET_KEY = os.environ.get('SECRET_KEY')

# DEBUG siempre es False en producción.
DEBUG = False

# El '*' es una configuración de "confianza en el proxy". En plataformas como Railway,
# que gestionan el enrutamiento a través de un proxy, esto es una configuración común y segura.
# Elimina la posibilidad de un error 400 por un dominio mal configurado.
ALLOWED_HOSTS = ['*']

# --- IMPRESIONES PARA DEPURACIÓN EN LOS LOGS DE RAILWAY ---
# Estos prints nos ayudarán a verificar si las variables de entorno se están cargando correctamente.
print("--- SETTINGS.PY LOGS ---")
print(f"SECRET_KEY loaded: {'Yes' if SECRET_KEY else 'No, CRITICAL ERROR!'}")
print(f"DATABASE_URL loaded: {'Yes' if os.environ.get('DATABASE_URL') else 'No, this is normal during build, but should be Yes in runtime.'}")
print(f"ALLOWED_HOSTS set to: {ALLOWED_HOSTS}")
print("------------------------")

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic', # Necesario para que WhiteNoise funcione en desarrollo (aunque DEBUG es False)
    'django.contrib.staticfiles',
    # Tu aplicación
    'escritura',
    # Apps de terceros
    'ckeditor',
    'ckeditor_uploader',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # WhiteNoise debe ir aquí.
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

# --- Base de Datos (Configuración Robusta para Build vs. Runtime) ---
DATABASE_URL = os.environ.get('DATABASE_URL')

if DATABASE_URL:
    # Si DATABASE_URL existe (en la fase 'web' de ejecución), la usamos.
    DATABASES = {'default': dj_database_url.config(conn_max_age=600, ssl_require=False)}
else:
    # Si no (en la fase de 'release'/'build'), usamos una SQLite en memoria.
    # Esto permite que comandos como `collectstatic` se ejecuten sin necesitar la DB real.
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:',
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
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# WhiteNoise Storage
STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# Default primary key
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Auth URLs
LOGIN_REDIRECT_URL = 'escritura:lista_escritos'
LOGOUT_REDIRECT_URL = 'escritura:lista_escritos'

# CKEditor
CKEDITOR_UPLOAD_PATH = 'uploads/'
# (La configuración de CKEDITOR_CONFIGS se puede omitir si el default es suficiente)
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