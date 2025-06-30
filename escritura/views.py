# escritura/views.py

from django.shortcuts import render, get_object_or_404, redirect

# AÑADIDO: Vista para la página principal
def pagina_principal(request):
    """
    Renderiza la página de inicio/landing page.
    Obtiene todos los perfiles que han aceptado ser mostrados públicamente.
    """
    # Usamos select_related('user') para optimizar la consulta.
    # Evita que Django haga una consulta a la base de datos por cada usuario en el bucle de la plantilla.
    perfiles_publicos = Profile.objects.filter(mostrar_en_comunidad=True).select_related('user')

    contexto = {
        'perfiles_publicos': perfiles_publicos
    }
    return render(request, 'escritura/home.html', contexto)


from django.views.generic import DetailView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required # Decorador para requerir autenticación
from django.http import Http404
from django.contrib import messages

from .models import Escrito, Profile # MODIFICADO: Importamos también el modelo Profile
from .forms import CustomUserCreationForm, EscritoForm, ProfileForm # MODIFICADO: Importamos ProfileForm

# Vista basada en función para listar escritos públicos
def lista_escritos(request):
    """
    Esta vista recupera todos los objetos Escrito cuyo estado sea 'PUBLICO'
    y los pasa a la plantilla para su visualización.
    """
    # MODIFICADO: Se optimiza la consulta para incluir los datos del autor y su perfil.
    # Esto evita múltiples consultas a la base de datos (problema N+1) en la plantilla.
    escritos = Escrito.objects.filter(estado='PUBLICO').select_related('autor__profile').order_by('-fecha_creacion')

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
        # Si es GET, muestra un formulario vacío.
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


# AÑADIDO: Vista para eliminar un escrito
@login_required # Solo usuarios autenticados pueden acceder.
def eliminar_escrito(request, pk):
    """
    Esta vista maneja la eliminación de un escrito.
    - Si la solicitud es GET, muestra una página de confirmación.
    - Si la solicitud es POST, procede a eliminar el escrito.
    - Se verifica que el usuario autenticado sea el autor del escrito.
    """
    escrito = get_object_or_404(Escrito, pk=pk)

    # VERIFICACIÓN DE PERMISOS: Asegurarse de que solo el autor pueda eliminar.
    if request.user != escrito.autor:
        messages.error(request, "No tienes permiso para eliminar este escrito.")
        return redirect('escritura:detalle_escrito', pk=escrito.pk)
        # O podrías lanzar un Http404 como en editar_escrito, si prefieres no dar pistas.
        # raise Http404("No tienes permiso para eliminar este escrito.")

    if request.method == 'POST':
        # Si la solicitud es POST, significa que el usuario ha confirmado la eliminación.
        escrito.delete() # ¡Elimina el objeto de la base de datos!
        messages.success(request, f"El escrito '{escrito.titulo}' ha sido eliminado exitosamente.")
        return redirect('escritura:lista_escritos') # Redirige a la lista después de eliminar.

    # Si la solicitud es GET, muestra la página de confirmación.
    return render(request, 'escritura/confirmar_eliminar_escrito.html', {'escrito': escrito})


# AÑADIDO: Vista para mostrar el perfil del usuario y sus escritos
@login_required # Solo usuarios autenticados pueden acceder a su perfil.
def perfil_usuario(request):
    """
    Esta vista muestra el perfil del usuario autenticado, incluyendo
    su biografía, foto de perfil y una lista de TODOS sus escritos
    (sin importar el estado: borrador, privado, público).
    """
    # El objeto 'request.user' ya está disponible gracias a @login_required
    # y el middleware de autenticación.
    usuario = request.user

    # Intentamos obtener el perfil del usuario.
    # Gracias a la señal post_save que creamos, cada usuario debería tener un perfil.
    try:
        perfil = usuario.profile
    except Profile.DoesNotExist:
        # En un escenario muy improbable (ej. si la señal falló o se deshabilitó),
        # podríamos crear uno aquí o redirigir. Por ahora, asumimos que existe.
        perfil = Profile.objects.create(user=usuario)
        # Podrías añadir un mensaje de warning aquí si esto fuera algo que debe ser notado:
        # messages.warning(request, "Tu perfil fue creado automáticamente. Por favor, complétalo.")

    # MODIFICADO: Se optimiza la consulta para evitar el problema N+1.
    # Usamos `select_related` para traer la información del autor y su perfil
    # en una única consulta a la base de datos, mejorando drásticamente el rendimiento.
    mis_escritos = Escrito.objects.filter(autor=usuario).select_related('autor__profile').order_by('-fecha_creacion')

    contexto = {
        'usuario': usuario,      # El objeto User
        'perfil': perfil,        # El objeto Profile asociado
        'mis_escritos': mis_escritos # Todos los escritos del usuario
    }

    return render(request, 'escritura/perfil_usuario.html', contexto)


# AÑADIDO: Vista para editar el perfil del usuario
@login_required
def editar_perfil(request):
    """
    Permite al usuario autenticado editar su propio perfil (bio y foto).
    """
    if request.method == 'POST':
        # Al procesar el formulario, pasamos la instancia del perfil a actualizar.
        # ¡CRÍTICO! Pasamos request.FILES para manejar la subida de la imagen.
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save() # Guarda los cambios en el perfil del usuario.
            messages.success(request, '¡Tu perfil ha sido actualizado con éxito!')
            return redirect('escritura:perfil_usuario')
    else:
        # Al mostrar el formulario por primera vez, lo inicializamos con los datos actuales del perfil.
        form = ProfileForm(instance=request.user.profile)

    contexto = {
        'form': form
    }
    return render(request, 'escritura/editar_perfil.html', contexto)