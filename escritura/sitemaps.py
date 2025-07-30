# escritura/sitemaps.py
from django.contrib.sitemaps import Sitemap
from .models import Escrito
from django.urls import reverse

class EscritoSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        print("[Sitemap DEBUG] Entrando a EscritoSitemap.items()") # Micrófono 1
        queryset = Escrito.objects.filter(estado='PUBLICO')
        print(f"[Sitemap DEBUG] .items() encontró {queryset.count()} objetos.") # Micrófono 2
        return queryset

    def location(self, obj):
        # Sobrescribimos este método para ver qué pasa para CADA objeto.
        # Este es el micrófono más importante.
        print(f"  [Sitemap DEBUG] Procesando location para el objeto: '{obj.titulo}' (ID: {obj.pk})") # Micrófono 3
        
        # Devolvemos la URL como lo haría el método por defecto
        url = obj.get_absolute_url()
        print(f"  [Sitemap DEBUG] get_absolute_url() devolvió: '{url}'") # Micrófono 4
        return url

    def lastmod(self, obj):
        return obj.fecha_actualizacion

# Dejamos la otra clase sin cambios
class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'
    protocol = 'https' # Añadimos el protocolo aquí también por si acaso

    def items(self):
        return ['home', 'escritura:lista_escritos', 'escritura:search_results']

    def location(self, item):
        return reverse(item)