# taller_escritura/settings.py
# VERSIÓN ROBUSTA Y FLEXIBLE PARA DESARROLLO LOCAL Y PYTHONANYWHERE

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# --- La Clave de la Flexibilidad: La Variable de Entorno 'ENVIRONMENT' ---
# En PythonAnywhere, definiremos una variable de entorno llamada 'ENVIRONMENT' con el valor 'production'.
# Si esta variable no existe, asumiremos que estamos en desarrollo local.
IS_PRODUCTION = os.environ.get('ENVIRONMENT') == 'production'

if IS_PRODUCTION:
    # --- AJUSTES DE PRODUCCIÓN (PYTHONANYWHERE) ---
    # Estas variables las configuraremos en PythonAnywhere.
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DEBUG = False
    ALLOWED_HOSTS = [os.environ.get('ALLOWED_HOSTS')] # Ej: 'tu-usuario.pythonanywhere.com'
else:
    # --- AJUSTES DE DESARROLLO (LOCAL) ---
    SECRET_KEY = 'django-insecure-una-clave-local-que-no-importa-mucho'
    DEBUG = True
    ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'devivan.pythonanywhere.com']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'escritura',
    'ckeditor',
    'ckeditor_uploader',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
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

# --- Configuración de Base de Datos ---
if IS_PRODUCTION:
    # --- BASE DE DATOS DE PRODUCCIÓN (MYSQL EN PYTHONANYWHERE) ---
    # PythonAnywhere nos dará estos datos para poner en las variables de entorno.
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.environ.get('DB_NAME'),
            'USER': os.environ.get('DB_USER'),
            'PASSWORD': os.environ.get('DB_PASSWORD'),
            'HOST': os.environ.get('DB_HOST'),
        }
    }
else:
    # --- BASE DE DATOS DE DESARROLLO (SQLITE LOCAL) ---
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
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
STATIC_ROOT = BASE_DIR / 'staticfiles' # PythonAnywhere necesita esta ruta
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# WhiteNoise Storage
STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
LOGIN_REDIRECT_URL = 'escritura:lista_escritos'
LOGOUT_REDIRECT_URL = 'escritura:lista_escritos'

# CKEditor
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