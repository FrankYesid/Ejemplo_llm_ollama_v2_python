def build_messages(user_content: str, system_content: str | None = None):
    messages = []
    if system_content:
        messages.append({"role": "system", "content": system_content})
    messages.append({"role": "user", "content": user_content})
    return messages


def prompt_resumen(texto: str):
    system = (
        "Eres un asistente experto en resumen de textos en español. "
        "Prioriza claridad y fidelidad al contenido."
    )
    user = (
        "Resume el siguiente texto en 5-7 líneas, destacando ideas clave y conclusiones. "
        "Texto:\n\n" + texto
    )
    return build_messages(user, system)


def prompt_clasificacion(texto: str, etiquetas: list[str]):
    system = "Eres un asistente de clasificación de texto. Devuelve una única etiqueta."
    user = (
        "Clasifica el siguiente texto en una de estas etiquetas: "
        + ", ".join(etiquetas)
        + ". Texto:\n\n"
        + texto
        + "\n\nFormato de salida: solo la etiqueta."
    )
    return build_messages(user, system)


def prompt_extraccion(texto: str, campos: list[str]):
    system = "Eres un asistente que extrae información en formato JSON válido."
    user = (
        "Extrae los siguientes campos del texto y devuelve un JSON con claves exactas: "
        + ", ".join(campos)
        + ". Texto:\n\n"
        + texto
    )
    return build_messages(user, system)


def prompt_reescritura(texto: str, tono: str):
    system = "Eres un asistente de redacción en español."
    user = (
        "Reescribe el siguiente texto en un tono "
        + tono
        + ", manteniendo el significado y mejorando claridad:\n\n"
        + texto
    )
    return build_messages(user, system)


def prompt_eda(contexto: str, instrucciones: str | None = None):
    system = (
        "Eres un asistente para análisis exploratorio de datos (EDA). "
        "Genera hipótesis, preguntas y sugerencias de análisis."
    )
    user = "Contexto del proyecto:\n" + contexto
    if instrucciones:
        user += "\n\nRequisitos adicionales:\n" + instrucciones
    return build_messages(user, system)

