# Proyecto: LLMs locales con Ollama y Python

## Introducción
- Este proyecto demuestra cómo ejecutar modelos de lenguaje grandes (LLMs) de forma local con Ollama y consumirlos desde Python y Jupyter Notebooks.
- Sirve como guía de aprendizaje, base para experimentación y repositorio demostrativo.
- Todo el contenido está en español y orientado a perfiles de Data Science y Machine Learning.

## Qué es Ollama
- Ollama es una herramienta que permite descargar y ejecutar modelos LLM de forma local.
- Un LLM local significa que la inferencia ocurre en tu máquina, sin enviar datos a servicios externos.
- Ventajas:
  - Privacidad: los datos nunca salen de tu equipo.
  - Costos: sin tarifas por token o suscripciones a APIs.
  - Control: versionado de modelos y parametrización completa del entorno.

## Instalación de Ollama
- Windows:
  - Descarga el instalador desde https://ollama.com/download y sigue los pasos.
  - Verifica la instalación: `ollama --version`
- macOS:
  - `brew install ollama` o descarga desde la web oficial.
  - Verifica: `ollama --version`
- Linux:
  - Usa el script oficial: `curl -fsSL https://ollama.com/install.sh | sh`
  - Verifica: `ollama --version`
- Arranque del servicio:
  - Asegúrate de que el servidor de Ollama esté corriendo. En la mayoría de sistemas se inicia automáticamente.

## Descarga de modelos
- Lista de modelos instalados: `ollama list`
- Descarga ejemplos:
  - `ollama pull llama3`
  - `ollama pull mistral`
- Buenas prácticas:
  - Elige modelos acordes a tu hardware (VRAM/CPU).
  - Mantén un conjunto pequeño de modelos para pruebas rápidas.

## Requisitos del sistema
- CPU moderna; se recomienda GPU para acelerar algunos modelos.
- Memoria suficiente para el modelo (consultar documentación del modelo).
- Python 3.9+.

## Entorno virtual (venv)
- Crear entorno virtual:
  - Windows (PowerShell): `python -m venv .venv`
  - Linux/macOS: `python3 -m venv .venv`
- Activar:
  - Windows (PowerShell): `.\\.venv\\Scripts\\Activate.ps1`
  - Linux/macOS: `source .venv/bin/activate`
- Instalar dependencias:
  - `pip install -r requirements.txt`

## Dependencias
- ollama: cliente Python para interactuar con el servidor local de Ollama.
- jupyter: entorno de notebooks interactivos.
- ipykernel: kernel de Python para Jupyter.

## Estructura del proyecto
- notebooks: cuadernos educativos paso a paso.
- scripts: utilidades de línea de comandos y funciones reutilizables.
- data: datos de ejemplo.
- docs: documentación de arquitectura del proyecto.

## Uso básico de Ollama con Python
- Asegúrate de que Ollama esté activo y que el modelo esté descargado (por ejemplo, `llama3`).
- Ejemplo mínimo:
  - `from ollama import Client`
  - `client = Client(host='http://localhost:11434')`
  - `res = client.chat(model='llama3', messages=[{'role':'user','content':'Hola, ¿qué puedes hacer?'}])`
  - `print(res['message']['content'])`

## Ejecución de scripts
- `python scripts/run_model.py --model llama3 --prompt "Explica brevemente qué es un LLM"`
- También puedes usar `--prompt_file data/textos_ejemplo.txt` para leer el prompt desde archivo.

## Uso de notebooks
- Inicia Jupyter:
  - `jupyter notebook`
- Abre los cuadernos en la carpeta `notebooks` en orden:
  - [01_introduccion_llm_y_ollama.ipynb](notebooks/01_introduccion_llm_y_ollama.ipynb)
  - [02_instalacion_y_descarga_modelos.ipynb](notebooks/02_instalacion_y_descarga_modelos.ipynb)
  - [03_inferencia_basica_con_python.ipynb](notebooks/03_inferencia_basica_con_python.ipynb)
  - [04_prompt_engineering.ipynb](notebooks/04_prompt_engineering.ipynb)
  - [05_ejemplos_de_uso_practico.ipynb](notebooks/05_ejemplos_de_uso_practico.ipynb)
  - [06_caso_aplicado_data_science.ipynb](notebooks/06_caso_aplicado_data_science.ipynb)

## Casos de uso
- Resumen automático de texto, clasificación, extracción de información, reescritura de contenido.
- Asistente para análisis exploratorio de datos y documentación técnica.

## Buenas prácticas
- Mantén prompts claros y específicos; usa rol de sistema para contexto persistente.
- Controla parámetros del modelo (temperatura, top_p) según el caso.
- Versiona tus prompts y guarda resultados para reproducibilidad.

## Créditos y referencias
- Ollama: https://ollama.com/
- Modelos (ejemplos): Llama 3, Mistral
- Comunidad y foros: consulta repositorios y discusiones sobre LLMs locales.

