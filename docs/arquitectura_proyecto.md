# Arquitectura del proyecto

## Objetivos
- Ejecutar LLMs localmente con Ollama y consumirlos desde Python y Jupyter.
- Facilitar experimentación con inferencia, prompt engineering y casos aplicados.
- Proveer documentación clara y reproducible.

## Organización
- README.md: guía principal del proyecto.
- requirements.txt: dependencias mínimas.
- .gitignore: archivos ignorados comunes.
- notebooks: cuadernos educativos y prácticos.
- scripts: utilidades reutilizables para prompts e inferencia por consola.
- data: textos y archivos de ejemplo.
- docs: documentación de arquitectura y notas técnicas.

## Flujo de trabajo recomendado
- Preparar el entorno virtual y dependencias.
- Instalar y verificar Ollama; descargar los modelos necesarios.
- Explorar los notebooks en orden progresivo.
- Reutilizar `scripts/run_model.py` para validar prompts y flujos desde consola.
- Iterar prompts en `scripts/prompts.py` y funciones en `scripts/utils.py`.

## Buenas prácticas
- Asegurar reproducibilidad con versiones de modelos y parámetros.
- Separar prompts reutilizables y utilidades en módulos claros.
- Mantener los notebooks con narrativa y ejemplos autocontenidos.

