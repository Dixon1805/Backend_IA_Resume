import requests

OLLAMA_URL = "http://localhost:11434" # se indica la url del servidor de ollama
MODEL_NAME = "gemma3:latest"  # se indica el modelo a utilizar, en este caso gemma3

def summarize_text(text: str) -> str:
    prompt = f"Resume el siguiente texto de forma clara, concisa y en español:\n\n{text}\n\nResumen:" # se define el prompt que se le enviará al modelo para resumir el texto
    try: # se intenta enviar el prompt al servidor de ollama
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
        return result.get("response", "").strip() # se obtiene el resumen del texto desde la respuesta del modelo
    except Exception as e:
        return f"Error al resumir con Gemma: {str(e)}"
