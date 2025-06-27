# escritura/urls.py

from django.urls import path
from . import views # Importamos el módulo views de nuestra propia aplicación

# Definición del nombre de la aplicación para URL namespaces
# Es una buena práctica para evitar conflictos de nombres si tienes URLs con el mismo nombre en diferentes apps.
app_name = 'escritura'

urlpatterns = [
    # path(ruta_url, vista_a_llamar, name=nombre_para_referenciar_url)
    # path('', ...) significa la raíz de esta app (ej: /escritura/)
    path('', views.lista_escritos, name='lista_escritos'),

    # AÑADIDO: URL para el detalle de un escrito.
    # <int:pk> es un conversor de path que captura un número entero (la clave primaria del escrito)
    # y lo pasa como argumento 'pk' a la vista DetalleEscrito.
    # .as_view() se usa para llamar vistas basadas en clase.
    path('<int:pk>/', views.DetalleEscrito.as_view(), name='detalle_escrito'),
]