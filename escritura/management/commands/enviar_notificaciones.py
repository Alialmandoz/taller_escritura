# escritura/management/commands/enviar_notificaciones.py

from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from escritura.models import Escrito

User = get_user_model()

class Command(BaseCommand):
    help = 'Envía notificaciones por email sobre nuevos escritos publicados.'

    def handle(self, *args, **options):
        # 1. Obtener los escritos que son públicos y de los que aún no se ha enviado notificación.
        escritos_a_notificar = Escrito.objects.filter(estado='PUBLICO', notificacion_enviada=False)

        if not escritos_a_notificar.exists():
            self.stdout.write(self.style.SUCCESS('No hay nuevos escritos para notificar.'))
            return

        # 2. Obtener todos los usuarios que recibirán la notificación.
        usuarios = User.objects.all()

        for escrito in escritos_a_notificar:
            self.stdout.write(f'Procesando escrito: "{escrito.titulo}"...')

            # 3. Preparar el contenido del email.
            # Usamos un template para que sea más fácil de mantener.
            # (Crearemos este template en el siguiente paso)
            contexto_email = {
                'titulo_escrito': escrito.titulo,
                'nombre_autor': escrito.autor.username,
                # Podrías añadir una URL completa si tienes configurado el dominio
                # 'url_escrito': escrito.get_absolute_url() 
            }
            asunto = f"Nuevo artículo de {escrito.autor.username}: {escrito.titulo}"
            
            # Renderizamos un template HTML para el cuerpo del correo
            # html_mensaje = render_to_string('emails/notificacion_nuevo_escrito.html', contexto_email)
            # Creamos una versión en texto plano para clientes de correo que no soportan HTML
            # texto_plano_mensaje = strip_tags(html_mensaje)
            
            # Por simplicidad ahora, usaremos un texto simple.
            mensaje = f'{escrito.autor.username} ha publicado un nuevo artículo: "{escrito.titulo}"'

            # 4. Filtrar y enviar emails.
            destinatarios = [user.email for user in usuarios if user.email and user.id != escrito.autor.id]
            
            if destinatarios:
                try:
                    send_mail(
                        asunto,
                        mensaje,
                        'notificaciones@tallerescritura.com', # Remitente
                        destinatarios,
                        fail_silently=False,
                    )
                    self.stdout.write(self.style.SUCCESS(f'  > Notificaciones enviadas a {len(destinatarios)} usuarios.'))
                    
                    # 5. Marcar el escrito como notificado para no volver a enviarlo.
                    escrito.notificacion_enviada = True
                    escrito.save()

                except Exception as e:
                    self.stdout.write(self.style.ERROR(f'  > Error al enviar notificaciones para "{escrito.titulo}": {e}'))
            else:
                self.stdout.write(self.style.WARNING(f'  > No hay destinatarios para notificar sobre "{escrito.titulo}".'))
                # Aunque no haya destinatarios, lo marcamos como procesado.
                escrito.notificacion_enviada = True
                escrito.save()

        self.stdout.write(self.style.SUCCESS('Proceso de notificación completado.'))
