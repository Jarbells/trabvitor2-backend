from sqlalchemy.orm import Session
from .. import models, schemas

def create(db: Session, disciplina: schemas.DisciplinaCreate):
    db_disc = models.Disciplina(**disciplina.dict())
    db.add(db_disc)
    db.commit()
    db.refresh(db_disc)
    return db_disc

def get_all(db: Session):
    return db.query(models.Disciplina).all()

def get_by_id(db: Session, disc_id: int):
    return db.query(models.Disciplina).filter(models.Disciplina.id == disc_id).first()

def update(db: Session, disc_id: int, disc_data: schemas.DisciplinaCreate):
    db_disc = db.query(models.Disciplina).filter(models.Disciplina.id == disc_id).first()
    if db_disc:
        for key, value in disc_data.dict().items():
            setattr(db_disc, key, value)
        db.commit()
        db.refresh(db_disc)
    return db_disc

def delete(db: Session, disc_id: int):
    db_disc = db.query(models.Disciplina).filter(models.Disciplina.id == disc_id).first()
    if db_disc:
        db.delete(db_disc)
        db.commit()
    return db_disc
