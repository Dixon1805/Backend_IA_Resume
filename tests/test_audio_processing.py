import os
from app.services import audioProcessing

def test_extract_audio_from_video():
    input_video = "tests/video.mp4"
    assert os.path.exists(input_video), "El archivo sample.mp4 no existe en la carpeta tests"

    audio_path = audioProcessing.extract_audio_from_video(input_video)

    # Verifica que el archivo de audio fue creado
    assert os.path.exists(audio_path), "El archivo de audio no fue creado por FFmpeg"
    assert audio_path.endswith(".wav")

    # Imprime la ruta del archivo generado
    print(f"Archivo de audio generado: {audio_path}")

    # Limpieza
    os.remove(audio_path)