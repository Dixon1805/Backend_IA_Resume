from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router

app = FastAPI()

# Configurar CORS
origins = [
    "http://localhost:5173",  # tu frontend
    # Podés agregar más orígenes si querés
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,       # Permite solo estos orígenes
    allow_credentials=True,
    allow_methods=["*"],         # Permite todos los métodos (GET, POST, etc)
    allow_headers=["*"],         # Permite todos los headers
)

app.include_router(router, prefix="/api")
