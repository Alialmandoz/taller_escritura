from django.contrib import admin
from django.urls import path, include 
from django.conf import settings # AÑADIDO: Para importar settings
from django.conf.urls.static import static # AÑADIDO: Para servir archivos media en desarrollo
from escritura import views # AÑADIDO: Importamos las vistas de nuestra app

urlpatterns = [
    # AÑADIDO: URL para la página principal
    path('', views.pagina_principal, name='home'),

    path('admin/', admin.site.urls),
    path('escritura/', include('escritura.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    # AÑADIDO: URLs para django-ckeditor-uploader
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

# AÑADIDO: Configuración para servir archivos de medios en el servidor de desarrollo.
# ¡Esto solo debe usarse en desarrollo (DEBUG = True)!
# En producción, un servidor web como Nginx o Apache se encargará de servir los archivos media.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
