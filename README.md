# taller_escritura ✨

Una plataforma digital centralizada y colaborativa para participantes de talleres de escritura.

[![Built with Django](https://img.shields.io/badge/Built%20with-Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Built with Python](https://img.shields.io/badge/Built%20with-Python-3670A0?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Licencia MIT](https://img.shields.io/badge/Licencia-MIT-green.svg)](./LICENSE)

## 🚀 Introducción

**taller_escritura** es el "hogar digital" para que los participantes de un taller de escritura desarrollen, organicen y compartan sus textos, y obtengan retroalimentación constructiva de sus pares en un entorno de comunidad y apoyo.

Esta plataforma busca ser la herramienta centralizada donde los escritores pueden gestionar su proceso creativo, beneficiarse del intercambio de ideas y sentirse parte de una comunidad activa.

## ✨ Características

La plataforma cuenta actualmente con las siguientes funcionalidades:

*   **Autenticación y Perfiles:**
    *   Registro, inicio y cierre de sesión de usuarios.
    *   Modelo `Profile` preparado para futuras ampliaciones (bio, foto).
    *   Página de perfil de usuario que muestra sus datos y una lista de todos sus escritos.

*   **Gestión Completa de Escritos (CRUD):**
    *   Creación de nuevos textos con un editor de texto enriquecido (CKEditor).
    *   Edición de escritos existentes (restringido al autor).
    *   Eliminación de escritos (restringido al autor, con página de confirmación).
    *   Control de visibilidad (`Público`, `Privado`, `Borrador`).

*   **Mejoras de UI/UX:**
    *   Paleta de colores y tipografías consistentes para una estética cuidada.
    *   Diseño responsivo base para una correcta visualización en móviles y escritorio.
    *   Sistema de mensajes para dar feedback al usuario (ej. "Escrito creado con éxito").
    *   ✨ **¡Nuevo!** Los escritos en la lista principal se pueden **expandir y contraer** para facilitar la lectura y reducir el desorden visual.

## ⚙️ Puesta en Marcha (Getting Started)

Sigue estos pasos para ejecutar el proyecto en tu entorno local.

**Prerrequisitos:**
*   Python 3.8+
*   pip & venv
*   Git

**Pasos:**

1.  **Clona el repositorio:**
    ```bash
    git clone https://github.com/Alialmandoz/taller_escritura.git
    cd taller_escritura
    ```

2.  **Crea y activa un entorno virtual:**
    ```bash
    # En macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # En Windows
    python -m venv venv
    venv\Scripts\activate
    ```

3.  **Instala las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Ejecuta las migraciones de la base de datos:**
    ```bash
    python manage.py migrate
    ```

5.  **Crea un superusuario (administrador):**
    ```bash
    python manage.py createsuperuser
    ```

6.  **¡Inicia el servidor!**
    ```bash
    python manage.py runserver
    ```
    La aplicación estará disponible en `http://127.0.0.1:8000/escritura/`.

## 🗺️ Roadmap (Hoja de Ruta)

El progreso del proyecto y las próximas funcionalidades planeadas.

*   [x] **Fase 1: Fundamentos**
    *   [x] Autenticación y Perfiles de Usuario básicos.
    *   [x] CRUD completo para Escritos.
    *   [x] Sistema de visibilidad (Público, Privado, Borrador).
    *   [x] Integración de Editor de Texto Enriquecido (CKEditor).
*   [x] **Fase 2: Usabilidad y Diseño**
    *   [x] Implementación de plantilla base y estilos CSS globales.
    *   [x] Diseño responsivo inicial.
    *   [x] Sistema de Mensajes de Django.
    *   [x] Funcionalidad para expandir/contraer escritos en la lista.
*   [ ] **Fase 3: Interacción y Comunidad (Próximos Pasos)**
    *   [ ] Edición de perfil de usuario (bio, foto de perfil).
    *   [ ] Sistema de comentarios en los escritos.
    *   [ ] Paginación en la lista de escritos.
    *   [ ] Funcionalidad de búsqueda.
*   [ ] **Fase 4: Funcionalidades Avanzadas**
    *   [ ] Implementación de etiquetas/categorías para los escritos.
    *   [ ] Sistema de notificaciones (ej. "Alguien comentó tu escrito").
    *   [ ] Panel de Control (Dashboard) personalizado para el usuario.

## 🤝 Contribución

Las contribuciones son bienvenidas. Para errores o sugerencias, por favor, abre un *issue*. Para contribuir con código, sigue el flujo estándar de `Fork` -> `Crea una Rama` -> `Pull Request`.

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.