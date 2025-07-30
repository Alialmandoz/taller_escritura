# escritura/sitemaps.py

from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Escrito

class EscritoSitemap(Sitemap):
    """
    Sitemap para los modelos de Escrito.
    Usa el comportamiento por defecto de Django, que buscará automáticamente
    el método `get_absolute_url()` en cada objeto Escrito.
    """
    changefreq = "weekly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        """
        Devuelve el QuerySet de objetos que se incluirán en el sitemap.
        """
        return Escrito.objects.filter(estado='PUBLICO')

    def lastmod(self, obj):
        """
        Devuelve la fecha de la última modificación para cada objeto.
        """
        return obj.fecha_actualizacion


class StaticViewSitemap(Sitemap):
    """
    Sitemap para las páginas estáticas del sitio (ej. Inicio, Lista de Escritos).
    """
    priority = 0.6
    changefreq = 'daily'
    protocol = 'https'

    def items(self):
        """
        Devuelve una lista con los nombres de las URLs estáticas.
        Estos nombres deben coincidir con el `name` definido en los archivos urls.py.
        """
        return ['home', 'escritura:lista_escritos', 'escritura:search_results']

    def location(self, item):
        """
        Para cada item de la lista de arriba, devuelve su URL completa.
        La función `reverse` construye la URL a partir de su nombre.
        """
        return reverse(item)