from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas, database, auth

router = APIRouter(
    prefix="/professores",
    tags=["professores"]
)

# LISTAR
@router.get("/", response_model=List[schemas.ProfessorResponse])
def listar_professores(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    return db.query(models.Professor).offset(skip).limit(limit).all()

# CRIAR - PROTEGIDO
@router.post("/", response_model=schemas.ProfessorResponse, status_code=status.HTTP_201_CREATED)
def criar_professor(prof: schemas.ProfessorCreate, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    db_prof = db.query(models.Professor).filter(models.Professor.email == prof.email).first()
    if db_prof:
        raise HTTPException(status_code=400, detail="Email de professor já cadastrado")
    
    novo_prof = models.Professor(**prof.dict())
    db.add(novo_prof)
    db.commit()
    db.refresh(novo_prof)
    return novo_prof

# BUSCAR POR ID
@router.get("/{prof_id}", response_model=schemas.ProfessorResponse)
def obter_professor(prof_id: int, db: Session = Depends(database.get_db)):
    prof = db.query(models.Professor).filter(models.Professor.id == prof_id).first()
    if not prof:
        raise HTTPException(status_code=404, detail="Professor não encontrado")
    return prof

# DELETAR - PROTEGIDO
@router.delete("/{prof_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_professor(prof_id: int, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    prof = db.query(models.Professor).filter(models.Professor.id == prof_id).first()
    if not prof:
        raise HTTPException(status_code=404, detail="Professor não encontrado")
    
    db.delete(prof)
    db.commit()
    return None
