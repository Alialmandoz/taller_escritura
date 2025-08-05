# escritura/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.views.generic import DetailView
from django.contrib.auth import login, get_user_model
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.contrib import messages
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib.auth.decorators import user_passes_test

from .models import Escrito, Profile, Comentario
from .forms import CustomUserCreationForm, EscritoForm, UserUpdateForm, ProfileUpdateForm, ComentarioForm

User = get_user_model()

# -----------------------------------------------------------------------------
# VISTAS PRINCIPALES DE LA APLICACIÓN
# -----------------------------------------------------------------------------

def pagina_principal(request):
    """
    Renderiza la página de inicio/landing page.
    Obtiene todos los perfiles que han aceptado ser mostrados públicamente.
    """
    perfiles_publicos = Profile.objects.filter(mostrar_en_comunidad=True).select_related('user')
    contexto = {'perfiles_publicos': perfiles_publicos}
    return render(request, 'escritura/home.html', contexto)

def lista_escritos(request):
    """
    Esta vista recupera todos los objetos Escrito cuyo estado sea 'PUBLICO',
    los pagina y los pasa a la plantilla para su visualización.
    """
    escritos_list = Escrito.objects.filter(estado='PUBLICO').select_related('autor__profile').order_by('-fecha_creacion')
    
    paginator = Paginator(escritos_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    contexto = {'page_obj': page_obj}
    return render(request, 'escritura/lista_escritos.html', contexto)


class DetalleEscrito(DetailView):
    """
    Vista basada en clase para mostrar los detalles de un escrito,
    sus comentarios, y manejar la publicación de nuevos comentarios.
    """
    model = Escrito
    template_name = 'escritura/detalle_escrito.html'
    context_object_name = 'escrito'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        escrito = self.get_object()
        context['comentarios'] = escrito.comentarios.select_related('autor__profile').all()
        if self.request.user.is_authenticated:
            context['comentario_form'] = ComentarioForm()
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')

        self.object = self.get_object()
        form = ComentarioForm(request.POST)

        if form.is_valid():
            nuevo_comentario = form.save(commit=False)
            nuevo_comentario.escrito = self.object
            nuevo_comentario.autor = request.user
            nuevo_comentario.save()
            messages.success(request, "Tu comentario ha sido publicado.")
            return redirect('escritura:detalle_escrito', pk=self.object.pk)
        else:
            context = self.get_context_data()
            context['comentario_form'] = form
            messages.error(request, "Hubo un error al publicar tu comentario.")
            return self.render_to_response(context)


# -----------------------------------------------------------------------------
# VISTAS DE AUTENTICACIÓN Y PERFILES
# -----------------------------------------------------------------------------

def registro_usuario(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('escritura:lista_escritos')
    else:
        form = CustomUserCreationForm()
    return render(request, 'escritura/registro.html', {'form': form})

@login_required
def perfil_usuario(request):
    usuario = request.user
    try:
        perfil = usuario.profile
    except Profile.DoesNotExist:
        perfil = Profile.objects.create(user=usuario)

    mis_escritos_list = Escrito.objects.filter(autor=usuario).order_by('-fecha_creacion')
    paginator = Paginator(mis_escritos_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    contexto = {
        'usuario': usuario,
        'perfil': perfil,
        'page_obj': page_obj
    }
    return render(request, 'escritura/perfil_usuario.html', contexto)

@login_required
def editar_perfil(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, '¡Tu perfil ha sido actualizado con éxito!')
            return redirect('escritura:perfil_usuario')
        else:
            messages.error(request, 'Por favor, corrige los errores a continuación.')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    
    contexto = {'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'escritura/editar_perfil.html', contexto)

def perfil_publico(request, user_id):
    usuario_perfil = get_object_or_404(
        User.objects.select_related('profile'),
        pk=user_id,
        profile__mostrar_en_comunidad=True
    )
    escritos_publicos_list = Escrito.objects.filter(autor=usuario_perfil, estado='PUBLICO')
    paginator = Paginator(escritos_publicos_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    contexto = {'usuario_perfil': usuario_perfil, 'page_obj': page_obj}
    return render(request, 'escritura/perfil_publico.html', contexto)


# -----------------------------------------------------------------------------
# VISTAS DE GESTIÓN DE ESCRITOS (CRUD)
# -----------------------------------------------------------------------------

@login_required
def crear_escrito(request):
    if request.method == 'POST':
        form = EscritoForm(request.POST)
        if form.is_valid():
            escrito = form.save(commit=False)
            escrito.autor = request.user
            escrito.save()
            return redirect('escritura:detalle_escrito', pk=escrito.pk)
    else:
        form = EscritoForm()
    return render(request, 'escritura/crear_editar_escrito.html', {'form': form, 'es_creacion': True})

@login_required
def editar_escrito(request, pk):
    escrito = get_object_or_404(Escrito, pk=pk)
    if request.user != escrito.autor:
        raise Http404("No tienes permiso para editar este escrito.")

    if request.method == 'POST':
        form = EscritoForm(request.POST, instance=escrito)
        if form.is_valid():
            form.save()
            return redirect('escritura:detalle_escrito', pk=escrito.pk)
    else:
        form = EscritoForm(instance=escrito)
    return render(request, 'escritura/crear_editar_escrito.html', {'form': form, 'es_creacion': False})

@login_required
def eliminar_escrito(request, pk):
    escrito = get_object_or_404(Escrito, pk=pk)
    if request.user != escrito.autor:
        messages.error(request, "No tienes permiso para eliminar este escrito.")
        return redirect('escritura:detalle_escrito', pk=escrito.pk)

    if request.method == 'POST':
        escrito.delete()
        messages.success(request, f"El escrito '{escrito.titulo}' ha sido eliminado exitosamente.")
        return redirect('escritura:lista_escritos')

    return render(request, 'escritura/confirmar_eliminar_escrito.html', {'escrito': escrito})


# -----------------------------------------------------------------------------
# VISTAS DE UTILIDAD (BÚSQUEDA, SITEMAP)
# -----------------------------------------------------------------------------

def search_results_view(request):
    """Renderiza la página que contendrá los resultados de búsqueda de Google."""
    return render(request, 'escritura/search_results.html')

def generar_sitemap(request):
    """
    Una vista personalizada para generar el sitemap.xml de forma manual y robusta.
    """
    from django.contrib.sites.models import Site
    
    current_site = Site.objects.get_current()
    domain = current_site.domain

    escritos_publicos = Escrito.objects.filter(estado='PUBLICO').order_by('-fecha_actualizacion')
    urls_escritos = []
    for escrito in escritos_publicos:
        url_info = {
            'location': f"https://{domain}{escrito.get_absolute_url()}",
            'lastmod': escrito.fecha_actualizacion,
            'priority': 0.8,
            'changefreq': 'weekly'
        }
        urls_escritos.append(url_info)

    nombres_rutas_estaticas = ['home', 'escritura:lista_escritos', 'escritura:search_results']
    urls_estaticas = []
    for name in nombres_rutas_estaticas:
        url_info = {
            'location': f"https://{domain}{reverse(name)}",
            'priority': 0.6,
            'changefreq': 'daily'
        }
        urls_estaticas.append(url_info)

    todas_las_urls = urls_estaticas + urls_escritos

    return render(
        request,
        'sitemap.xml',
        {'url_list': todas_las_urls},
        content_type='application/xml'
    )

@user_passes_test(lambda u: u.is_superuser)
def vista_test_email(request):
    """
    Una vista para administradores para enviar un correo de prueba y verificar
    la configuración del servidor de correo.
    """
    # Si se hace clic en el botón, el método de la petición será POST.
    if request.method == 'POST':
        try:
            # Construimos y enviamos el correo.
            asunto = "Correo de prueba desde Taller de Escritura"
            mensaje = (
                "¡Felicidades! Este es un correo de prueba enviado desde tu aplicación "
                "en PythonAnywhere. Si lo has recibido, tu configuración de correo (SMTP) funciona correctamente."
            )
            # El remitente (from_email) se toma del DEFAULT_FROM_EMAIL en settings.py
            send_mail(
                subject=asunto,
                message=mensaje,
                from_email=None,
                # Corregí el typo en el correo, debe ser una lista.
                recipient_list=['alialmandoz@gmail.com'], 
                fail_silently=False  # Queremos que falle ruidosamente si hay un error.
            )
            # Añadimos un mensaje de éxito para mostrar en la plantilla.
            messages.success(request, "¡Correo de prueba enviado con éxito! Revisa la bandeja de entrada de alialmandoz@gmail.com.")

        except Exception as e:
            # Si algo sale mal (ej: contraseña incorrecta, bloqueo de Google), mostramos un error.
            messages.error(request, f"Error al enviar el correo: {e}")

        # Redirigimos a la misma página para mostrar el mensaje de éxito o error.
        return redirect('escritura:test_email')

    # Si la petición es GET, simplemente mostramos la página.
    return render(request, 'escritura/test_email.html')