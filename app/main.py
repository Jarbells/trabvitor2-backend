from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models, database
from .routers import alunos, auth, professores, disciplinas, turmas

# Cria tabelas
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Gestão Escolar Pro API", version="1.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclusão dos 5 módulos de rotas
app.include_router(auth.router)
app.include_router(alunos.router)
app.include_router(professores.router)
app.include_router(disciplinas.router)
app.include_router(turmas.router)
