# escritura/views.py

from django.shortcuts import render, get_object_or_404 # Importamos get_object_or_404
from django.views.generic import DetailView           # AÑADIDO: Importamos DetailView de las CBV
from .models import Escrito                           # Importamos nuestro modelo Escrito

# AÑADIDO: Vista basada en función para listar escritos públicos
def lista_escritos(request):
    """
    Esta vista recupera todos los objetos Escrito cuyo estado sea 'PUBLICO'
    y los pasa a la plantilla para su visualización.
    """
    escritos = Escrito.objects.filter(estado='PUBLICO').order_by('-fecha_creacion')
    contexto = {
        'escritos': escritos
    }
    return render(request, 'escritura/lista_escritos.html', contexto)

# AÑADIDO: Vista basada en clase para mostrar el detalle de un escrito
class DetalleEscrito(DetailView):
    """
    Esta vista basada en clase (CBV) se encarga de mostrar los detalles
    de un único objeto Escrito.

    Usa DetailView de Django para simplificar la lógica de obtención de un objeto.
    """
    model = Escrito  # Le decimos a DetailView qué modelo debe usar.
    template_name = 'escritura/detalle_escrito.html' # Ruta a la plantilla para mostrar el detalle.
    context_object_name = 'escrito' # Nombre de la variable que contendrá el objeto en la plantilla.

    def get_queryset(self):
        """
        Sobrescribe get_queryset para asegurar que solo se puedan ver
        escritos que sean públicos.
        """
        # Filtra para obtener solo escritos públicos.
        # Esto añade una capa de seguridad para que los usuarios no puedan acceder
        # a escritos privados o borradores a través de la URL directa.
        return Escrito.objects.filter(estado='PUBLICO')