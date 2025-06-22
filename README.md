# Backend_IA_Resume

linea de ejecucion
uvicorn app.main:app --reload --port 5000


ejecucion de pruebas sin consola
python -m pytest tests/test_audio_processing.py

ejecucion de pruebas con consola
python -m pytest -s tests/test_audio_processing.py
