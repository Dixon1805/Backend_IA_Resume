import requests

OLLAMA_URL = "http://localhost:11434"
MODEL_NAME = "gemma3:latest"  # cambia a gemma

def summarize_text(text: str) -> str:
    prompt = f"Resume el siguiente texto de forma clara, concisa y en español:\n\n{text}\n\nResumen:"
    try:
        response = requests.post(
             f"{OLLAMA_URL}/api/generate",
            json={
                "model": MODEL_NAME,
                "prompt": prompt,
                "stream": False
            },
            timeout=600
        )
        response.raise_for_status()
        result = response.json()
        return result.get("response", "").strip()
    except Exception as e:
        return f"Error al resumir con Gemma: {str(e)}"
