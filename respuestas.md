# Respuestas del Examen - Análisis de Sensores

## Respuestas Teóricas

1. **Entornos virtuales:** Aíslan las dependencias de cada proyecto para evitar conflictos de versiones con otros proyectos de Python en la misma máquina.
2. **Exclusión en .gitignore:** Se agregó `env/` para no subir la carpeta pesada del entorno virtual y `__pycache__/` para omitir los archivos compilados temporales.
3. **Rutas relativas:** Se utilizó `pathlib.Path(__file__).resolve().parent` para que las rutas a la carpeta `data/` funcionen de manera portable en Windows, Mac o Linux.
