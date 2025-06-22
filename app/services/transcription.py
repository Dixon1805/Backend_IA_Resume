import whisper

model = whisper.load_model("base") # se carga el modelo Whisper base para transcripción de audio

def transcribe_audio(audio_path: str) -> str: # función para transcribir audio
    result = model.transcribe(audio_path) # se transcribe el audio
    return result["text"] # se devuelve el texto transcrito
