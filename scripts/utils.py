import json
import re
import urllib.request
from pathlib import Path


def safe_read_file(path: Path) -> str:
    with path.open("r", encoding="utf-8") as f:
        return f.read()


def clean_text(text: str) -> str:
    text = text.strip()
    text = re.sub(r"\s+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text


def is_ollama_running() -> bool:
    try:
        with urllib.request.urlopen("http://localhost:11434/api/tags", timeout=3) as resp:
            data = resp.read().decode("utf-8")
            json.loads(data)
        return True
    except Exception:
        return False

