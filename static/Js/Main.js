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
        const content = item.querySelector('.escrito-content');
        const toggleButton = item.querySelector('.toggle-button');

        if (!content || !toggleButton) return;

        const buttonText = toggleButton.querySelector('.button-text');

        if (content.scrollHeight <= content.clientHeight) {
            toggleButton.style.display = 'none';
        } else {
            buttonText.textContent = 'Leer más';
            toggleButton.setAttribute('aria-expanded', 'false');
        }

        toggleButton.addEventListener('click', () => {
            item.classList.toggle('is-expanded');

            const isExpanded = item.classList.contains('is-expanded');
            toggleButton.setAttribute('aria-expanded', isExpanded);

            if (isExpanded) {
                buttonText.textContent = 'Leer menos';
            } else {
                buttonText.textContent = 'Leer más';
            }
        });
    });
});