# Proyecto Django de EJEMPLO (tutoriales 01–03 + estructura ampliada)

Este proyecto es una **base/plantilla** para que la adaptes en Visual
Studio Code a la problemática que tú identifiques. Todos los nombres
(`catalogo`, `Elemento`, `Categoria`, `reportes`, `Comentario`, etc.) son
**genéricos de ejemplo** — reemplázalos por los términos reales de tu
proyecto (ej. `Producto`, `Cliente`, `Curso`, `Tarea`, `Paciente`...).

Busca los comentarios `# EJEMPLO` y `# TODO` en el código: son los
puntos donde se espera que tú edites.

## ¿Qué incluye y de dónde sale cada parte?

| Elemento del proyecto | Tutorial oficial de Django | Dónde está aquí |
|---|---|---|
| Crear proyecto (`django-admin startproject`) | [tutorial01](https://docs.djangoproject.com/en/6.1/intro/tutorial01/) | Carpeta `config/` (equivalente a `mysite/`) |
| Crear una app (`manage.py startapp`) | tutorial01 | Carpetas `catalogo/` y `reportes/` |
| Primera vista + `urls.py` de la app | tutorial01 | `catalogo/views.py` + `catalogo/urls.py` |
| `include()` en el URLconf raíz | tutorial01 | `config/urls.py` |
| Modelos y migraciones | [tutorial02](https://docs.djangoproject.com/en/6.1/intro/tutorial02/) | `catalogo/models.py`, `reportes/models.py` |
| Sitio de administración (`admin.py`) | tutorial02 | `catalogo/admin.py`, `reportes/admin.py` |
| Vistas que reciben parámetros de la URL | [tutorial03](https://docs.djangoproject.com/en/6.1/intro/tutorial03/) | `detalle`, `por_categoria`, `detalle_categoria` |
| `render()`, `get_object_or_404()` | tutorial03 | Todas las vistas |
| Templates, `{% extends %}`, `{% url %}`, namespaces (`app_name`) | tutorial03 | Carpeta `templates/` de cada app + `templates/base.html` |

## Requisitos adicionales que pediste (más allá de los tutoriales)

- **Múltiples vistas en una app:** `catalogo` tiene `index`, `detalle`,
  `por_categoria` y `buscar`. `reportes` tiene `resumen`,
  `detalle_categoria` y `acerca`.
- **Múltiples apps en un proyecto:** `catalogo` y `reportes`, ambas
  registradas en `config/settings.py` → `INSTALLED_APPS`.
- **Modelos consultados desde las vistas:** todas las vistas usan el
  ORM (`Elemento.objects...`, `Categoria.objects...`, etc.). `reportes`
  incluso consulta modelos definidos en `catalogo` (relación entre apps).
- **Rutas dinámicas con parámetros:** `catalogo/<int:elemento_id>/`,
  `catalogo/categoria/<slug:categoria_slug>/`,
  `reportes/categoria/<int:categoria_id>/`. Cada una hace algo real con
  el parámetro (buscar el objeto, filtrar, agrupar), no solo lo muestra.

## Estructura de carpetas

```
proyecto_django/
├── manage.py
├── requirements.txt
├── config/                 # el "proyecto" (equivalente a mysite/)
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── catalogo/                # app 1
│   ├── models.py            # Categoria, Elemento
│   ├── views.py             # index, detalle, por_categoria, buscar
│   ├── urls.py
│   ├── admin.py
│   └── templates/catalogo/
├── reportes/                 # app 2
│   ├── models.py             # Comentario (relacionado con Elemento)
│   ├── views.py              # resumen, detalle_categoria, acerca
│   ├── urls.py
│   ├── admin.py
│   └── templates/reportes/
└── templates/
    └── base.html             # plantilla base compartida
```

## Puesta en marcha (entorno virtual + instalación)

Desde la carpeta del proyecto (`proyecto_django/`), en la terminal de
Visual Studio Code:

### 1. Crear y activar el entorno virtual

```bash
# Crear el entorno virtual
python -m venv venv

# Activarlo
# Windows (PowerShell):
venv\Scripts\Activate.ps1
# Windows (cmd):
venv\Scripts\activate.bat
# macOS / Linux:
source venv/bin/activate
```

En VS Code, verifica que el intérprete de Python seleccionado
(esquina inferior derecha) sea el de `venv`.

### 2. Instalar Django dentro del entorno virtual

```bash
pip install -r requirements.txt
```

### 3. Crear las migraciones y la base de datos (SQLite por defecto)

```bash
python manage.py makemigrations catalogo reportes
python manage.py migrate
```

### 4. Crear un superusuario para entrar al admin

```bash
python manage.py createsuperuser
```

### 5. Levantar el servidor de desarrollo

```bash
python manage.py runserver
```

Luego visita:

- `http://127.0.0.1:8000/catalogo/` — catálogo (vista `index`)
- `http://127.0.0.1:8000/catalogo/buscar/` — búsqueda
- `http://127.0.0.1:8000/reportes/` — panel de reportes
- `http://127.0.0.1:8000/reportes/acerca/` — página estática
- `http://127.0.0.1:8000/admin/` — administración (con el superusuario)

> Como todavía no hay datos, ve primero a `/admin/` y crea 2 o 3
> `Categoria` y algunos `Elemento` para ver el catálogo y los reportes
> funcionando con información real.

## Cómo adaptarlo a TU problemática

1. Define tu problemática (ej: "control de préstamos de una
   biblioteca", "gestión de citas médicas", "seguimiento de tareas de
   un equipo").
2. Decide qué "entidades" necesitas (equivalentes a `Categoria` y
   `Elemento`) y renómbralas en `catalogo/models.py` (o crea una app
   nueva con `python manage.py startapp nombre_app` si prefieres
   empezar más limpio).
3. Ajusta `catalogo/admin.py`, `catalogo/views.py`,
   `catalogo/urls.py` y los templates para que hablen del lenguaje de
   tu problemática.
4. Revisa `reportes/` y decide qué indicadores tiene sentido mostrar
   para tu caso (totales, promedios, alertas, etc.).
5. Actualiza `config/settings.py` (nombre del proyecto en comentarios,
   idioma, zona horaria) y este mismo `README.md`.
6. Corre de nuevo `makemigrations` y `migrate` cada vez que cambies
   los modelos.

## Notas

- El proyecto usa SQLite por defecto (no necesitas instalar nada
  aparte de Django para empezar).
- `venv/` y `db.sqlite3` están en `.gitignore`: no los subas al
  repositorio; cada quien crea su propio entorno virtual localmente.
- Si tu profesor/documentación pide nombres distintos para el proyecto
  (en vez de `config`) o para las apps, puedes renombrarlos, solo
  recuerda actualizar las referencias (`DJANGO_SETTINGS_MODULE`,
  `ROOT_URLCONF`, `INSTALLED_APPS`, los `include()` en `config/urls.py`).
