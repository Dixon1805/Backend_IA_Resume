import os
from app.services import transcription, audioProcessing  # Ajusta import según tu estructura

def test_extract_and_transcribe():
    video_path = "tests/video.mp4"  # Video de prueba, debe existir
    
    # Verificamos que el video exista
    assert os.path.exists(video_path), "El archivo video.mp4 no existe en la carpeta tests"

    # Extraemos el audio del video
    audio_path = audioProcessing.extract_audio_from_video(video_path)

    # Verificamos que se creó el archivo .wav
    assert os.path.exists(audio_path), "No se creó el archivo de audio"

    # Transcribimos el audio
    texto = transcription.transcribe_audio(audio_path)

    # Verificamos que la transcripción sea una cadena no vacía
    assert isinstance(texto, str)
    assert texto.strip() != ""

    print("Texto transcrito:", texto)

    # Limpiamos archivo generado
    if os.path.exists(audio_path):
        os.remove(audio_path)
