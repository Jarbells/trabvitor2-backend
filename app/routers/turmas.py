from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, database, models, auth
from ..services import turma_service

router = APIRouter(prefix="/turmas", tags=["turmas"])

@router.post("/", response_model=schemas.TurmaResponse, status_code=status.HTTP_201_CREATED)
def criar_turma(turma: schemas.TurmaCreate, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    return turma_service.create(db, turma)

@router.get("/", response_model=List[schemas.TurmaResponse])
def listar_turmas(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    return turma_service.get_all(db, skip, limit)

@router.get("/{turma_id}", response_model=schemas.TurmaResponse)
def obter_turma(turma_id: int, db: Session = Depends(database.get_db)):
    turma = turma_service.get_by_id(db, turma_id)
    if not turma:
        raise HTTPException(status_code=404, detail="Turma não encontrada")
    return turma

@router.put("/{turma_id}", response_model=schemas.TurmaResponse)
def atualizar_turma(turma_id: int, turma: schemas.TurmaCreate, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    turma_atualizada = turma_service.update(db, turma_id, turma)
    if not turma_atualizada:
        raise HTTPException(status_code=404, detail="Turma não encontrada")
    return turma_atualizada

@router.delete("/{turma_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_turma(turma_id: int, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    turma = turma_service.get_by_id(db, turma_id)
    if not turma:
        raise HTTPException(status_code=404, detail="Turma não encontrada")
    turma_service.delete(db, turma_id)
    return None
