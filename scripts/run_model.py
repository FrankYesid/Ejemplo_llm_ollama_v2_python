import argparse
import json
import sys
from pathlib import Path
from ollama import Client
from .utils import safe_read_file, clean_text
from .prompts import build_messages


def run(model: str, prompt: str, system: str | None, temperature: float | None, top_p: float | None,
        seed: int | None, max_tokens: int | None, format_output: str) -> None:
    client = Client(host="http://localhost:11434")
    messages = build_messages(user_content=prompt, system_content=system)
    options = {}
    if temperature is not None:
        options["temperature"] = float(temperature)
    if top_p is not None:
        options["top_p"] = float(top_p)
    if seed is not None:
        options["seed"] = int(seed)
    if max_tokens is not None:
        options["num_predict"] = int(max_tokens)
    res = client.chat(model=model, messages=messages, options=options)
    content = res.get("message", {}).get("content", "")
    content = clean_text(content)
    if format_output == "json":
        print(json.dumps({"model": model, "content": content}, ensure_ascii=False))
    else:
        print(content)


def main() -> None:
    parser = argparse.ArgumentParser(description="Ejecuta un modelo Ollama desde consola.")
    parser.add_argument("--model", default="llama3", help="Nombre del modelo (ej. llama3, mistral).")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--prompt", help="Texto del prompt.")
    group.add_argument("--prompt_file", help="Ruta a archivo de texto con el prompt.")
    parser.add_argument("--system", help="Contexto de sistema opcional.")
    parser.add_argument("--temperature", type=float, help="Temperatura del muestreo.")
    parser.add_argument("--top_p", type=float, help="Top-p del muestreo.")
    parser.add_argument("--seed", type=int, help="Semilla para reproducibilidad.")
    parser.add_argument("--max_tokens", type=int, help="Límite de tokens generados.")
    parser.add_argument("--format", choices=["text", "json"], default="text", help="Formato de salida.")
    args = parser.parse_args()
    if args.prompt_file:
        path = Path(args.prompt_file)
        if not path.exists():
            print(f"Archivo no encontrado: {path}", file=sys.stderr)
            sys.exit(1)
        prompt_text = safe_read_file(path)
    else:
        prompt_text = args.prompt or ""
    prompt_text = clean_text(prompt_text)
    run(
        model=args.model,
        prompt=prompt_text,
        system=args.system,
        temperature=args.temperature,
        top_p=args.top_p,
        seed=args.seed,
        max_tokens=args.max_tokens,
        format_output=args.format,
    )


if __name__ == "__main__":
    main()

