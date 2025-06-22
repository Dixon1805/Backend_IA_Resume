import subprocess
import os

def extract_audio_from_video(video_path: str) -> str:
    audio_path = "temp_audio.wav"
    # Usar ffmpeg para extraer audio
    command = [
        "ffmpeg", "-i", video_path, "-vn", "-acodec", "pcm_s16le", "-ar", "44100", "-ac", "2", audio_path
    ]
    subprocess.run(command, check=True)
    return audio_path
