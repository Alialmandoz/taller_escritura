// static/js/main.js

// Usamos 'DOMContentLoaded' para asegurarnos de que el script se ejecuta
// solo después de que todo el HTML de la página se haya cargado y parseado.
// Es una buena práctica para evitar errores de "elemento no encontrado".
document.addEventListener('DOMContentLoaded', function () {

    // SECCIÓN: Lógica para contraer/expandir escritos en la lista
    // -----------------------------------------------------------

    // 1. Seleccionamos todos los elementos de la lista de escritos.
    const escritoItems = document.querySelectorAll('.escrito-item');

    // 2. Iteramos sobre cada elemento de la lista para añadirle la funcionalidad.
    escritoItems.forEach(item => {
        // Encontramos el contenido y el botón dentro de cada item.
        const content = item.querySelector('.escrito-content');
        const toggleButton = item.querySelector('.toggle-button');

        // Si no encontramos el contenido o el botón, saltamos al siguiente item.
        if (!content || !toggleButton) return;

        // Por defecto, comprobamos si el contenido es más alto que nuestra altura colapsada.
        // Si no lo es, no necesitamos el botón, así que lo ocultamos.
        // `scrollHeight` es la altura total del contenido, `clientHeight` es la altura visible.
        if (content.scrollHeight <= content.clientHeight) {
            toggleButton.style.display = 'none';
        }

        // 3. Añadimos un 'escuchador de eventos' al botón.
        //    Esto ejecuta una función cada vez que el usuario hace clic en el botón.
        toggleButton.addEventListener('click', () => {
            // `classList.toggle` es un método muy útil:
            // - Si la clase 'is-expanded' existe en el 'item', la quita.
            // - Si la clase 'is-expanded' no existe, la añade.
            // Esto nos permite cambiar entre los dos estados con una sola línea.
            item.classList.toggle('is-expanded');

            // MEJORA DE ACCESIBILIDAD: Actualizamos el atributo aria-expanded.
            const isExpanded = item.classList.contains('is-expanded');
            toggleButton.setAttribute('aria-expanded', isExpanded);
        });
    });
});