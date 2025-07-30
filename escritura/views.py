def generar_sitemap(request):
    """
    Una vista personalizada para generar el sitemap.xml de forma manual y robusta.
    """
    from django.contrib.sites.models import Site
    
    # Obtenemos el dominio actual del framework de 'sites' que ya configuramos.
    current_site = Site.objects.get_current()
    domain = current_site.domain

    # 1. Recopilar URLs de los Escritos Públicos
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

    # 2. Recopilar URLs de las Páginas Estáticas
    nombres_rutas_estaticas = ['home', 'escritura:lista_escritos', 'escritura:search_results']
    urls_estaticas = []
    for name in nombres_rutas_estaticas:
        url_info = {
            'location': f"https://{domain}{reverse(name)}",
            'priority': 0.6,
            'changefreq': 'daily'
        }
        urls_estaticas.append(url_info)

    # 3. Combinar todas las URLs
    todas_las_urls = urls_estaticas + urls_escritos

    # 4. Renderizar la plantilla XML
    return render(
        request,
        'sitemap.xml',
        {'url_list': todas_las_urls},
        content_type='application/xml'
    )