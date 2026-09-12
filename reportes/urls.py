from django.urls import path

from . import views

app_name = "reportes"

urlpatterns = [
    # /reportes/
    path("", views.resumen, name="resumen"),
    # /reportes/categoria/<categoria_id>/ -> ruta dinámica (número)
    path("categoria/<int:categoria_id>/", views.detalle_categoria, name="detalle_categoria"),
    # /reportes/acerca/
    path("acerca/", views.acerca, name="acerca"),
]
