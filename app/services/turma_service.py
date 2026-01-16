from sqlalchemy.orm import Session
from .. import models, schemas

def create(db: Session, turma: schemas.TurmaCreate):
    db_turma = models.Turma(**turma.dict())
    db.add(db_turma)
    db.commit()
    db.refresh(db_turma)
    return db_turma

def get_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Turma).offset(skip).limit(limit).all()

def get_by_id(db: Session, turma_id: int):
    return db.query(models.Turma).filter(models.Turma.id == turma_id).first()

def update(db: Session, turma_id: int, turma_data: schemas.TurmaCreate):
    db_turma = db.query(models.Turma).filter(models.Turma.id == turma_id).first()
    if db_turma:
        for key, value in turma_data.dict().items():
            setattr(db_turma, key, value)
        db.commit()
        db.refresh(db_turma)
    return db_turma

def delete(db: Session, turma_id: int):
    db_turma = db.query(models.Turma).filter(models.Turma.id == turma_id).first()
    if db_turma:
        db.delete(db_turma)
        db.commit()
    return db_turma
