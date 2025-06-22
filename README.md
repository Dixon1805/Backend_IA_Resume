# Backend_IA_Resume

linea de ejecucion
uvicorn app.main:app --reload --port 5000

activar entorno 
.venv\Scripts\activate

ejecucion de pruebas sin consola de test_audio_processing.py
python -m pytest tests/test_audio_processing.py

ejecucion de pruebas con consola de test_audio_processing.py
python -m pytest -s tests/test_audio_processing.py

para ejecutar todas las pruebas unitarias
python -m pytest -s tests/
