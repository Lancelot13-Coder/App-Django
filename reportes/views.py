"""
Vistas de la app 'reportes'.

Muestra que una app distinta a 'catalogo' también puede tener varias
vistas propias, y que puede consultar modelos de OTRA app del mismo
proyecto (catalogo.Categoria / catalogo.Elemento) además de los suyos
(Comentario). Esto cumple el requisito de "modelos consultados desde
las vistas" incluso entre apps distintas del mismo proyecto.
"""

from django.db.models import Count
from django.shortcuts import get_object_or_404, render

from catalogo.models import Categoria, Elemento
from .models import Comentario


def resumen(request):
    """Vista 1: panel general con conteos por categoría.
    EJEMPLO: cambia esta consulta según los indicadores que necesite
    tu problemática (totales, promedios, filtros por fecha, etc.)
    """
    categorias_con_totales = Categoria.objects.annotate(total_elementos=Count("elementos"))
    total_elementos = Elemento.objects.count()
    total_comentarios = Comentario.objects.count()
    context = {
        "categorias_con_totales": categorias_con_totales,
        "total_elementos": total_elementos,
        "total_comentarios": total_comentarios,
    }
    return render(request, "reportes/resumen.html", context)


def detalle_categoria(request, categoria_id):
    """Vista 2: reporte de UNA categoría puntual.
    Ruta dinámica con parámetro: /reportes/categoria/<categoria_id>/
    """
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    elementos = categoria.elementos.all()
    context = {"categoria": categoria, "elementos": elementos}
    return render(request, "reportes/detalle_categoria.html", context)


def acerca(request):
    """Vista 3: página estática de ejemplo (sin consultar modelos),
    útil como plantilla para páginas informativas de tu proyecto
    (ayuda, contacto, políticas, etc.)
    """
    return render(request, "reportes/acerca.html")
