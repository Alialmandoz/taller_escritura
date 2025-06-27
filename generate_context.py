import os
import fnmatch # Para patrones de nombres de archivo
from pathlib import Path
import datetime # Para la fecha de generación

# --- CONFIGURACIÓN ---
# Directorio raíz del proyecto (asume que el script se ejecuta desde aquí)
PROJECT_ROOT = Path(".") 

# Extensiones de archivo de código/texto que queremos incluir
# Añade o quita según sea necesario
TEXT_FILE_EXTENSIONS = [
    '.py', '.html', '.css', '.js', '.md', '.txt', 
    '.yml', '.yaml', '.json', '.toml', '.ini', '.sh', '.bat'
]

# Directorios a excluir completamente (ej. entornos virtuales, cachés, etc.)
# Usamos nombres de directorio, no rutas completas inicialmente
EXCLUDE_DIRS = [
    'venv', '.venv', '__pycache__', '.git', '.vscode', '.idea', 
    'staticfiles_production', # Directorio generado por collectstatic
    'media', # Si tuvieras archivos subidos por usuarios
    # Añade aquí otros directorios que no sean relevantes para el contexto del código fuente
    # 'node_modules', 'build', 'dist', etc.
]

# Archivos específicos a excluir (por nombre exacto)
EXCLUDE_FILES = [
    'db.sqlite3', # Base de datos SQLite
    '.env',       # Archivo de variables de entorno (sensible)
    # Añade aquí archivos específicos que no quieras incluir
    # 'local_settings.py', 'secrets.json', etc.
]

# Patrones de archivo a excluir (estilo glob)
EXCLUDE_PATTERNS = [
    '*.pyc', '*.sqlite3-journal', '*.log', # Archivos compilados, journal de BD, logs
    # 'migrations/*', # Podrías excluir todas las migraciones si son muchas y no tan relevantes para el contexto general
]

# Máximo tamaño de archivo a leer (en bytes) para evitar leer archivos muy grandes accidentalmente
MAX_FILE_SIZE_BYTES = 2 * 1024 * 1024  # 2MB

# Archivo de salida donde se guardará el contexto
OUTPUT_FILE_NAME = "project_structure_and_content_tree.md"
# --- FIN CONFIGURACIÓN ---


def should_exclude(path: Path, root_path: Path) -> bool:
    """
    Verifica si una ruta (archivo o directorio) debe ser excluida.
    """
    # Excluir por nombre de archivo exacto
    if path.name in EXCLUDE_FILES:
        return True

    # Excluir por patrón de archivo
    for pattern in EXCLUDE_PATTERNS:
        if fnmatch.fnmatch(path.name, pattern):
            return True
        # Para patrones que podrían incluir directorios, como 'migrations/*'
        # necesitamos comparar la ruta relativa.
        try:
            relative_path_str = str(path.relative_to(root_path))
            if fnmatch.fnmatch(relative_path_str, pattern) or \
               fnmatch.fnmatch(relative_path_str.replace('\\', '/'), pattern): # Normalizar separadores
                return True
        except ValueError: # Si path no está bajo root_path (no debería pasar con os.walk)
            pass


    # Excluir si algún componente del path es un directorio excluido
    # Esto maneja la exclusión de directorios completos y sus contenidos
    # Comparamos partes de la ruta relativa para no excluir accidentalmente
    # un directorio con el mismo nombre en una ubicación diferente si EXCLUDE_DIRS
    # solo contiene nombres base.
    try:
        relative_path_parts = path.relative_to(root_path).parts
        for part in relative_path_parts:
            if part in EXCLUDE_DIRS:
                return True
    except ValueError:
        pass
        
    # Caso especial: excluir el propio script de salida si está en el proyecto
    if path.name == OUTPUT_FILE_NAME or path.name == __file__: # Excluye también el propio script que se está ejecutando
        return True
        
    return False


def get_project_context(project_dir: Path, output_file: Path):
    """
    Recorre el proyecto, extrae la estructura y el contenido de archivos pertinentes,
    y lo guarda en un archivo Markdown.
    """
    skipped_files_binary_or_error = []
    skipped_files_too_large = []
    processed_files_count = 0
    
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"# Contenido del Proyecto: {project_dir.resolve().name}\n\n") # Usar resolve().name para el nombre del dir actual
        
        fecha_generacion = datetime.datetime.now()
        f.write(f"**Generado el:** {fecha_generacion.strftime('%Y-%m-%d %H:%M:%S')}\n\n")

        # 1. Estructura del Proyecto (Árbol)
        f.write("## Estructura del Proyecto\n\n```text\n")
        
        tree_paths = []
        root_display_name = project_dir.resolve().name # Nombre del directorio raíz para la primera línea

        for root, dirs, files in os.walk(project_dir, topdown=True):
            current_root_path = Path(root)
            
            # Filtrar directorios excluidos ANTES de descender
            # Aplicar el filtro de should_exclude también a los directorios que se listan
            original_dirs_count = len(dirs)
            dirs[:] = [d_name for d_name in dirs if not should_exclude(current_root_path / d_name, project_dir)]
            
            # Ordenar directorios y archivos para una salida consistente
            dirs.sort()
            files.sort()

            # Calcular nivel de indentación
            try:
                level_parts = current_root_path.relative_to(project_dir).parts
                level = len(level_parts)
            except ValueError: # current_root_path es project_dir
                level = 0

            if current_root_path == project_dir:
                tree_paths.append(f"{root_display_name}\n")
            else:
                indent = "│   " * (level -1) + "├── "
                tree_paths.append(f"{indent}{current_root_path.name}\n")

            file_indent = "│   " * level + "├── "
            for i, file_name in enumerate(files):
                file_path = current_root_path / file_name
                if not should_exclude(file_path, project_dir):
                    tree_paths.append(f"{file_indent}{file_name}\n")
        
        for line in tree_paths:
            f.write(line)

        f.write("```\n\n---\n\n")

        # 2. Contenido de los Archivos
        files_to_process = []
        for root, dirs, files in os.walk(project_dir, topdown=True):
            current_root_path = Path(root)
            # Re-aplicar filtro de directorios para la fase de recolección de archivos
            dirs[:] = [d_name for d_name in dirs if not should_exclude(current_root_path / d_name, project_dir)]
            dirs.sort() # Ordenar para consistencia
            files.sort() # Ordenar para consistencia


            for file_name in files:
                file_path = current_root_path / file_name
                if not should_exclude(file_path, project_dir):
                    files_to_process.append(file_path)
        
        # No es necesario ordenar files_to_process de nuevo aquí si os.walk y sort() ya lo hicieron consistentemente.
        # Pero si se quisiera un orden global absoluto: files_to_process.sort()

        for file_path in files_to_process:
            relative_file_path_str = str(file_path.relative_to(project_dir)).replace('\\', '/') # Normalizar separadores para display

            f.write(f"## Archivo: `{relative_file_path_str}`\n\n")
            
            if file_path.suffix.lower() not in TEXT_FILE_EXTENSIONS:
                f.write(f"[Contenido de '{file_path.name}' omitido (Extensión no listada: {file_path.suffix})]\n\n")
                skipped_files_binary_or_error.append(f"{relative_file_path_str} (Extensión no listada)")
                continue

            try:
                file_size = file_path.stat().st_size
                if file_size > MAX_FILE_SIZE_BYTES:
                    f.write(f"[Contenido de '{file_path.name}' omitido (Archivo demasiado grande: {file_size / (1024*1024):.2f} MB)]\n\n")
                    skipped_files_too_large.append(f"{relative_file_path_str} ({file_size / (1024*1024):.2f} MB)")
                    continue
            except OSError:
                f.write(f"[Contenido de '{file_path.name}' omitido (Error al obtener tamaño)]\n\n")
                skipped_files_binary_or_error.append(f"{relative_file_path_str} (Error tamaño)")
                continue

            try:
                with open(file_path, "r", encoding="utf-8", errors='ignore') as content_file:
                    content = content_file.read()
                
                lang = file_path.suffix.lower().lstrip('.')
                if lang == 'py': lang = 'python'
                elif lang == 'js': lang = 'javascript'
                elif lang == 'md': lang = 'markdown'
                elif lang == 'html' or lang == 'htm': lang = 'html'
                elif lang == 'css': lang = 'css'
                elif lang == 'json': lang = 'json'
                elif lang == 'yaml' or lang == 'yml': lang = 'yaml'
                elif lang == 'bat': lang = 'batch' # Para archivos .bat
                elif lang == 'sh': lang = 'shell'   # Para archivos .sh
                elif lang == 'txt': lang = 'text'   # Para archivos .txt
                # Añadir más mapeos si es necesario para otros tipos de texto plano

                f.write(f"```{lang}\n")
                f.write(content)
                f.write("\n```\n\n---\n\n")
                processed_files_count += 1
            except UnicodeDecodeError:
                f.write(f"[Contenido de '{file_path.name}' omitido (Binario, error de codificación/lectura)]\n\n")
                skipped_files_binary_or_error.append(f"{relative_file_path_str} (Error decodificación)")
            except Exception as e:
                f.write(f"[Contenido de '{file_path.name}' omitido (Error inesperado al leer: {e})]\n\n")
                skipped_files_binary_or_error.append(f"{relative_file_path_str} (Error: {e})")
        
        f.write("## Lista de Archivos con Contenido Omitido\n\n")
        f.write("*(Binarios, errores de codificación/lectura, o errores inesperados durante el procesamiento)*\n\n")
        if skipped_files_binary_or_error:
            for skipped in skipped_files_binary_or_error:
                f.write(f"- `{skipped}`\n")
        else:
            f.write("Ninguno.\n")
        f.write("\n")

        f.write("## Lista de Archivos Omitidos por Tamaño Excesivo\n\n")
        if skipped_files_too_large:
            for skipped_large in skipped_files_too_large:
                f.write(f"- `{skipped_large}`\n")
        else:
            f.write("Ninguno.\n")

    print(f"Contexto del proyecto guardado en: {output_file.resolve()}")
    print(f"Archivos procesados y contenido incluido: {processed_files_count}")
    if skipped_files_binary_or_error:
        print(f"Archivos omitidos por ser binarios o errores de lectura: {len(skipped_files_binary_or_error)}")
    if skipped_files_too_large:
        print(f"Archivos omitidos por tamaño excesivo: {len(skipped_files_too_large)}")


if __name__ == "__main__":
    # Construir la ruta al script actual para poder excluirlo
    # Esto es un poco más robusto para encontrar el nombre del script en ejecución
    current_script_name = Path(__file__).name
    if current_script_name not in EXCLUDE_FILES: # Evitar duplicados si ya está
        EXCLUDE_FILES.append(current_script_name)

    output_path = PROJECT_ROOT / OUTPUT_FILE_NAME
    
    if output_path.exists():
        user_input = input(f"El archivo '{OUTPUT_FILE_NAME}' ya existe. ¿Deseas sobrescribirlo? (s/N): ")
        if user_input.lower() != 's':
            print("Operación cancelada por el usuario.")
            exit()
            
    get_project_context(PROJECT_ROOT, output_path)