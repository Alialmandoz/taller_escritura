# escritura/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required # Decorador para requerir autenticación

from .models import Escrito # Importamos nuestro modelo Escrito
from .forms import CustomUserCreationForm, EscritoForm # Importamos nuestros formularios
from django.http import Http404 # Para lanzar un error 404 si el usuario no es el autor

# Vista basada en función para listar escritos públicos
def lista_escritos(request):
    """
    Esta vista recupera todos los objetos Escrito cuyo estado sea 'PUBLICO'
    y los pasa a la plantilla para su visualización.
    """
    # Consulta a la base de datos: Obtiene todos los escritos donde el estado es 'PUBLICO'.
    # .order_by('-fecha_creacion') asegura que los escritos más recientes aparezcan primero.
    escritos = Escrito.objects.filter(estado='PUBLICO').order_by('-fecha_creacion')

    # AÑADIDO PARA DEPURACIÓN: Imprime el queryset para ver qué elementos contiene.
    # Estas líneas te mostrarán en la terminal del servidor qué escritos está recuperando la consulta.
    print(f"DEBUG: Escritos públicos recuperados: {escritos}")
    print(f"DEBUG: Cantidad de escritos públicos: {escritos.count()}")
    for escrito in escritos:
        print(f"DEBUG: Escrito ID: {escrito.pk}, Título: {escrito.titulo}, Estado: {escrito.estado}, Autor: {escrito.autor.username}")


    # Diccionario de contexto: Los datos que queremos pasar a la plantilla.
    # La clave 'escritos' será el nombre de la variable en la plantilla.
    contexto = {
        'escritos': escritos
    }

    # Renderiza la plantilla 'escritura/lista_escritos.html'
    # y le pasa el diccionario 'contexto'.
    return render(request, 'escritura/lista_escritos.html', contexto)


# Vista basada en clase para mostrar el detalle de un escrito
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


# Vista para el registro de nuevos usuarios
def registro_usuario(request):
    """
    Esta vista maneja la lógica para el registro de nuevos usuarios.
    - Si la solicitud es GET, muestra el formulario de registro vacío.
    - Si la solicitud es POST, procesa los datos del formulario:
        - Si es válido, crea el usuario, inicia sesión al usuario y redirige a la página principal.
        - Si no es válido, vuelve a mostrar el formulario con los errores.
    """
    if request.method == 'POST':
        # Si la solicitud es POST, el formulario ha sido enviado
        form = CustomUserCreationForm(request.POST) # Crea una instancia del formulario con los datos enviados
        if form.is_valid():
            # Si el formulario es válido, guarda el nuevo usuario
            user = form.save()
            # Opcional: Iniciar sesión al usuario automáticamente después del registro
            login(request, user)
            # Redirige al usuario a una página de éxito (ej. la lista de escritos o un dashboard)
            # Por ahora, redirigimos a la lista de escritos.
            return redirect('escritura:lista_escritos')
    else:
        # Si la solicitud es GET, muestra un formulario vacío
        form = CustomUserCreationForm()
    
    # Renderiza la plantilla con el formulario (vacío o con errores)
    return render(request, 'escritura/registro.html', {'form': form})


# Vista para crear un nuevo escrito
@login_required # Decorador: Solo usuarios autenticados pueden acceder a esta vista.
def crear_escrito(request):
    """
    Esta vista permite a un usuario autenticado crear un nuevo escrito.
    - Si la solicitud es GET, muestra un formulario EscritoForm vacío.
    - Si la solicitud es POST, procesa el formulario:
        - Si es válido, guarda el escrito, asigna el autor (el usuario actual)
          y redirige a la página de detalle del nuevo escrito.
        - Si no es válido, vuelve a mostrar el formulario con los errores.
    """
    if request.method == 'POST':
        form = EscritoForm(request.POST) # Crea una instancia del formulario con los datos enviados
        if form.is_valid():
            # No guardamos el formulario directamente todavía (commit=False)
            # porque necesitamos añadir el autor (el usuario actual) antes de guardar.
            escrito = form.save(commit=False) 
            escrito.autor = request.user # Asigna el autor del escrito al usuario actualmente logueado.
            escrito.save() # Ahora sí, guarda el objeto Escrito completo en la base de datos.
            
            # Redirige a la página de detalle del escrito recién creado.
            # Necesitamos pasar el 'pk' del escrito a la URL.
            return redirect('escritura:detalle_escrito', pk=escrito.pk)
    else:
        # Si la solicitud es GET, muestra un formulario vacío.
        form = EscritoForm()
    
    # Renderiza la plantilla con el formulario (vacío o con errores)
    return render(request, 'escritura/crear_editar_escrito.html', {'form': form, 'es_creacion': True})

# Vista para editar un escrito existente
@login_required # Solo usuarios autenticados pueden acceder.
def editar_escrito(request, pk):
    """
    Esta vista permite a un usuario autenticado editar un escrito existente.
    - pk: La clave primaria (ID) del escrito a editar.
    - Se verifica que el usuario autenticado sea el autor del escrito.
    """
    # Intentar obtener el escrito, o lanzar un 404 si no existe.
    escrito = get_object_or_404(Escrito, pk=pk)

    # VERIFICACIÓN DE PERMISOS: Asegurarse de que solo el autor pueda editar.
    # Si el usuario logueado no es el autor del escrito, levantamos un error 404
    # (por motivos de seguridad, es mejor un 404 que un 403 en algunos casos,
    # para no revelar la existencia del escrito a usuarios no autorizados).
    if request.user != escrito.autor:
        raise Http404("No tienes permiso para editar este escrito.")
        # Alternativamente, podrías redirigir:
        # from django.contrib import messages
        # messages.error(request, "No tienes permiso para editar este escrito.")
        # return redirect('escritura:detalle_escrito', pk=escrito.pk)


    if request.method == 'POST':
        # Si es POST, creamos una instancia del formulario con los datos enviados
        # y le pasamos la instancia del escrito existente para que la actualice.
        form = EscritoForm(request.POST, instance=escrito)
        if form.is_valid():
            # Guarda los cambios en el escrito. Como ya pasamos 'instance', no necesitamos commit=False.
            form.save()
            # Redirige a la página de detalle del escrito editado.
            return redirect('escritura:detalle_escrito', pk=escrito.pk)
    else:
        # Si es GET, creamos una instancia del formulario y la inicializamos
        # con los datos del escrito existente para que aparezcan pre-rellenados.
        form = EscritoForm(instance=escrito)
    
    # Renderiza la misma plantilla usada para crear, pasando el formulario y la bandera.
    # es_creacion = False le dice a la plantilla que es una operación de edición.
    return render(request, 'escritura/crear_editar_escrito.html', {'form': form, 'es_creacion': False})