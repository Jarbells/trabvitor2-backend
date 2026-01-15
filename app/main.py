from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models, database
from .routers import alunos, professores, auth

# CRIA AS TB'S QUANDO INICIA
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(
    title="Gestão Escolar Digital API",
    description="API para gerenciamento de alunos, professores e turmas.",
    version="1.0.0"
)

# CONFIGURAÇÕES CORS (PERMITIR QUE O REACT NA PORTA 5173 ACESSE A API)
origins = [
    "http://localhost:5173",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ADD AS ROTAS
app.include_router(auth.router)
app.include_router(alunos.router)
app.include_router(professores.router)

@app.get("/")
def read_root():
    return {"message": "API Gestão Escolar rodando!"}
