from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, database, models, auth
from ..services import professor_service

router = APIRouter(prefix="/professores", tags=["professores"])

@router.post("/", response_model=schemas.ProfessorResponse, status_code=status.HTTP_201_CREATED)
def criar_professor(prof: schemas.ProfessorCreate, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    return professor_service.create(db, prof)

@router.get("/", response_model=List[schemas.ProfessorResponse])
def listar_professores(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    return professor_service.get_all(db, skip, limit)

@router.get("/{prof_id}", response_model=schemas.ProfessorResponse)
def obter_professor(prof_id: int, db: Session = Depends(database.get_db)):
    prof = professor_service.get_by_id(db, prof_id)
    if not prof:
        raise HTTPException(status_code=404, detail="Professor não encontrado")
    return prof

@router.put("/{prof_id}", response_model=schemas.ProfessorResponse)
def atualizar_professor(prof_id: int, prof: schemas.ProfessorCreate, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    prof_atualizado = professor_service.update(db, prof_id, prof)
    if not prof_atualizado:
        raise HTTPException(status_code=404, detail="Professor não encontrado")
    return prof_atualizado

@router.delete("/{prof_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_professor(prof_id: int, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    prof = professor_service.get_by_id(db, prof_id)
    if not prof:
        raise HTTPException(status_code=404, detail="Professor não encontrado")
    professor_service.delete(db, prof_id)
    return None
