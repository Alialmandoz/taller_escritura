# taller_escritura/settings.py
# VERSIÓN SIMPLIFICADA PARA RAILWAY

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# --- Variables de Entorno (Leídas directamente de Railway) ---
# En producción, estas variables SIEMPRE deben existir.
SECRET_KEY = os.environ['SECRET_KEY']
DEBUG = False # En producción, DEBUG siempre es False.
ALLOWED_HOSTS = [os.environ['RAILWAY_PUBLIC_DOMAIN']] # Leemos directamente el dominio público de Railway.

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic', # Para servir estáticos con WhiteNoise
    'django.contrib.staticfiles',
    'escritura',
    'ckeditor',
    'ckeditor_uploader',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # WhiteNoise
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

# --- Base de Datos (Leída directamente de Railway) ---
import dj_database_url

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Un motor por defecto
        'NAME': 'dummy_db_for_build', # Un nombre cualquiera
    }
}

# Sobrescribe con la base de datos de producción si la URL está disponible
db_from_env = dj_database_url.config(conn_max_age=600)
if db_from_env:
    DATABASES['default'] = db_from_env

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