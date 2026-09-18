"""
Configuración del proyecto 'config'.

Este archivo nace del tutorial oficial de Django (tutorial01) y se
extiende con lo visto en tutorial02 (base de datos / apps instaladas)
y tutorial03 (templates).

NOTA PARA TI: cambia el nombre del proyecto, el idioma, la zona horaria,
etc. según tu problemática real. Aquí se deja tal cual lo genera
'django-admin startproject' más los ajustes mínimos de los tutoriales.
"""

import os
from pathlib import Path

# Construye rutas dentro del proyecto así: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# ADVERTENCIA DE SEGURIDAD: mantén en secreto la clave usada en producción.
# En un proyecto real, esto NO debe subirse a un repositorio público;
# usa variables de entorno (por ejemplo con python-decouple o django-environ).
SECRET_KEY = "clave-de-ejemplo-cambia-esto-antes-de-producción"

# ADVERTENCIA DE SEGURIDAD: no ejecutes con DEBUG activado en producción.
DEBUG = True

ALLOWED_HOSTS = []


# Definición de aplicaciones -------------------------------------------------
# Aquí se ve claramente que UN proyecto puede contener VARIAS apps:
# 'catalogo' y 'reportes' son dos apps propias de este proyecto,
# además de las apps que trae Django por defecto (admin, auth, etc.)
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # --- Apps propias del proyecto (EJEMPLO, agrega o renombra las tuyas) ---
    "catalogo",
    "reportes",
    "integracion",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # 'templates/' a nivel de proyecto, para una plantilla base
        # compartida por todas las apps (tutorial03 permite ambos enfoques:
        # templates por app y templates a nivel de proyecto).
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Base de datos ---------------------------------------------------------
# Por defecto SQLite, tal como lo deja el tutorial oficial (tutorial02).
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Validación de contraseñas ----------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Internacionalización ----------------------------------------------------
# EJEMPLO: cámbialo si tu problemática está en otro idioma / zona horaria.
LANGUAGE_CODE = "es-co"
TIME_ZONE = "America/Bogota"
USE_I18N = True
USE_TZ = True


# Archivos estáticos (CSS, JavaScript, imágenes) ---------------------------
STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Microservicio externo (app 'integracion') --------------------------------
# EJEMPLO: reemplaza este valor por la URL real una vez despliegues tu
# microservicio en Render, Railway o como función de Netlify
# (ej. "https://mi-servicio.onrender.com/api/datos/").
# Se lee de una variable de entorno para NO dejar la URL final "quemada"
# en el código; si no defines la variable, usa el placeholder de ejemplo.
MICROSERVICIO_URL = os.environ.get(
    "MICROSERVICIO_URL",
    "https://threed-organ-inc-microservicio.onrender.com/api/modelos",
)
