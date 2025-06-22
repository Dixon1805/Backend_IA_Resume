from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from app.services import audioProcessing
from app.services import transcription
from app.services import summarization

import os
import shutil
import uuid

router = APIRouter() 

@router.post("/get/video") # Ruta para procesar el video
async def process_video(video: UploadFile = File(...)): # Parametro video es un archivo de video
    tmp_filename = f"tmp_{uuid.uuid4().hex}_{video.filename}" # Genera un nombre temporal único para el archivo
    video_path = os.path.join("tmp", tmp_filename) # Ruta temporal para guardar el video
    os.makedirs("tmp", exist_ok=True) # Crea el directorio tmp si no existe

    with open(video_path, "wb") as buffer: # Abre el archivo en modo binario
        shutil.copyfileobj(video.file, buffer) # Copia el contenido del archivo subido al archivo temporal

    audio_path = None
    transcript_path = None
    summary_path = None

    try: # Intenta procesar el video
        audio_path = audioProcessing.extract_audio_from_video(video_path) # Extrae el audio del video 
        text = transcription.transcribe_audio(audio_path) # Transcribe el audio a texto
        summary = summarization.summarize_text(text) #resume texto

        transcript_path = "transcription.txt"
        summary_path = "summary.txt"
        with open(transcript_path, "w", encoding="utf-8") as f:
            f.write(text)
        with open(summary_path, "w", encoding="utf-8") as f:
            f.write(summary)

        return { # Devuelve un diccionario con los resultados
            "transcription": text,
            "summary": summary
        }
    except Exception as e: # Si ocurre un error durante el procesamiento
        return {
            "recibi el video": video.filename,
            "error": str(e)
        }
    finally: # Finalmente, limpia los archivos temporales
        for path in [video_path, audio_path, transcript_path, summary_path]:
            if path and os.path.exists(path):
                os.remove(path)