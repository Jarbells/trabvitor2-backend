from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, database, models, auth
from ..services import aluno_service

router = APIRouter(prefix="/alunos", tags=["alunos"])

@router.post("/", response_model=schemas.AlunoResponse, status_code=status.HTTP_201_CREATED)
def criar_aluno(aluno: schemas.AlunoCreate, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    return aluno_service.create(db, aluno)

@router.get("/", response_model=List[schemas.AlunoResponse])
def listar_alunos(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    return aluno_service.get_all(db, skip, limit)

@router.get("/{aluno_id}", response_model=schemas.AlunoResponse)
def obter_aluno(aluno_id: int, db: Session = Depends(database.get_db)):
    aluno = aluno_service.get_by_id(db, aluno_id)
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return aluno

@router.put("/{aluno_id}", response_model=schemas.AlunoResponse)
def atualizar_aluno(aluno_id: int, aluno: schemas.AlunoCreate, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    aluno_atualizado = aluno_service.update(db, aluno_id, aluno)
    if not aluno_atualizado:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return aluno_atualizado

@router.delete("/{aluno_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_aluno(aluno_id: int, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    aluno = aluno_service.get_by_id(db, aluno_id)
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    aluno_service.delete(db, aluno_id)
    return None
