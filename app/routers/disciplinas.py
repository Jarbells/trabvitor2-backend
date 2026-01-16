from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, database, models, auth
from ..services import disciplina_service

router = APIRouter(prefix="/disciplinas", tags=["disciplinas"])

@router.post("/", response_model=schemas.DisciplinaResponse, status_code=status.HTTP_201_CREATED)
def criar_disciplina(disc: schemas.DisciplinaCreate, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    return disciplina_service.create(db, disc)

@router.get("/", response_model=List[schemas.DisciplinaResponse])
def listar_disciplinas(db: Session = Depends(database.get_db)):
    return disciplina_service.get_all(db)

@router.get("/{disc_id}", response_model=schemas.DisciplinaResponse)
def obter_disciplina(disc_id: int, db: Session = Depends(database.get_db)):
    disc = disciplina_service.get_by_id(db, disc_id)
    if not disc:
        raise HTTPException(status_code=404, detail="Disciplina não encontrada")
    return disc

@router.put("/{disc_id}", response_model=schemas.DisciplinaResponse)
def atualizar_disciplina(disc_id: int, disc: schemas.DisciplinaCreate, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    disc_atualizada = disciplina_service.update(db, disc_id, disc)
    if not disc_atualizada:
        raise HTTPException(status_code=404, detail="Disciplina não encontrada")
    return disc_atualizada

@router.delete("/{disc_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_disciplina(disc_id: int, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    disc = disciplina_service.get_by_id(db, disc_id)
    if not disc:
        raise HTTPException(status_code=404, detail="Disciplina não encontrada")
    disciplina_service.delete(db, disc_id)
    return None
