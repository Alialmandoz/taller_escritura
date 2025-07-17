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
