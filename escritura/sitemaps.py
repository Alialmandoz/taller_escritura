from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Escrito

class EscritoSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return Escrito.objects.filter(estado='PUBLICO')

    def lastmod(self, obj):
        return obj.fecha_actualizacion

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['home', 'escritura:lista_escritos', 'escritura:search_results']

    def location(self, item):
        return reverse(item)
