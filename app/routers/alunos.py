from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas, database, auth

router = APIRouter(
    prefix="/alunos",
    tags=["alunos"]
)

# LISTAR
@router.get("/", response_model=List[schemas.AlunoResponse])
def listar_alunos(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    alunos = db.query(models.Aluno).offset(skip).limit(limit).all()
    return alunos

# CRIAR - PROTEGIDO
@router.post("/", response_model=schemas.AlunoResponse, status_code=status.HTTP_201_CREATED)
def criar_aluno(aluno: schemas.AlunoCreate, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    # Verifica se matrícula já existe
    db_aluno = db.query(models.Aluno).filter(models.Aluno.matricula == aluno.matricula).first()
    if db_aluno:
        raise HTTPException(status_code=400, detail="Matrícula já cadastrada")
    
    novo_aluno = models.Aluno(**aluno.dict())
    db.add(novo_aluno)
    db.commit()
    db.refresh(novo_aluno)
    return novo_aluno

# BUSCAR POR ID
@router.get("/{aluno_id}", response_model=schemas.AlunoResponse)
def obter_aluno(aluno_id: int, db: Session = Depends(database.get_db)):
    aluno = db.query(models.Aluno).filter(models.Aluno.id == aluno_id).first()
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return aluno

# ATUALIZAR - PROTEGIDO
@router.put("/{aluno_id}", response_model=schemas.AlunoResponse)
def atualizar_aluno(aluno_id: int, aluno_update: schemas.AlunoUpdate, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    db_aluno = db.query(models.Aluno).filter(models.Aluno.id == aluno_id).first()
    if not db_aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    
    # SÓ ATUALIZA OS ENVIADOS
    for key, value in aluno_update.dict(exclude_unset=True).items():
        setattr(db_aluno, key, value)
    
    db.commit()
    db.refresh(db_aluno)
    return db_aluno

# DELETAR - PROTEGIDO
@router.delete("/{aluno_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_aluno(aluno_id: int, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    db_aluno = db.query(models.Aluno).filter(models.Aluno.id == aluno_id).first()
    if not db_aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    
    db.delete(db_aluno)
    db.commit()
    return None
