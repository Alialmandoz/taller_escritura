# escritura/urls.py

from django.urls import path, include
from . import views # Importamos el módulo views de nuestra propia aplicación

# Definición del nombre de la aplicación para URL namespaces
# Es una buena práctica para evitar conflictos de nombres si tienes URLs con el mismo nombre en diferentes apps.
app_name = 'escritura'

urlpatterns = [
    path('', views.lista_escritos, name='lista_escritos'),
    path('<int:pk>/', views.DetalleEscrito.as_view(), name='detalle_escrito'),
    path('registro/', views.registro_usuario, name='registro'),
    path('crear/', views.crear_escrito, name='crear_escrito'),
    path('<int:pk>/editar/', views.editar_escrito, name='editar_escrito'),
    path('<int:pk>/eliminar/', views.eliminar_escrito, name='eliminar_escrito'),
    path('perfil/', views.perfil_usuario, name='perfil_usuario'),
    # AÑADIDO: URL para la página de edición del perfil
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
    # AÑADIDO: URL para el perfil público de un usuario
    path('perfil/<int:user_id>/', views.perfil_publico, name='perfil_publico'),
    path('search-results/', views.search_results_view, name='search_results'),
    path('test-email/', views.vista_test_email, name='test_email'),
]