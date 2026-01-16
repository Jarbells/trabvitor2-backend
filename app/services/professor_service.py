from sqlalchemy.orm import Session
from .. import models, schemas

def create(db: Session, professor: schemas.ProfessorCreate):
    db_prof = models.Professor(**professor.dict())
    db.add(db_prof)
    db.commit()
    db.refresh(db_prof)
    return db_prof

def get_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Professor).offset(skip).limit(limit).all()

def get_by_id(db: Session, prof_id: int):
    return db.query(models.Professor).filter(models.Professor.id == prof_id).first()

def update(db: Session, prof_id: int, prof_data: schemas.ProfessorCreate):
    db_prof = db.query(models.Professor).filter(models.Professor.id == prof_id).first()
    if db_prof:
        for key, value in prof_data.dict().items():
            setattr(db_prof, key, value)
        db.commit()
        db.refresh(db_prof)
    return db_prof

def delete(db: Session, prof_id: int):
    db_prof = db.query(models.Professor).filter(models.Professor.id == prof_id).first()
    if db_prof:
        db.delete(db_prof)
        db.commit()
    return db_prof
